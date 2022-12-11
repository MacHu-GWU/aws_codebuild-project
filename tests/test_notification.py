# -*- coding: utf-8 -*-

import typing as T
import re
import enum
import json
import dataclasses
from pathlib import Path
from datetime import datetime

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
    return CBE.from_codebuid_notification_event(
        read_json(f"{dir_codebuild_events / fname}")
    )


class Value(T.NamedTuple):
    v: CodeBuildEvent


class CBEventEnum(Value, enum.Enum):
    state_in_progress = Value(v=read_cb_event("21-build-state-change-in-progress.json"))
    state_failed = Value(v=read_cb_event("22-build-state-change-failed.json"))
    state_succeeded = Value(v=read_cb_event("23-build-state-change-succeeded.json"))

    phase_change_pre_build = Value(
        v=read_cb_event("31-build-phase-change-pre-build.json")
    )


cb_event_list: T.List[CodeBuildEvent] = [value.v for value in CBEventEnum]


def test_properties():
    fields = [
        field
        for field in dataclasses.fields(CodeBuildEvent)
        if field.name not in ["_data", "bsm"]
    ]
    for value in CBEventEnum:
        for field in fields:
            getattr(value.v, field.name)


def test_is_method():
    for value in [
        CBEventEnum.state_in_progress,
        CBEventEnum.state_failed,
        CBEventEnum.state_succeeded,
    ]:
        value.v.is_state_change_event()
        value.v.is_phase_change_event()

        value.v.is_build_status_IN_PROGRESS()
        value.v.is_build_status_FAILED()
        value.v.is_build_status_SUCCEEDED()

    for value in [
        CBEventEnum.phase_change_pre_build,
    ]:

        value.v.is_state_change_event()
        value.v.is_phase_change_event()

        value.v.is_complete_phase_INITIALIZED()
        value.v.is_complete_phase_SUBMITTED()
        value.v.is_complete_phase_PROVISIONING()
        value.v.is_complete_phase_DOWNLOAD_SOURCE()
        value.v.is_complete_phase_INSTALL()
        value.v.is_complete_phase_PRE_BUILD()
        value.v.is_complete_phase_POST_BUILD()
        value.v.is_complete_phase_UPLOAD_ARTIFACTS()
        value.v.is_complete_phase_FINALIZING()
        value.v.is_complete_phase_COMPLETED()
        value.v.is_complete_phase_status_TIMED_OUT()
        value.v.is_complete_phase_status_FAILED()
        value.v.is_complete_phase_status_SUCCEEDED()
        value.v.is_complete_phase_status_STOPPED()
        value.v.is_complete_phase_status_FAULT()
        value.v.is_complete_phase_status_CLIENT_ERROR()


def test_attribute_value():
    assert CBEventEnum.state_in_progress.v.aws_account_id == "111122223333"
    assert CBEventEnum.state_in_progress.v.aws_region == "us-east-1"
    assert CBEventEnum.state_in_progress.v.project_name == "aws_codebuild-project"
    assert CBEventEnum.state_in_progress.v.build_number is None
    assert CBEventEnum.state_in_progress.v.build_start_datetime == datetime(
        2022, 7, 21, 0, 2, 19
    )
    assert CBEventEnum.state_in_progress.v.complete_phase_start_datetime is None
    assert CBEventEnum.state_in_progress.v.complete_phase_end_datetime is None

    _ = CBEventEnum.state_in_progress.v.console_url

    assert CBEventEnum.state_failed.v.build_number == 176
    assert CBEventEnum.state_succeeded.v.build_number == 99

    assert CBEventEnum.phase_change_pre_build.v.build_start_datetime == datetime(
        2022, 12, 11, 0, 44, 39
    )
    assert (
        CBEventEnum.phase_change_pre_build.v.complete_phase_start_datetime
        == datetime(2022, 12, 11, 0, 45, 35)
    )
    assert CBEventEnum.phase_change_pre_build.v.complete_phase_end_datetime == datetime(
        2022, 12, 11, 0, 45, 35
    )


def test_method_value():
    assert CBEventEnum.state_in_progress.v.is_build_status_IN_PROGRESS() is True
    assert CBEventEnum.state_failed.v.is_build_status_FAILED() is True
    assert CBEventEnum.state_failed.v.is_build_status_SUCCEEDED() is False
    assert CBEventEnum.state_succeeded.v.is_build_status_FAILED() is False
    assert CBEventEnum.state_succeeded.v.is_build_status_SUCCEEDED() is True
    assert CBEventEnum.state_in_progress.v.is_build_status_STOPPED() is False


def test_plain_text_env_var():
    assert CBEventEnum.phase_change_pre_build.v.plain_text_env_var == {
        "CI_DATA_COMMENT_ID": "7763f126-91f0-4a0b-8c78-9d4aa7ef3db7:b1cacec7-7638-4b2f-a4a1-84bb58d3b6e6",
        "CI_DATA_COMMIT_MESSAGE": "Update chore.txt\n",
    }


if __name__ == "__main__":
    from aws_codebuild.tests import run_cov_test

    run_cov_test(__file__, "aws_codebuild.notification", preview=False)
