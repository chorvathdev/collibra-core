# ScopeImpl

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the represented object (entity). | 
**created_by** | **str** | The id of the user that created this resource. | [optional] 
**created_on** | **int** | The timestamp (in UTC time standard) of the creation of this resource. | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time. | [optional] 
**last_modified_on** | **int** | The timestamp (in UTC time standard) of the last modification of this resource. | [optional] 
**system** | **bool** | Whether this is a system resource or not. | [optional] 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]. | 
**name** | **str** | The name of the resource. | [optional] 
**description** | **str** | The description of the resource. | [optional] 
**domains** | [**list[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md) | The list of domains that are included in this scope. | [optional] 
**communities** | [**list[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md) | The list of communities that are included in this scope. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


