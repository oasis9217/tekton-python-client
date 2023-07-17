# V1PipelineTask

PipelineTask defines a task in a Pipeline, passing inputs from both Params and from the output of previous tasks.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description is the description of this task within the context of a Pipeline. This description may be used to populate a UI. | [optional] 
**display_name** | **str** | DisplayName is the display name of this task within the context of a Pipeline. This display name may be used to populate a UI. | [optional] 
**matrix** | [**V1Matrix**](V1Matrix.md) |  | [optional] 
**name** | **str** | Name is the name of this task within the context of a Pipeline. Name is used as a coordinate with the &#x60;from&#x60; and &#x60;runAfter&#x60; fields to establish the execution order of tasks relative to one another. | [optional] 
**params** | [**list[V1Param]**](V1Param.md) | Parameters declares parameters passed to this task. | [optional] 
**retries** | **int** | Retries represents how many times this task should be retried in case of task failure: ConditionSucceeded set to False | [optional] 
**run_after** | **list[str]** | RunAfter is the list of PipelineTask names that should be executed before this Task executes. (Used to force a specific ordering in graph execution.) | [optional] 
**task_ref** | [**V1TaskRef**](V1TaskRef.md) |  | [optional] 
**task_spec** | [**V1EmbeddedTask**](V1EmbeddedTask.md) |  | [optional] 
**timeout** | [**V1Duration**](V1Duration.md) |  | [optional] 
**when** | [**list[V1WhenExpression]**](V1WhenExpression.md) | When is a list of when expressions that need to be true for the task to run | [optional] 
**workspaces** | [**list[V1WorkspacePipelineTaskBinding]**](V1WorkspacePipelineTaskBinding.md) | Workspaces maps workspaces from the pipeline spec to the workspaces declared in the Task. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


