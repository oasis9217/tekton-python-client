# V1TaskRef

TaskRef can be used to refer to a specific instance of a task.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_version** | **str** | API version of the referent Note: A Task with non-empty APIVersion and Kind is considered a Custom Task | [optional] 
**kind** | **str** | TaskKind indicates the Kind of the Task: 1. Namespaced Task when Kind is set to \&quot;Task\&quot;. If Kind is \&quot;\&quot;, it defaults to \&quot;Task\&quot;. 2. Custom Task when Kind is non-empty and APIVersion is non-empty | [optional] 
**name** | **str** | Name of the referent; More info: http://kubernetes.io/docs/user-guide/identifiers#names | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


