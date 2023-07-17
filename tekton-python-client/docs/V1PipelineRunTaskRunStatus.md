# V1PipelineRunTaskRunStatus

PipelineRunTaskRunStatus contains the name of the PipelineTask for this TaskRun and the TaskRun's Status
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pipeline_task_name** | **str** | PipelineTaskName is the name of the PipelineTask. | [optional] 
**status** | [**V1TaskRunStatus**](V1TaskRunStatus.md) |  | [optional] 
**when_expressions** | [**list[V1WhenExpression]**](V1WhenExpression.md) | WhenExpressions is the list of checks guarding the execution of the PipelineTask | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


