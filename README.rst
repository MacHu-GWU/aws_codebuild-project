
.. image:: https://readthedocs.org/projects/aws_codebuild/badge/?version=latest
    :target: https://aws_codebuild.readthedocs.io/index.html
    :alt: Documentation Status

.. image:: https://github.com/MacHu-GWU/aws_codebuild-project/workflows/CI/badge.svg
    :target: https://github.com/MacHu-GWU/aws_codebuild-project/actions?query=workflow:CI

.. image:: https://codecov.io/gh/MacHu-GWU/aws_codebuild-project/branch/main/graph/badge.svg
    :target: https://codecov.io/gh/MacHu-GWU/aws_codebuild-project

.. image:: https://img.shields.io/pypi/v/aws_codebuild.svg
    :target: https://pypi.python.org/pypi/aws_codebuild

.. image:: https://img.shields.io/pypi/l/aws_codebuild.svg
    :target: https://pypi.python.org/pypi/aws_codebuild

.. image:: https://img.shields.io/pypi/pyversions/aws_codebuild.svg
    :target: https://pypi.python.org/pypi/aws_codebuild

.. image:: https://img.shields.io/badge/STAR_Me_on_GitHub!--None.svg?style=social
    :target: https://github.com/MacHu-GWU/aws_codebuild-project

------


.. image:: https://img.shields.io/badge/Link-Document-blue.svg
    :target: https://aws_codebuild.readthedocs.io/index.html

.. image:: https://img.shields.io/badge/Link-API-blue.svg
    :target: https://aws_codebuild.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Source_Code-blue.svg
    :target: https://aws_codebuild.readthedocs.io/py-modindex.html

.. image:: https://img.shields.io/badge/Link-Install-blue.svg
    :target: `install`_

.. image:: https://img.shields.io/badge/Link-GitHub-blue.svg
    :target: https://github.com/MacHu-GWU/aws_codebuild-project

.. image:: https://img.shields.io/badge/Link-Submit_Issue-blue.svg
    :target: https://github.com/MacHu-GWU/aws_codebuild-project/issues

.. image:: https://img.shields.io/badge/Link-Request_Feature-blue.svg
    :target: https://github.com/MacHu-GWU/aws_codebuild-project/issues

.. image:: https://img.shields.io/badge/Link-Download-blue.svg
    :target: https://pypi.org/pypi/aws_codebuild#files


Welcome to ``aws_codebuild`` Documentation
==============================================================================
**Feature**:

- ``aws_codebuild.CodeBuildEventTypeEnum``: codebuild trigger event type enumeration
- ``aws_codebuild.CodeBuildEvent``: codebuild trigger event data class
- ``aws_codebuild.BuildJobRun``: build job run data class
- ``aws_codebuild.start_build``: better boto3 start_build API
- ``aws_codebuild.start_build_batch``: better boto3 start_build_batch API
- ``aws_codebuild.BuiltinEnvVar``: built in build job run environment variable accessor


.. _install:

Install
------------------------------------------------------------------------------

``aws_codebuild`` is released on PyPI, so all you need is:

.. code-block:: console

    $ pip install aws_codebuild

To upgrade to latest version:

.. code-block:: console

    $ pip install --upgrade aws_codebuild