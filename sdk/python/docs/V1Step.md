# V1Step

Step runs a subcomponent of a Task
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **list[str]** | Arguments to the entrypoint. The image&#39;s CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#39;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell | [optional] 
**command** | **list[str]** | Entrypoint array. Not executed within a shell. The image&#39;s ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container&#39;s environment. If a variable cannot be resolved, the reference in the input string will be unchanged. Double $$ are reduced to a single $, which allows for escaping the $(VAR_NAME) syntax: i.e. \&quot;$$(VAR_NAME)\&quot; will produce the string literal \&quot;$(VAR_NAME)\&quot;. Escaped references will never be expanded, regardless of whether the variable exists or not. Cannot be updated. More info: https://kubernetes.io/docs/tasks/inject-data-application/define-command-argument-container/#running-a-command-in-a-shell | [optional] 
**compute_resources** | [**V1ResourceRequirements**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1ResourceRequirements.md) |  | [optional] 
**env** | [**list[V1EnvVar]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1EnvVar.md) | List of environment variables to set in the Step. Cannot be updated. | [optional] 
**env_from** | [**list[V1EnvFromSource]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1EnvFromSource.md) | List of sources to populate environment variables in the Step. The keys defined within a source must be a C_IDENTIFIER. All invalid keys will be reported as an event when the Step is starting. When a key exists in multiple sources, the value associated with the last source will take precedence. Values defined by an Env with a duplicate key will take precedence. Cannot be updated. | [optional] 
**image** | **str** | Docker image name. More info: https://kubernetes.io/docs/concepts/containers/images | [optional] 
**image_pull_policy** | **str** | Image pull policy. One of Always, Never, IfNotPresent. Defaults to Always if :latest tag is specified, or IfNotPresent otherwise. Cannot be updated. More info: https://kubernetes.io/docs/concepts/containers/images#updating-images | [optional] 
**name** | **str** | Name of the Step specified as a DNS_LABEL. Each Step in a Task must have a unique name. | [default to '']
**on_error** | **str** | OnError defines the exiting behavior of a container on error can be set to [ continue | stopAndFail ] | [optional] 
**script** | **str** | Script is the contents of an executable file to execute.  If Script is not empty, the Step cannot have an Command and the Args will be passed to the Script. | [optional] 
**security_context** | [**V1SecurityContext**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1SecurityContext.md) |  | [optional] 
**stderr_config** | [**V1StepOutputConfig**](V1StepOutputConfig.md) |  | [optional] 
**stdout_config** | [**V1StepOutputConfig**](V1StepOutputConfig.md) |  | [optional] 
**timeout** | [**V1Duration**](V1Duration.md) |  | [optional] 
**volume_devices** | [**list[V1VolumeDevice]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1VolumeDevice.md) | volumeDevices is the list of block devices to be used by the Step. | [optional] 
**volume_mounts** | [**list[V1VolumeMount]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1VolumeMount.md) | Volumes to mount into the Step&#39;s filesystem. Cannot be updated. | [optional] 
**working_dir** | **str** | Step&#39;s working directory. If not specified, the container runtime&#39;s default will be used, which might be configured in the container image. Cannot be updated. | [optional] 
**workspaces** | [**list[V1WorkspaceUsage]**](V1WorkspaceUsage.md) | This is an alpha field. You must set the \&quot;enable-api-fields\&quot; feature flag to \&quot;alpha\&quot; for this field to be supported.  Workspaces is a list of workspaces from the Task that this Step wants exclusive access to. Adding a workspace to this list means that any other Step or Sidecar that does not also request this Workspace will not have access to it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


