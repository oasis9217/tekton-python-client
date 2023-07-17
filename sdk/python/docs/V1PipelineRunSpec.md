# V1PipelineRunSpec

PipelineRunSpec defines the desired state of PipelineRun
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**list[V1Param]**](V1Param.md) | Params is a list of parameter names and values. | [optional] 
**pipeline_ref** | [**V1PipelineRef**](V1PipelineRef.md) |  | [optional] 
**pipeline_spec** | [**V1PipelineSpec**](V1PipelineSpec.md) |  | [optional] 
**status** | **str** | Used for cancelling a pipelinerun (and maybe more later on) | [optional] 
**task_run_specs** | [**list[V1PipelineTaskRunSpec]**](V1PipelineTaskRunSpec.md) | TaskRunSpecs holds a set of runtime specs | [optional] 
**task_run_template** | [**V1PipelineTaskRunTemplate**](V1PipelineTaskRunTemplate.md) |  | [optional] 
**timeouts** | [**V1TimeoutFields**](V1TimeoutFields.md) |  | [optional] 
**workspaces** | [**list[V1WorkspaceBinding]**](V1WorkspaceBinding.md) | Workspaces holds a set of workspace bindings that must match names with those declared in the pipeline. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


