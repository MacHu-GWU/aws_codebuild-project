# -*- coding: utf-8 -*-

"""
This module implements the Data Model for the CodeBuild notification event.
"""

import typing as T
import enum
import dataclasses
from datetime import datetime

from boto_session_manager import BotoSesManager

from .arn_and_console import BuildJobRun


class CodeBuildEventTypeEnum(str, enum.Enum):
    state_change = "CodeBuild Build State Change"
    phase_change = "CodeBuild Build Phase Change"


class BuildStatusEnum(str, enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"


class PhaseEnum(str, enum.Enum):
    INITIALIZED = "INITIALIZED"
    SUBMITTED = "SUBMITTED"
    QUEUED = "QUEUED"
    PROVISIONING = "PROVISIONING"
    DOWNLOAD_SOURCE = "DOWNLOAD_SOURCE"
    INSTALL = "INSTALL"
    PRE_BUILD = "PRE_BUILD"
    BUILD = "BUILD"
    POST_BUILD = "POST_BUILD"
    UPLOAD_ARTIFACTS = "UPLOAD_ARTIFACTS"
    FINALIZING = "FINALIZING"
    COMPLETED = "COMPLETED"


DATETIME_FORMAT = "%b %d, %Y %I:%M:%S %p"


@dataclasses.dataclass
class CodeBuildEvent:
    """
    Data container class to represent a CodeBuild notification event.

    See example at `Build notifications sample for CodeBuild <https://docs.aws.amazon.com/codebuild/latest/userguide/sample-build-notifications.html>`_

    :param data: the original CodeBuild notification event data. you can access
        important attributes via property method
    :param bsm: optional boto session manager object.

    .. versionadded:: 1.1.1

    [中文] Developer note:

    把一个外部传进来的 dict data 变成一个 dataclass, 这种工作我们一般有以下几种办法来做:

    1. 精心设计这个 dataclass 的属性. 在初始化对象的时候就把这些属性的值从 data 中提取出来.
        这样做的好处是可以用 ``dataclasses.asdict`` 的方法将其转化成 dict 容器. 坏处是你
        需要设计一个很复杂的工厂函数, 里面的逻辑糅合在了一起, 比较难以一次性实现正确.
    2. 只给这个 dataclass 一个叫做 data 的属性, 用来储存原始的 data. 然后把每一个你要用到
        的属性写成 ``@property`` method. 这样的好处是所有的属性的逻辑都解耦了, 还能有一定
        的复用, 但是你就无法使用 ``dataclasses.asdict`` 的方法了.

    我选择的是结合上面的两种方法, 为每个属性设计一个工厂函数, 而最终也为这个属性定义一个
    ``dataclasses.field()``, 两种方法的优点都吸取了, 代价就是要写的代码比较多.
    """

    _data: dict = dataclasses.field()

    aws_account_id: str = dataclasses.field()
    aws_region: str = dataclasses.field()
    event_version: str = dataclasses.field()
    event_time: str = dataclasses.field()
    event_type: str = dataclasses.field()
    project_name: str = dataclasses.field()
    build_arn: str = dataclasses.field()
    initiator: str = dataclasses.field()
    build_start_time: str = dataclasses.field()
    timeout_in_minutes: int = dataclasses.field()
    build_complete: bool = dataclasses.field()
    source_location: str = dataclasses.field()
    source_type: str = dataclasses.field()
    source_version: str = dataclasses.field()
    env_vars: T.List[T.Dict[str, str]] = dataclasses.field(default_factory=list)
    phases: T.List[T.Dict[str, T.Any]] = dataclasses.field(default_factory=list)
    build_number: T.Optional[int] = dataclasses.field(default=None)
    build_status: T.Optional[str] = dataclasses.field(default=None)
    complete_phase: T.Optional[str] = dataclasses.field(default=None)
    complete_phase_context: T.Optional[str] = dataclasses.field(default=None)
    complete_phase_status: T.Optional[str] = dataclasses.field(default=None)
    complete_phase_duration_seconds: T.Optional[int] = dataclasses.field(default=None)
    complete_phase_start: T.Optional[str] = dataclasses.field(default=None)
    complete_phase_end: T.Optional[str] = dataclasses.field(default=None)

    bsm: T.Optional[BotoSesManager] = dataclasses.field(default=None)

    @classmethod
    def from_codebuid_notification_event(cls, event: dict) -> "CodeBuildEvent":
        """
        Make object from CodeBuild notification event.
        :param event:
        :return:
        """
        return cls(
            _data=event,
            aws_account_id=cls._get_aws_account_id(event),
            aws_region=cls._get_aws_region(event),
            event_version=cls._get_event_version(event),
            event_time=cls._get_event_time(event),
            event_type=cls._get_event_type(event),
            project_name=cls._get_project_name(event),
            build_arn=cls._get_build_arn(event),
            initiator=cls._get_initiator(event),
            build_start_time=cls._get_build_start_time(event),
            timeout_in_minutes=cls._get_timeout_in_minutes(event),
            build_complete=cls._get_build_complete(event),
            source_location=cls._get_source_location(event),
            source_type=cls._get_source_type(event),
            source_version=cls._get_source_version(event),
            env_vars=cls._get_env_vars(event),
            phases=cls._get_phases(event),
            build_number=cls._get_build_number(event),
            build_status=cls._get_build_status(event),
            complete_phase=cls._get_complete_phase(event),
            complete_phase_context=cls._get_complete_phase_context(event),
            complete_phase_status=cls._get_complete_phase_status(event),
            complete_phase_duration_seconds=cls._get_complete_phase_duration_seconds(
                event
            ),
            complete_phase_start=cls._get_complete_phase_start(event),
            complete_phase_end=cls._get_complete_phase_end(event),
        )

    # --------------------------------------------------------------------------
    # attribute value extractor
    # --------------------------------------------------------------------------
    @classmethod
    def _get_aws_account_id(cls, data: dict) -> str:
        return data["account"]

    @classmethod
    def _get_aws_region(cls, data: dict) -> str:
        return data["region"]

    @classmethod
    def _get_event_version(cls, data: dict) -> str:
        return data["detail"]["version"]

    @classmethod
    def _get_event_time(cls, data: dict) -> str:
        return data["time"]

    @classmethod
    def _get_event_type(cls, data: dict) -> str:
        return data["detailType"]

    @classmethod
    def _get_project_name(cls, data: dict) -> str:
        return data["detail"]["project-name"]

    @classmethod
    def _get_build_arn(cls, data: dict) -> str:
        return data["detail"]["build-id"]

    @classmethod
    def _get_initiator(cls, data: dict) -> str:
        return data["detail"]["additional-information"]["initiator"]

    @classmethod
    def _get_build_start_time(cls, data: dict) -> str:
        return data["detail"]["additional-information"]["build-start-time"]

    @classmethod
    def _get_timeout_in_minutes(cls, data: dict) -> int:
        return data["detail"]["additional-information"]["timeout-in-minutes"]

    @classmethod
    def _get_build_complete(cls, data: dict) -> bool:
        return data["detail"]["additional-information"]["build-complete"]

    @classmethod
    def _get_source_location(cls, data: dict) -> str:
        return data["detail"]["additional-information"]["source"]["location"]

    @classmethod
    def _get_source_type(cls, data: dict) -> str:
        return data["detail"]["additional-information"]["source"]["type"]

    @classmethod
    def _get_source_version(cls, data: dict) -> str:
        return data["detail"]["additional-information"]["source-version"]

    @classmethod
    def _get_env_vars(cls, data: dict) -> T.List[T.Dict[str, str]]:
        return data["detail"]["additional-information"]["environment"].get(
            "environment-variables", []
        )

    @classmethod
    def _get_phases(cls, data: dict) -> T.List[T.Dict[str, T.Any]]:
        return data["detail"]["additional-information"].get("phases", [])

    @classmethod
    def _get_build_number(cls, data: dict) -> T.Optional[int]:
        try:
            return int(data["detail"]["additional-information"].get("build-number"))
        except:
            return None

    # State Change Related
    @classmethod
    def _get_build_status(cls, data: dict) -> T.Optional[str]:
        return data["detail"].get("build-status")

    # Phase Change Related
    @classmethod
    def _get_complete_phase(cls, data: dict) -> T.Optional[str]:
        return data["detail"].get("completed-phase")

    @classmethod
    def _get_complete_phase_context(cls, data: dict) -> T.Optional[str]:
        return data["detail"].get("completed-phase-context")

    @classmethod
    def _get_complete_phase_status(cls, data: dict) -> T.Optional[str]:
        return data["detail"].get("completed-phase-status")

    @classmethod
    def _get_complete_phase_duration_seconds(cls, data: dict) -> T.Optional[int]:
        return data["detail"].get("completed-phase-duration-seconds")

    @classmethod
    def _get_complete_phase_start(cls, data: dict) -> T.Optional[str]:
        return data["detail"].get("completed-phase-start")

    @classmethod
    def _get_complete_phase_end(cls, data: dict) -> T.Optional[str]:
        return data["detail"].get("completed-phase-end")

    # --------------------------------------------------------------------------
    # Derived value
    # --------------------------------------------------------------------------
    @property
    def console_url(self) -> str:
        return BuildJobRun.from_arn(self.build_arn).console_url

    @property
    def plain_text_env_var(self) -> dict:
        return {
            dct["name"]: dct["value"]
            for dct in self.env_vars
            if dct["type"] == "PLAINTEXT"
        }

    @property
    def build_start_datetime(self) -> datetime:
        return datetime.strptime(self.build_start_time, DATETIME_FORMAT)

    @property
    def complete_phase_start_datetime(self) -> T.Optional[datetime]:
        if self.complete_phase_start is None:
            return None
        else:
            return datetime.strptime(self.complete_phase_start, DATETIME_FORMAT)

    @property
    def complete_phase_end_datetime(self) -> T.Optional[datetime]:
        if self.complete_phase_start is None:
            return None
        else:
            return datetime.strptime(self.complete_phase_end, DATETIME_FORMAT)

    # --------------------------------------------------------------------------
    # Test functions
    # --------------------------------------------------------------------------
    def is_state_change_event(self) -> bool:
        return self.event_type == CodeBuildEventTypeEnum.state_change

    def is_phase_change_event(self) -> bool:
        return self.event_type == CodeBuildEventTypeEnum.phase_change

    def is_build_status_IN_PROGRESS(self) -> bool:
        return self.build_status == BuildStatusEnum.IN_PROGRESS

    def is_build_status_FAILED(self) -> bool:
        return self.build_status == BuildStatusEnum.FAILED

    def is_build_status_SUCCEEDED(self) -> bool:
        return self.build_status == BuildStatusEnum.SUCCEEDED

    def is_complete_phase_INITIALIZED(self) -> bool:
        return self.complete_phase == PhaseEnum.INITIALIZED

    def is_complete_phase_SUBMITTED(self) -> bool:
        return self.complete_phase == PhaseEnum.SUBMITTED

    def is_complete_phase_PROVISIONING(self) -> bool:
        return self.complete_phase == PhaseEnum.PROVISIONING

    def is_complete_phase_DOWNLOAD_SOURCE(self) -> bool:
        return self.complete_phase == PhaseEnum.DOWNLOAD_SOURCE

    def is_complete_phase_INSTALL(self) -> bool:
        return self.complete_phase == PhaseEnum.INSTALL

    def is_complete_phase_PRE_BUILD(self) -> bool:
        return self.complete_phase == PhaseEnum.PRE_BUILD

    def is_complete_phase_POST_BUILD(self) -> bool:
        return self.complete_phase == PhaseEnum.POST_BUILD

    def is_complete_phase_UPLOAD_ARTIFACTS(self) -> bool:
        return self.complete_phase == PhaseEnum.UPLOAD_ARTIFACTS

    def is_complete_phase_FINALIZING(self) -> bool:
        return self.complete_phase == PhaseEnum.FINALIZING

    def is_complete_phase_COMPLETED(self) -> bool:
        return self.complete_phase == PhaseEnum.COMPLETED

    def is_complete_phase_status_IN_PROGRESS(self) -> bool:
        return self.complete_phase_status == BuildStatusEnum.IN_PROGRESS

    def is_complete_phase_status_FAILED(self) -> bool:
        return self.complete_phase_status == BuildStatusEnum.FAILED

    def is_complete_phase_status_SUCCEEDED(self) -> bool:
        return self.complete_phase_status == BuildStatusEnum.SUCCEEDED
