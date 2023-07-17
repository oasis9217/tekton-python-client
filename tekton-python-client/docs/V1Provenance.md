# V1Provenance

Provenance contains metadata about resources used in the TaskRun/PipelineRun such as the source from where a remote build definition was fetched. This field aims to carry minimum amoumt of metadata in *Run status so that Tekton Chains can capture them in the provenance.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**feature_flags** | [**GithubComTektoncdPipelinePkgApisConfigFeatureFlags**](GithubComTektoncdPipelinePkgApisConfigFeatureFlags.md) |  | [optional] 
**ref_source** | [**V1RefSource**](V1RefSource.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


