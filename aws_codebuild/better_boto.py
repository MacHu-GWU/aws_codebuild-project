# -*- coding: utf-8 -*-

import typing as T


def resolve_kwargs(**kwargs) -> dict:
    return {k: v for k, v in kwargs if v is not None}


def start_build(
    cb_client,
    projectName: str,
    secondarySourcesOverride: T.Optional[dict] = None,
    secondarySourcesVersionOverride: T.Optional[dict] = None,
    sourceVersion: T.Optional[str] = None,
    artifactsOverride: T.Optional[dict] = None,
    secondaryArtifactsOverride: T.Optional[dict] = None,
    environmentVariablesOverride: T.Optional[T.List[T.Dict[str, str]]] = None,
    sourceTypeOverride: T.Optional[str] = None,
    sourceLocationOverride: T.Optional[str] = None,
    sourceAuthOverride: T.Optional[dict] = None,
    gitCloneDepthOverride: T.Optional[int] = None,
    gitSubmodulesConfigOverride: T.Optional[dict] = None,
    buildspecOverride: T.Optional[str] = None,
    insecureSslOverride: T.Optional[bool] = None,
    reportBuildStatusOverride: T.Optional[bool] = None,
    buildStatusConfigOverride: T.Optional[dict] = None,
    environmentTypeOverride: T.Optional[str] = None,
    imageOverride: T.Optional[str] = None,
    computeTypeOverride: T.Optional[str] = None,
    certificateOverride: T.Optional[str] = None,
    cacheOverride: T.Optional[dict] = None,
    serviceRoleOverride: T.Optional[str] = None,
    privilegedModeOverride: T.Optional[bool] = None,
    timeoutInMinutesOverride: T.Optional[int] = None,
    queuedTimeoutInMinutesOverride: T.Optional[int] = None,
    encryptionKeyOverride: T.Optional[str] = None,
    idempotencyToken: T.Optional[str] = None,
    logsConfigOverride: T.Optional[dict] = None,
    registryCredentialOverride: T.Optional[dict] = None,
    imagePullCredentialsTypeOverride: T.Optional[str] = None,
    debugSessionEnabled: T.Optional[bool] = None,
) -> dict:
    """
    Reference:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build
    """
    return cb_client.start_build(
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
    cb_client,
    projectName: str,
    secondarySourcesOverride: T.Optional[dict] = None,
    secondarySourcesVersionOverride: T.Optional[dict] = None,
    sourceVersion: T.Optional[str] = None,
    artifactsOverride: T.Optional[dict] = None,
    secondaryArtifactsOverride: T.Optional[dict] = None,
    environmentVariablesOverride: T.Optional[T.List[T.Dict[str, str]]] = None,
    sourceTypeOverride: T.Optional[str] = None,
    sourceLocationOverride: T.Optional[str] = None,
    sourceAuthOverride: T.Optional[dict] = None,
    gitCloneDepthOverride: T.Optional[int] = None,
    gitSubmodulesConfigOverride: T.Optional[dict] = None,
    buildspecOverride: T.Optional[str] = None,
    insecureSslOverride: T.Optional[bool] = None,
    reportBuildStatusOverride: T.Optional[bool] = None,
    environmentTypeOverride: T.Optional[str] = None,
    imageOverride: T.Optional[str] = None,
    computeTypeOverride: T.Optional[str] = None,
    certificateOverride: T.Optional[str] = None,
    cacheOverride: T.Optional[dict] = None,
    serviceRoleOverride: T.Optional[str] = None,
    privilegedModeOverride: T.Optional[bool] = None,
    buildTimeoutInMinutesOverride: T.Optional[int] = None,
    queuedTimeoutInMinutesOverride: T.Optional[int] = None,
    encryptionKeyOverride: T.Optional[str] = None,
    idempotencyToken: T.Optional[str] = None,
    logsConfigOverride: T.Optional[dict] = None,
    registryCredentialOverride: T.Optional[dict] = None,
    imagePullCredentialsTypeOverride: T.Optional[str] = None,
    buildBatchConfigOverride: T.Optional[dict] = None,
    debugSessionEnabled: T.Optional[bool] = None,
) -> dict:
    """
    Reference:

    - https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/codebuild.html#CodeBuild.Client.start_build_batch
    """
    return cb_client.start_build_batch(
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
