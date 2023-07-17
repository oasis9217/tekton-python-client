# V1ChildStatusReference

ChildStatusReference is used to point to the statuses of individual TaskRuns and Runs within this PipelineRun.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**name** | **str** | Name is the name of the TaskRun or Run this is referencing. | [optional] 
**pipeline_task_name** | **str** | PipelineTaskName is the name of the PipelineTask this is referencing. | [optional] 
**when_expressions** | [**list[V1WhenExpression]**](V1WhenExpression.md) | WhenExpressions is the list of checks guarding the execution of the PipelineTask | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


