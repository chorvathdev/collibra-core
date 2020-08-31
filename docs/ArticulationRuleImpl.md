# ArticulationRuleImpl

The list of articulation rules applying with the assignment.
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
**score** | **float** | The value that should be either added or set (depending on the operation) when this rule matches. | [optional] 
**operation** | **str** | The type of an operation that should be performed when asset is matching this rule. | [optional] 
**status** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**attribute_type** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


