# -*- coding: utf-8 -*-

"""
Codebuild ARN and Console related.
"""

import typing as T
import dataclasses


@dataclasses.dataclass
class BuildJobRun:
    """
    For example, if the build arn is:
    "arn:aws:codebuild:us-east-1:111122223333:build/my-project:ae6a271b-609e-4e76-b6bb-3bac681edd05"

    Then:

    - aws_account_id: "111122223333"
    - aws_region: "us-east-1"
    - project_name: "my-project"
    - run_id: "ae6a271b-609e-4e76-b6bb-3bac681edd05"
    - run_uuid: "my-project:ae6a271b-609e-4e76-b6bb-3bac681edd05"

    .. versionadded:: 1.1.1
    """
    is_batch: bool = dataclasses.field()
    aws_account_id: str = dataclasses.field()
    aws_region: str = dataclasses.field()
    project_name: str = dataclasses.field()
    run_id: str = dataclasses.field()
    build_number: T.Optional[int] = dataclasses.field(default=None)

    @classmethod
    def from_arn(cls, arn: str) -> "BuildJobRun":
        part1, part2 = arn.split("/")
        part1_chunks = part1.split(":")
        part2_chunks = part2.split(":")
        is_batch = part1_chunks[5] == "build-batch"
        return cls(
            is_batch=is_batch,
            aws_account_id=part1_chunks[4],
            aws_region=part1_chunks[3],
            project_name=part2_chunks[0],
            run_id=part2_chunks[1],
        )

    @property
    def _arn_template(self) -> str:
        return (
            f"arn:aws:codebuild:{self.aws_region}:{self.aws_account_id}:{{type}}/"
            f"{self.project_name}:{self.run_id}"
        )

    @property
    def arn(self) -> str:
        """
        .. versionadded:: 1.1.1
        """
        if self.is_batch:
            return self._arn_template.format(type="build-batch")
        else:
            return self._arn_template.format(type="build")

    # @classmethod
    # def from_console_url(cls, console_url) -> "BuildJobRun":
    #     parts = console_url.split("/")
    #     return cls(
    #         aws_account_id=parts[5],
    #         aws_region=parts[2].split(".")[0],
    #         project_name=parts[7],
    #         run_id=parts[9][-36:],
    #     )

    @property
    def _console_url_template_1(self) -> str:
        return (
            f"https://{self.aws_region}.console.aws.amazon.com/codesuite/codebuild/"
            f"{self.aws_account_id}/projects/{self.project_name}/{{type}}/"
            f"{self.project_name}:{self.run_id}/{{tab}}?region={self.aws_region}"
        )

    @property
    def _console_url_template_2(self) -> str:
        if self.is_batch:
            return self._console_url_template_1.format(type="batch", tab="{tab}")
        else:
            return self._console_url_template_1.format(type="build", tab="{tab}")

    @property
    def console_url(self) -> str:
        """
        .. versionadded:: 1.1.1
        """
        return self._console_url_template_2.format(tab="")

    @property
    def phase_console_url(self) -> str:
        """
        .. versionadded:: 1.1.1
        """
        return self._console_url_template_2.format(tab="phase")

    @property
    def env_var_console_url(self) -> str:
        """
        .. versionadded:: 1.1.1
        """
        return self._console_url_template_2.format(tab="env_var")

    @classmethod
    def from_start_build_response(cls, res: dict) -> "BuildJobRun":
        """
        Reference:

        - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build
        - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build_batch

        :param res:
        :return:

        .. versionadded:: 1.1.1
        """
        if "build" in res:
            data = res["build"]
            build_number = data["buildNumber"]
        elif "buildBatch" in res:
            data = res["buildBatch"]
            build_number = data["buildBatchNumber"]
        else:  # pragma: no cover
            raise NotImplementedError
        build_job_run = BuildJobRun.from_arn(data["arn"])
        build_job_run.build_number = build_number
        return build_job_run

    @property
    def run_uuid(self) -> str:
        """
        .. versionadded:: 1.1.1
        """
        return f"{self.project_name}:{self.run_id}"