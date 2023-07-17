# V1PipelineSpec

PipelineSpec defines the desired state of Pipeline.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Description is a user-facing description of the pipeline that may be used to populate a UI. | [optional] 
**display_name** | **str** | DisplayName is a user-facing name of the pipeline that may be used to populate a UI. | [optional] 
**_finally** | [**list[V1PipelineTask]**](V1PipelineTask.md) | Finally declares the list of Tasks that execute just before leaving the Pipeline i.e. either after all Tasks are finished executing successfully or after a failure which would result in ending the Pipeline | [optional] 
**params** | [**list[V1ParamSpec]**](V1ParamSpec.md) | Params declares a list of input parameters that must be supplied when this Pipeline is run. | [optional] 
**results** | [**list[V1PipelineResult]**](V1PipelineResult.md) | Results are values that this pipeline can output once run | [optional] 
**tasks** | [**list[V1PipelineTask]**](V1PipelineTask.md) | Tasks declares the graph of Tasks that execute when this Pipeline is run. | [optional] 
**workspaces** | [**list[V1PipelineWorkspaceDeclaration]**](V1PipelineWorkspaceDeclaration.md) | Workspaces declares a set of named workspaces that are expected to be provided by a PipelineRun. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


