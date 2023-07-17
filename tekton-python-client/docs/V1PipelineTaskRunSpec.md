# V1PipelineTaskRunSpec

PipelineTaskRunSpec  can be used to configure specific specs for a concrete Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compute_resources** | [**V1ResourceRequirements**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ResourceRequirements.md) |  | [optional] 
**metadata** | [**V1PipelineTaskMetadata**](V1PipelineTaskMetadata.md) |  | [optional] 
**pipeline_task_name** | **str** |  | [optional] 
**pod_template** | [**PodTemplate**](PodTemplate.md) |  | [optional] 
**service_account_name** | **str** |  | [optional] 
**sidecar_specs** | [**list[V1TaskRunSidecarSpec]**](V1TaskRunSidecarSpec.md) |  | [optional] 
**step_specs** | [**list[V1TaskRunStepSpec]**](V1TaskRunStepSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


