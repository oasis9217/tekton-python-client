# V1TaskSpec

TaskSpec defines the desired state of Task.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description is a user-facing description of the task that may be used to populate a UI. | [optional] 
**display_name** | **str** | DisplayName is a user-facing name of the task that may be used to populate a UI. | [optional] 
**params** | [**list[V1ParamSpec]**](V1ParamSpec.md) | Params is a list of input parameters required to run the task. Params must be supplied as inputs in TaskRuns unless they declare a default value. | [optional] 
**results** | [**list[V1TaskResult]**](V1TaskResult.md) | Results are values that this Task can output | [optional] 
**sidecars** | [**list[V1Sidecar]**](V1Sidecar.md) | Sidecars are run alongside the Task&#39;s step containers. They begin before the steps start and end after the steps complete. | [optional] 
**step_template** | [**V1StepTemplate**](V1StepTemplate.md) |  | [optional] 
**steps** | [**list[V1Step]**](V1Step.md) | Steps are the steps of the build; each step is run sequentially with the source mounted into /workspace. | [optional] 
**volumes** | [**list[V1Volume]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Volume.md) | Volumes is a collection of volumes that are available to mount into the steps of the build. | [optional] 
**workspaces** | [**list[V1WorkspaceDeclaration]**](V1WorkspaceDeclaration.md) | Workspaces are the volumes that this Task requires. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


