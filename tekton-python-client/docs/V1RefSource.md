# V1RefSource

RefSource contains the information that can uniquely identify where a remote built definition came from i.e. Git repositories, Tekton Bundles in OCI registry and hub.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**digest** | **dict(str, str)** | Digest is a collection of cryptographic digests for the contents of the artifact specified by URI. Example: {\&quot;sha1\&quot;: \&quot;f99d13e554ffcb696dee719fa85b695cb5b0f428\&quot;} | [optional] 
**entry_point** | **str** | EntryPoint identifies the entry point into the build. This is often a path to a build definition file and/or a target label within that file. Example: \&quot;task/git-clone/0.8/git-clone.yaml\&quot; | [optional] 
**uri** | **str** | URI indicates the identity of the source of the build definition. Example: \&quot;https://github.com/tektoncd/catalog\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


