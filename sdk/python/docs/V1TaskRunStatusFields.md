# V1TaskRunStatusFields

TaskRunStatusFields holds the fields of TaskRun's status.  This is defined separately and inlined so that other types can readily consume these fields via duck typing.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**completion_time** | [**V1Time**](V1Time.md) |  | [optional] 
**pod_name** | **str** | PodName is the name of the pod responsible for executing this task&#39;s steps. | [default to '']
**provenance** | [**V1Provenance**](V1Provenance.md) |  | [optional] 
**results** | [**list[V1TaskRunResult]**](V1TaskRunResult.md) | Results are the list of results written out by the task&#39;s containers | [optional] 
**retries_status** | [**list[V1TaskRunStatus]**](V1TaskRunStatus.md) | RetriesStatus contains the history of TaskRunStatus in case of a retry in order to keep record of failures. All TaskRunStatus stored in RetriesStatus will have no date within the RetriesStatus as is redundant. | [optional] 
**sidecars** | [**list[V1SidecarState]**](V1SidecarState.md) | The list has one entry per sidecar in the manifest. Each entry is represents the imageid of the corresponding sidecar. | [optional] 
**span_context** | **dict(str, str)** | SpanContext contains tracing span context fields | [optional] 
**start_time** | [**V1Time**](V1Time.md) |  | [optional] 
**steps** | [**list[V1StepState]**](V1StepState.md) | Steps describes the state of each build step container. | [optional] 
**task_spec** | [**V1TaskSpec**](V1TaskSpec.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


