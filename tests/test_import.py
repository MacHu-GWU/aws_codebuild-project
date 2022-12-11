# -*- coding: utf-8 -*-

import pytest
from pytest import raises, approx


def test():
    import aws_codebuild

    _ = aws_codebuild.BuildJobRun
    _ = aws_codebuild.start_build
    _ = aws_codebuild.start_build_batch
    _ = aws_codebuild.BuiltinEnvVar
    _ = aws_codebuild.CodeBuildEventTypeEnum
    _ = aws_codebuild.CodeBuildEvent
    _ = aws_codebuild.BuildStatusEnum
    _ = aws_codebuild.CompletePhaseStatusEnum
    _ = aws_codebuild.PhaseEnum


if __name__ == "__main__":
    import os

    basename = os.path.basename(__file__)
    pytest.main([basename, "-s", "--tb=native"])
