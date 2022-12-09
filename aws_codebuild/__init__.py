# -*- coding: utf-8 -*-

"""
empower AWS CodeBuild.
"""


from ._version import __version__

__short_description__ = "empower AWS CodeBuild."
__license__ = "MIT"
__author__ = "Sanhe Hu"
__author_email__ = "husanhe@gmail.com"
__github_username__ = "MacHu-GWU"

try:
    from .arn_and_console import BuildJobRun
    from .better_boto import (
        start_build,
        start_build_batch,
    )
    from .env_var import BuiltinEnvVar
    from .notification import CodeBuildEventTypeEnum, CodeBuildEvent
except ImportError as e:  # pragma: no cover
    pass
