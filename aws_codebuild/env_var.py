# -*- coding: utf-8 -*-

import os
import dataclasses


@dataclasses.dataclass
class BuiltinEnvVar:
    """
    Environment variables in build environments

    Reference:

    - https://docs.aws.amazon.com/codebuild/latest/userguide/build-env-ref-env-vars.html
    """

    AWS_DEFAULT_REGION: str = dataclasses.field()
    AWS_REGION: str = dataclasses.field()
    CODEBUILD_BATCH_BUILD_IDENTIFIER: str = dataclasses.field()
    CODEBUILD_BUILD_ARN: str = dataclasses.field()
    CODEBUILD_BUILD_ID: str = dataclasses.field()
    CODEBUILD_BUILD_IMAGE: str = dataclasses.field()
    CODEBUILD_BUILD_NUMBER: str = dataclasses.field()
    CODEBUILD_BUILD_SUCCEEDING: str = dataclasses.field()
    CODEBUILD_INITIATOR: str = dataclasses.field()
    CODEBUILD_KMS_KEY_ID: str = dataclasses.field()
    CODEBUILD_LOG_PATH: str = dataclasses.field()
    CODEBUILD_PUBLIC_BUILD_URL: str = dataclasses.field()
    CODEBUILD_RESOLVED_SOURCE_VERSION: str = dataclasses.field()
    CODEBUILD_SOURCE_REPO_URL: str = dataclasses.field()
    CODEBUILD_SOURCE_VERSION: str = dataclasses.field()
    CODEBUILD_SRC_DIR: str = dataclasses.field()
    CODEBUILD_START_TIME: str = dataclasses.field()
    CODEBUILD_WEBHOOK_ACTOR_ACCOUNT_ID: str = dataclasses.field()
    CODEBUILD_WEBHOOK_BASE_REF: str = dataclasses.field()
    CODEBUILD_WEBHOOK_EVENT: str = dataclasses.field()
    CODEBUILD_WEBHOOK_MERGE_COMMIT: str = dataclasses.field()
    CODEBUILD_WEBHOOK_PREV_COMMIT: str = dataclasses.field()
    CODEBUILD_WEBHOOK_HEAD_REF: str = dataclasses.field()
    CODEBUILD_WEBHOOK_TRIGGER: str = dataclasses.field()
    HOME: str = dataclasses.field()

    @classmethod
    def from_env_var(cls) -> "BuiltinEnvVar":
        kwargs = {os.environ.get(field.name, "") for field in dataclasses.fields(cls)}
        return cls(**kwargs)
