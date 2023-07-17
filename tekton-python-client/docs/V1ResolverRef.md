# V1ResolverRef

ResolverRef can be used to refer to a Pipeline or Task in a remote location like a git repo. This feature is in beta and these fields are only available when the beta feature gate is enabled.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**params** | [**list[V1Param]**](V1Param.md) | Params contains the parameters used to identify the referenced Tekton resource. Example entries might include \&quot;repo\&quot; or \&quot;path\&quot; but the set of params ultimately depends on the chosen resolver. | [optional] 
**resolver** | **str** | Resolver is the name of the resolver that should perform resolution of the referenced Tekton resource, such as \&quot;git\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


