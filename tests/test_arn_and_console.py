# -*- coding: utf-8 -*-

import pytest
import os

from aws_codebuild.arn_and_console import (
    BuildJobRun,
)


class TestBuildRun:
    def test(self):
        arn = "arn:aws:codebuild:us-east-1:111122223333:build/my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        build_run = BuildJobRun.from_arn(arn)
        assert build_run.aws_account_id == "111122223333"
        assert build_run.aws_region == "us-east-1"
        assert build_run.project_name == "my-project"
        assert build_run.run_id == "1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        assert build_run.arn == arn

        console_url = "https://us-east-1.console.aws.amazon.com/codesuite/codebuild/111122223333/projects/my-project/build/my-project%3A1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f/?region=us-east-1"
        build_run = BuildJobRun.from_console_url(console_url)
        assert build_run.aws_account_id == "111122223333"
        assert build_run.aws_region == "us-east-1"
        assert build_run.project_name == "my-project"
        assert build_run.run_id == "1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        assert (
            build_run.console_url
            == "https://us-east-1.console.aws.amazon.com/codesuite/codebuild/111122223333/projects/my-project/build/my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f/?region=us-east-1"
        )


if __name__ == "__main__":
    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
