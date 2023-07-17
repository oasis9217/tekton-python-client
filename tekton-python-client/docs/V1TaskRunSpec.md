# V1TaskRunSpec

TaskRunSpec defines the desired state of TaskRun
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_resources** | [**V1ResourceRequirements**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ResourceRequirements.md) |  | [optional] 
**debug** | [**V1TaskRunDebug**](V1TaskRunDebug.md) |  | [optional] 
**params** | [**list[V1Param]**](V1Param.md) |  | [optional] 
**pod_template** | [**PodTemplate**](PodTemplate.md) |  | [optional] 
**retries** | **int** | Retries represents how many times this TaskRun should be retried in the event of task failure. | [optional] 
**service_account_name** | **str** |  | [optional] [default to '']
**sidecar_specs** | [**list[V1TaskRunSidecarSpec]**](V1TaskRunSidecarSpec.md) | Specs to apply to Sidecars in this TaskRun. If a field is specified in both a Sidecar and a SidecarSpec, the value from the SidecarSpec will be used. This field is only supported when the alpha feature gate is enabled. | [optional] 
**status** | **str** | Used for cancelling a TaskRun (and maybe more later on) | [optional] 
**status_message** | **str** | Status message for cancellation. | [optional] 
**step_specs** | [**list[V1TaskRunStepSpec]**](V1TaskRunStepSpec.md) | Specs to apply to Steps in this TaskRun. If a field is specified in both a Step and a StepSpec, the value from the StepSpec will be used. This field is only supported when the alpha feature gate is enabled. | [optional] 
**task_ref** | [**V1TaskRef**](V1TaskRef.md) |  | [optional] 
**task_spec** | [**V1TaskSpec**](V1TaskSpec.md) |  | [optional] 
**timeout** | [**V1Duration**](V1Duration.md) |  | [optional] 
**workspaces** | [**list[V1WorkspaceBinding]**](V1WorkspaceBinding.md) | Workspaces is a list of WorkspaceBindings from volumes to workspaces. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


