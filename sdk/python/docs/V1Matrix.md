# V1Matrix

Matrix is used to fan out Tasks in a Pipeline
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**include** | [**list[V1IncludeParams]**](V1IncludeParams.md) | Include is a list of IncludeParams which allows passing in specific combinations of Parameters into the Matrix. | [optional] 
**params** | [**list[V1Param]**](V1Param.md) | Params is a list of parameters used to fan out the pipelineTask Params takes only &#x60;Parameters&#x60; of type &#x60;\&quot;array\&quot;&#x60; Each array element is supplied to the &#x60;PipelineTask&#x60; by substituting &#x60;params&#x60; of type &#x60;\&quot;string\&quot;&#x60; in the underlying &#x60;Task&#x60;. The names of the &#x60;params&#x60; in the &#x60;Matrix&#x60; must match the names of the &#x60;params&#x60; in the underlying &#x60;Task&#x60; that they will be substituting. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


