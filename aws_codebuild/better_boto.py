# -*- coding: utf-8 -*-

"""
Improved boto3 codebuild API.

Reference:

- https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html
"""

import typing as T

from boto_session_manager import BotoSesManager
from .arg import NOTHING, resolve_kwargs


def start_build(
    bsm: BotoSesManager,
    projectName: str,
    secondarySourcesOverride: T.Optional[dict] = NOTHING,
    secondarySourcesVersionOverride: T.Optional[dict] = NOTHING,
    sourceVersion: T.Optional[str] = NOTHING,
    artifactsOverride: T.Optional[dict] = NOTHING,
    secondaryArtifactsOverride: T.Optional[dict] = NOTHING,
    environmentVariablesOverride: T.Optional[T.List[T.Dict[str, str]]] = NOTHING,
    sourceTypeOverride: T.Optional[str] = NOTHING,
    sourceLocationOverride: T.Optional[str] = NOTHING,
    sourceAuthOverride: T.Optional[dict] = NOTHING,
    gitCloneDepthOverride: T.Optional[int] = NOTHING,
    gitSubmodulesConfigOverride: T.Optional[dict] = NOTHING,
    buildspecOverride: T.Optional[str] = NOTHING,
    insecureSslOverride: T.Optional[bool] = NOTHING,
    reportBuildStatusOverride: T.Optional[bool] = NOTHING,
    buildStatusConfigOverride: T.Optional[dict] = NOTHING,
    environmentTypeOverride: T.Optional[str] = NOTHING,
    imageOverride: T.Optional[str] = NOTHING,
    computeTypeOverride: T.Optional[str] = NOTHING,
    certificateOverride: T.Optional[str] = NOTHING,
    cacheOverride: T.Optional[dict] = NOTHING,
    serviceRoleOverride: T.Optional[str] = NOTHING,
    privilegedModeOverride: T.Optional[bool] = NOTHING,
    timeoutInMinutesOverride: T.Optional[int] = NOTHING,
    queuedTimeoutInMinutesOverride: T.Optional[int] = NOTHING,
    encryptionKeyOverride: T.Optional[str] = NOTHING,
    idempotencyToken: T.Optional[str] = NOTHING,
    logsConfigOverride: T.Optional[dict] = NOTHING,
    registryCredentialOverride: T.Optional[dict] = NOTHING,
    imagePullCredentialsTypeOverride: T.Optional[str] = NOTHING,
    debugSessionEnabled: T.Optional[bool] = NOTHING,
) -> dict:
    """
    Reference:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build

    .. versionadded:: 1.1.1
    """
    return bsm.codebuild_client.start_build(
        **resolve_kwargs(
            projectName=projectName,
            secondarySourcesOverride=secondarySourcesOverride,
            secondarySourcesVersionOverride=secondarySourcesVersionOverride,
            sourceVersion=sourceVersion,
            artifactsOverride=artifactsOverride,
            secondaryArtifactsOverride=secondaryArtifactsOverride,
            environmentVariablesOverride=environmentVariablesOverride,
            sourceTypeOverride=sourceTypeOverride,
            sourceLocationOverride=sourceLocationOverride,
            sourceAuthOverride=sourceAuthOverride,
            gitCloneDepthOverride=gitCloneDepthOverride,
            gitSubmodulesConfigOverride=gitSubmodulesConfigOverride,
            buildspecOverride=buildspecOverride,
            insecureSslOverride=insecureSslOverride,
            reportBuildStatusOverride=reportBuildStatusOverride,
            buildStatusConfigOverride=buildStatusConfigOverride,
            environmentTypeOverride=environmentTypeOverride,
            imageOverride=imageOverride,
            computeTypeOverride=computeTypeOverride,
            certificateOverride=certificateOverride,
            cacheOverride=cacheOverride,
            serviceRoleOverride=serviceRoleOverride,
            privilegedModeOverride=privilegedModeOverride,
            timeoutInMinutesOverride=timeoutInMinutesOverride,
            queuedTimeoutInMinutesOverride=queuedTimeoutInMinutesOverride,
            encryptionKeyOverride=encryptionKeyOverride,
            idempotencyToken=idempotencyToken,
            logsConfigOverride=logsConfigOverride,
            registryCredentialOverride=registryCredentialOverride,
            imagePullCredentialsTypeOverride=imagePullCredentialsTypeOverride,
            debugSessionEnabled=debugSessionEnabled,
        )
    )


def start_build_batch(
    bsm: BotoSesManager,
    projectName: str,
    secondarySourcesOverride: T.Optional[dict] = NOTHING,
    secondarySourcesVersionOverride: T.Optional[dict] = NOTHING,
    sourceVersion: T.Optional[str] = NOTHING,
    artifactsOverride: T.Optional[dict] = NOTHING,
    secondaryArtifactsOverride: T.Optional[dict] = NOTHING,
    environmentVariablesOverride: T.Optional[T.List[T.Dict[str, str]]] = NOTHING,
    sourceTypeOverride: T.Optional[str] = NOTHING,
    sourceLocationOverride: T.Optional[str] = NOTHING,
    sourceAuthOverride: T.Optional[dict] = NOTHING,
    gitCloneDepthOverride: T.Optional[int] = NOTHING,
    gitSubmodulesConfigOverride: T.Optional[dict] = NOTHING,
    buildspecOverride: T.Optional[str] = NOTHING,
    insecureSslOverride: T.Optional[bool] = NOTHING,
    reportBuildStatusOverride: T.Optional[bool] = NOTHING,
    environmentTypeOverride: T.Optional[str] = NOTHING,
    imageOverride: T.Optional[str] = NOTHING,
    computeTypeOverride: T.Optional[str] = NOTHING,
    certificateOverride: T.Optional[str] = NOTHING,
    cacheOverride: T.Optional[dict] = NOTHING,
    serviceRoleOverride: T.Optional[str] = NOTHING,
    privilegedModeOverride: T.Optional[bool] = NOTHING,
    buildTimeoutInMinutesOverride: T.Optional[int] = NOTHING,
    queuedTimeoutInMinutesOverride: T.Optional[int] = NOTHING,
    encryptionKeyOverride: T.Optional[str] = NOTHING,
    idempotencyToken: T.Optional[str] = NOTHING,
    logsConfigOverride: T.Optional[dict] = NOTHING,
    registryCredentialOverride: T.Optional[dict] = NOTHING,
    imagePullCredentialsTypeOverride: T.Optional[str] = NOTHING,
    buildBatchConfigOverride: T.Optional[dict] = NOTHING,
    debugSessionEnabled: T.Optional[bool] = NOTHING,
) -> dict:
    """
    Reference:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build_batch

    .. versionadded:: 1.1.1
    """
    return bsm.codebuild_client.start_build_batch(
        **resolve_kwargs(
            projectName=projectName,
            secondarySourcesOverride=secondarySourcesOverride,
            secondarySourcesVersionOverride=secondarySourcesVersionOverride,
            sourceVersion=sourceVersion,
            artifactsOverride=artifactsOverride,
            secondaryArtifactsOverride=secondaryArtifactsOverride,
            environmentVariablesOverride=environmentVariablesOverride,
            sourceTypeOverride=sourceTypeOverride,
            sourceLocationOverride=sourceLocationOverride,
            sourceAuthOverride=sourceAuthOverride,
            gitCloneDepthOverride=gitCloneDepthOverride,
            gitSubmodulesConfigOverride=gitSubmodulesConfigOverride,
            buildspecOverride=buildspecOverride,
            insecureSslOverride=insecureSslOverride,
            reportBuildStatusOverride=reportBuildStatusOverride,
            environmentTypeOverride=environmentTypeOverride,
            imageOverride=imageOverride,
            computeTypeOverride=computeTypeOverride,
            certificateOverride=certificateOverride,
            cacheOverride=cacheOverride,
            serviceRoleOverride=serviceRoleOverride,
            privilegedModeOverride=privilegedModeOverride,
            buildTimeoutInMinutesOverride=buildTimeoutInMinutesOverride,
            queuedTimeoutInMinutesOverride=queuedTimeoutInMinutesOverride,
            encryptionKeyOverride=encryptionKeyOverride,
            idempotencyToken=idempotencyToken,
            logsConfigOverride=logsConfigOverride,
            registryCredentialOverride=registryCredentialOverride,
            imagePullCredentialsTypeOverride=imagePullCredentialsTypeOverride,
            buildBatchConfigOverride=buildBatchConfigOverride,
            debugSessionEnabled=debugSessionEnabled,
        )
    )
