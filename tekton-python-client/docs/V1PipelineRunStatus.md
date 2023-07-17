# V1PipelineRunStatus

PipelineRunStatus defines the observed state of PipelineRun
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotations** | **dict(str, str)** | Annotations is additional Status fields for the Resource to save some additional State as well as convey more information to the user. This is roughly akin to Annotations on any k8s resource, just the reconciler conveying richer information outwards. | [optional] 
**child_references** | [**list[V1ChildStatusReference]**](V1ChildStatusReference.md) | list of TaskRun and Run names, PipelineTask names, and API versions/kinds for children of this PipelineRun. | [optional] 
**completion_time** | [**V1Time**](V1Time.md) |  | [optional] 
**conditions** | [**list[KnativeCondition]**](KnativeCondition.md) | Conditions the latest available observations of a resource&#39;s current state. | [optional] 
**finally_start_time** | [**V1Time**](V1Time.md) |  | [optional] 
**observed_generation** | **int** | ObservedGeneration is the &#39;Generation&#39; of the Service that was last processed by the controller. | [optional] 
**pipeline_spec** | [**V1PipelineSpec**](V1PipelineSpec.md) |  | [optional] 
**provenance** | [**V1Provenance**](V1Provenance.md) |  | [optional] 
**results** | [**list[V1PipelineRunResult]**](V1PipelineRunResult.md) | Results are the list of results written out by the pipeline task&#39;s containers | [optional] 
**skipped_tasks** | [**list[V1SkippedTask]**](V1SkippedTask.md) | list of tasks that were skipped due to when expressions evaluating to false | [optional] 
**span_context** | **dict(str, str)** | SpanContext contains tracing span context fields | [optional] 
**start_time** | [**V1Time**](V1Time.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


