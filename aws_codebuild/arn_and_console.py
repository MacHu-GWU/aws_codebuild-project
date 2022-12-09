# -*- coding: utf-8 -*-

import dataclasses


@dataclasses.dataclass
class BuildJobRun:
    aws_account_id: str = dataclasses.field()
    aws_region: str = dataclasses.field()
    project_name: str = dataclasses.field()
    run_id: str = dataclasses.field()

    @classmethod
    def from_arn(cls, arn: str) -> "BuildJobRun":
        part1, part2 = arn.split("/")
        part1_chunks = part1.split(":")
        part2_chunks = part2.split(":")
        return cls(
            aws_account_id=part1_chunks[4],
            aws_region=part1_chunks[3],
            project_name=part2_chunks[0],
            run_id=part2_chunks[1],
        )

    @property
    def arn(self) -> str:
        return (
            f"arn:aws:codebuild:{self.aws_region}:{self.aws_account_id}:build/"
            f"{self.project_name}:{self.run_id}"
        )

    @classmethod
    def from_console_url(cls, console_url) -> "BuildJobRun":
        parts = console_url.split("/")
        return cls(
            aws_account_id=parts[5],
            aws_region=parts[2].split(".")[0],
            project_name=parts[7],
            run_id=parts[9][-36:],
        )

    @property
    def console_url(self) -> str:
        return (
            f"https://{self.aws_region}.console.aws.amazon.com/codesuite/codebuild/"
            f"{self.aws_account_id}/projects/{self.project_name}/build/"
            f"{self.project_name}:{self.run_id}/?region={self.aws_region}"
        )
