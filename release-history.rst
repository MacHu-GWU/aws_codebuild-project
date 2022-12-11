.. _release_history:

Release and Version History
==============================================================================


Backlog
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

**Minor Improvements**

**Bugfixes**

**Miscellaneous**


1.2.1 (2022-12-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- Add the following public API:
    - ``aws_codebuild.BuildStatusEnum``
    - ``aws_codebuild.CompletePhaseStatusEnum``
    - ``aws_codebuild.PhaseEnum``

**Miscellaneous**

- add ``versionadded`` doc.


1.1.1 (2022-12-11)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- First API stable version
- Add the following public API:
    - ``aws_codebuild.BuildJobRun``
    - ``aws_codebuild.start_build``
    - ``aws_codebuild.start_build_batch``
    - ``aws_codebuild.BuiltinEnvVar``
    - ``aws_codebuild.CodeBuildEventTypeEnum``
    - ``aws_codebuild.CodeBuildEvent``


0.2.2 (2022-12-10)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Bugfixes**

- fix kwargs resolver


0.2.1 (2022-12-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add :meth:`aws_codebuld.arn_and_console.BuildJobRun.from_start_build_response` method


0.1.1 (2022-12-09)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add build job run console and arn module
- add build job run built-in env var module
- add better boto module


0.0.1 (2022-07-24)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
**Features and Improvements**

- add AWS CodeBuild notification event data model
