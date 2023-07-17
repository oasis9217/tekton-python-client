# V1PipelineRunStatusFields

PipelineRunStatusFields holds the fields of PipelineRunStatus' status. This is defined separately and inlined so that other types can readily consume these fields via duck typing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**child_references** | [**list[V1ChildStatusReference]**](V1ChildStatusReference.md) | list of TaskRun and Run names, PipelineTask names, and API versions/kinds for children of this PipelineRun. | [optional] 
**completion_time** | [**V1Time**](V1Time.md) |  | [optional] 
**finally_start_time** | [**V1Time**](V1Time.md) |  | [optional] 
**pipeline_spec** | [**V1PipelineSpec**](V1PipelineSpec.md) |  | [optional] 
**provenance** | [**V1Provenance**](V1Provenance.md) |  | [optional] 
**results** | [**list[V1PipelineRunResult]**](V1PipelineRunResult.md) | Results are the list of results written out by the pipeline task&#39;s containers | [optional] 
**skipped_tasks** | [**list[V1SkippedTask]**](V1SkippedTask.md) | list of tasks that were skipped due to when expressions evaluating to false | [optional] 
**span_context** | **dict(str, str)** | SpanContext contains tracing span context fields | [optional] 
**start_time** | [**V1Time**](V1Time.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


