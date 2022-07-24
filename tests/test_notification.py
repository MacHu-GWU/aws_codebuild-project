# -*- coding: utf-8 -*-

import pytest

from typing import List
import os
import re
import json
import dataclasses
from pathlib import Path
from datetime import datetime
from unittest.mock import patch, PropertyMock

from aws_codebuild.notification import (
    CodeBuildEventTypeEnum,
    CodeBuildEvent,
)

CBEventTypeEnum = CodeBuildEventTypeEnum
CBE = CodeBuildEvent


def strip_comment_line_with_symbol(line, start):
    """
    Strip comments from line string.
    """
    parts = line.split(start)
    counts = [len(re.findall(r'(?:^|[^"\\]|(?:\\\\|\\")+)(")', part)) for part in parts]
    total = 0
    for nr, count in enumerate(counts):
        total += count
        if total % 2 == 0:
            return start.join(parts[: nr + 1]).rstrip()
    else:  # pragma: no cover
        return line.rstrip()


def strip_comments(string, comment_symbols=frozenset(("#", "//"))):
    """
    Strip comments from json string.
    :param string: A string containing json with comments started by comment_symbols.
    :param comment_symbols: Iterable of symbols that start a line comment (default # or //).
    :return: The string with the comments removed.
    """
    lines = string.splitlines()
    for k in range(len(lines)):
        for symbol in comment_symbols:
            lines[k] = strip_comment_line_with_symbol(lines[k], start=symbol)
    return "\n".join(lines)


dir_codebuild_events = Path(__file__).absolute().parent / "events"


def read_json(file: str) -> dict:
    return json.loads(strip_comments(Path(file).read_text()))


def read_cb_event(fname: str) -> CBE:
    return CBE.from_event(
        read_json(f"{dir_codebuild_events / fname}")
    )


class CBEventEnum:
    state_in_progress = read_cb_event("21-build-state-change-in-progress.json")
    state_failed = read_cb_event("22-build-state-change-failed.json")
    state_succeeded = read_cb_event("23-build-state-change-succeeded.json")


cb_event_list: List[CodeBuildEvent] = [
    v for k, v in CBEventEnum.__dict__.items() if not k.startswith("_")
]


def test_properties():
    assert CBEventEnum.state_in_progress.awsAccountId == "111122223333"
    assert CBEventEnum.state_in_progress.awsRegion == "us-east-1"
    assert CBEventEnum.state_in_progress.buildUUID == "aws_codebuild-project:5d010eb5-6eeb-4966-9a07-6eadcd4def4e"
    assert CBEventEnum.state_in_progress.buildProject == "aws_codebuild-project"
    assert CBEventEnum.state_in_progress.buildId == "5d010eb5-6eeb-4966-9a07-6eadcd4def4e"
    assert CBEventEnum.state_in_progress.buildNumber == 0
    assert CBEventEnum.state_in_progress.buildStartTime == datetime(2022, 7, 21, 0, 2, 19)
    _ = CBEventEnum.state_in_progress.buildRunConsoleUrl

    assert CBEventEnum.state_failed.buildNumber == 176
    assert CBEventEnum.state_succeeded.buildNumber == 99


def test_event_type():
    assert CBEventEnum.state_in_progress.is_state_in_progress
    assert CBEventEnum.state_failed.is_state_failed
    assert CBEventEnum.state_succeeded.is_state_succeeded


def test_env_var_seder():
    env_var = CBEventEnum.state_succeeded.to_env_var(prefix="CUSTOM_")
    cb_event = CodeBuildEvent.from_env_var(env_var, prefix="CUSTOM_")
    assert (
        dataclasses.asdict(CBEventEnum.state_succeeded)
        == dataclasses.asdict(cb_event)
    )


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
