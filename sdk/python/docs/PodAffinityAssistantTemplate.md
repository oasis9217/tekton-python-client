# PodAffinityAssistantTemplate

AffinityAssistantTemplate holds pod specific configuration and is a subset of the generic pod Template
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_pull_secrets** | [**list[V1LocalObjectReference]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1LocalObjectReference.md) | ImagePullSecrets gives the name of the secret used by the pod to pull the image if specified | [optional] 
**node_selector** | **dict(str, str)** | NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node&#39;s labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/ | [optional] 
**tolerations** | [**list[V1Toleration]**](https://github.com/kubernetes-client/python/blob/master/kubernetes/docs/V1Toleration.md) | If specified, the pod&#39;s tolerations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


