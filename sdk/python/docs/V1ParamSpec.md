# V1ParamSpec

ParamSpec defines arbitrary parameters needed beyond typed inputs (such as resources). Parameter values are provided by users as inputs on a TaskRun or PipelineRun.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**default** | [**V1ParamValue**](V1ParamValue.md) |  | [optional] 
**description** | **str** | Description is a user-facing description of the parameter that may be used to populate a UI. | [optional] 
**name** | **str** | Name declares the name by which a parameter is referenced. | [default to '']
**properties** | [**dict(str, V1PropertySpec)**](V1PropertySpec.md) | Properties is the JSON Schema properties to support key-value pairs parameter. | [optional] 
**type** | **str** | Type is the user-specified type of the parameter. The possible types are currently \&quot;string\&quot;, \&quot;array\&quot; and \&quot;object\&quot;, and \&quot;string\&quot; is the default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


