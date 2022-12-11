# -*- coding: utf-8 -*-

import enum
from aws_codebuild.arn_and_console import (
    BuildJobRun,
)


class ArnEnum(str, enum.Enum):
    build = "arn:aws:codebuild:us-east-1:111122223333:build/my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
    batch_build = "arn:aws:codebuild:us-east-1:111122223333:build-batch/my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"


class TestBuildRun:
    def test(self):
        build_job_run = BuildJobRun.from_arn(ArnEnum.build)
        assert build_job_run.is_batch is False
        assert build_job_run.aws_account_id == "111122223333"
        assert build_job_run.aws_region == "us-east-1"
        assert build_job_run.project_name == "my-project"
        assert build_job_run.run_id == "1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        assert build_job_run.arn == ArnEnum.build
        assert build_job_run.run_uuid == "my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"

        assert build_job_run.aws_account_id == "111122223333"
        assert build_job_run.aws_region == "us-east-1"
        assert build_job_run.project_name == "my-project"
        assert build_job_run.run_id == "1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        assert (
            build_job_run.console_url
            == "https://us-east-1.console.aws.amazon.com/codesuite/codebuild/111122223333/projects/my-project/build/my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f/?region=us-east-1"
        )
        _ = build_job_run.phase_console_url
        _ = build_job_run.env_var_console_url

        build_job_run = BuildJobRun.from_arn(ArnEnum.batch_build)
        assert build_job_run.is_batch is True
        assert build_job_run.aws_account_id == "111122223333"
        assert build_job_run.aws_region == "us-east-1"
        assert build_job_run.project_name == "my-project"
        assert build_job_run.run_id == "1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        assert build_job_run.arn == ArnEnum.batch_build
        assert build_job_run.run_uuid == "my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"

        assert build_job_run.aws_account_id == "111122223333"
        assert build_job_run.aws_region == "us-east-1"
        assert build_job_run.project_name == "my-project"
        assert build_job_run.run_id == "1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f"
        assert (
            build_job_run.console_url
            == "https://us-east-1.console.aws.amazon.com/codesuite/codebuild/111122223333/projects/my-project/batch/my-project:1a2b3c4d-1234-abcd-1234-1a2b3c4d5e6f/?region=us-east-1"
        )
        _ = build_job_run.phase_console_url
        _ = build_job_run.env_var_console_url

    def test_from_start_build_response(self):
        start_build_response = {
            "build": {
                "id": "string",
                "arn": ArnEnum.build,
                "buildNumber": 123,
            }
        }
        build_job_run = BuildJobRun.from_start_build_response(start_build_response)
        assert build_job_run.build_number == 123

        start_build_batch_response = {
            "buildBatch": {
                "id": "string",
                "arn": ArnEnum.batch_build,
                "buildBatchNumber": 456,
            }
        }
        build_job_run = BuildJobRun.from_start_build_response(
            start_build_batch_response
        )
        assert build_job_run.build_number == 456


if __name__ == "__main__":
    from aws_codebuild.tests import run_cov_test

    run_cov_test(__file__, "aws_codebuild.arn_and_console", preview=False)
