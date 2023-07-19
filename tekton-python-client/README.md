# tekton_pipeline
Tekton Pipeline

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v0.49.0
- Package version: 0.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import tekton_pipeline
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tekton_pipeline
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function

import time
import tekton_pipeline
from tekton_pipeline.rest import ApiException
from pprint import pprint

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------


## Documentation For Models

 - [PodAffinityAssistantTemplate](docs/PodAffinityAssistantTemplate.md)
 - [PodTemplate](docs/PodTemplate.md)
 - [V1ChildStatusReference](docs/V1ChildStatusReference.md)
 - [V1EmbeddedTask](docs/V1EmbeddedTask.md)
 - [V1IncludeParams](docs/V1IncludeParams.md)
 - [V1Matrix](docs/V1Matrix.md)
 - [V1Param](docs/V1Param.md)
 - [V1ParamSpec](docs/V1ParamSpec.md)
 - [V1ParamValue](docs/V1ParamValue.md)
 - [V1Pipeline](docs/V1Pipeline.md)
 - [V1PipelineList](docs/V1PipelineList.md)
 - [V1PipelineRef](docs/V1PipelineRef.md)
 - [V1PipelineResult](docs/V1PipelineResult.md)
 - [V1PipelineRun](docs/V1PipelineRun.md)
 - [V1PipelineRunList](docs/V1PipelineRunList.md)
 - [V1PipelineRunResult](docs/V1PipelineRunResult.md)
 - [V1PipelineRunRunStatus](docs/V1PipelineRunRunStatus.md)
 - [V1PipelineRunSpec](docs/V1PipelineRunSpec.md)
 - [V1PipelineRunStatus](docs/V1PipelineRunStatus.md)
 - [V1PipelineRunStatusFields](docs/V1PipelineRunStatusFields.md)
 - [V1PipelineRunTaskRunStatus](docs/V1PipelineRunTaskRunStatus.md)
 - [V1PipelineSpec](docs/V1PipelineSpec.md)
 - [V1PipelineTask](docs/V1PipelineTask.md)
 - [V1PipelineTaskMetadata](docs/V1PipelineTaskMetadata.md)
 - [V1PipelineTaskParam](docs/V1PipelineTaskParam.md)
 - [V1PipelineTaskRun](docs/V1PipelineTaskRun.md)
 - [V1PipelineTaskRunSpec](docs/V1PipelineTaskRunSpec.md)
 - [V1PipelineTaskRunTemplate](docs/V1PipelineTaskRunTemplate.md)
 - [V1PipelineWorkspaceDeclaration](docs/V1PipelineWorkspaceDeclaration.md)
 - [V1PropertySpec](docs/V1PropertySpec.md)
 - [V1Provenance](docs/V1Provenance.md)
 - [V1RefSource](docs/V1RefSource.md)
 - [V1ResolverRef](docs/V1ResolverRef.md)
 - [V1ResultRef](docs/V1ResultRef.md)
 - [V1Sidecar](docs/V1Sidecar.md)
 - [V1SidecarState](docs/V1SidecarState.md)
 - [V1SkippedTask](docs/V1SkippedTask.md)
 - [V1Step](docs/V1Step.md)
 - [V1StepOutputConfig](docs/V1StepOutputConfig.md)
 - [V1StepState](docs/V1StepState.md)
 - [V1StepTemplate](docs/V1StepTemplate.md)
 - [V1Task](docs/V1Task.md)
 - [V1TaskList](docs/V1TaskList.md)
 - [V1TaskRef](docs/V1TaskRef.md)
 - [V1TaskResult](docs/V1TaskResult.md)
 - [V1TaskRun](docs/V1TaskRun.md)
 - [V1TaskRunDebug](docs/V1TaskRunDebug.md)
 - [V1TaskRunInputs](docs/V1TaskRunInputs.md)
 - [V1TaskRunList](docs/V1TaskRunList.md)
 - [V1TaskRunResult](docs/V1TaskRunResult.md)
 - [V1TaskRunSidecarSpec](docs/V1TaskRunSidecarSpec.md)
 - [V1TaskRunSpec](docs/V1TaskRunSpec.md)
 - [V1TaskRunStatus](docs/V1TaskRunStatus.md)
 - [V1TaskRunStatusFields](docs/V1TaskRunStatusFields.md)
 - [V1TaskRunStepSpec](docs/V1TaskRunStepSpec.md)
 - [V1TaskSpec](docs/V1TaskSpec.md)
 - [V1TimeoutFields](docs/V1TimeoutFields.md)
 - [V1WhenExpression](docs/V1WhenExpression.md)
 - [V1WorkspaceBinding](docs/V1WorkspaceBinding.md)
 - [V1WorkspaceDeclaration](docs/V1WorkspaceDeclaration.md)
 - [V1WorkspacePipelineTaskBinding](docs/V1WorkspacePipelineTaskBinding.md)
 - [V1WorkspaceUsage](docs/V1WorkspaceUsage.md)


## Documentation For Authorization

 All endpoints do not require authorization.

## Author


