# ComplexRelationLegImpl

The list of complex relation legs - assets related to the complex relation with role and co-role provided.
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
**asset_type** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**asset** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**asset_reference** | [**AssetReferenceImpl**](AssetReferenceImpl.md) |  | [optional] 
**role** | **str** | The role that the asset assigned to this leg plays in the complex relation. | [optional] 
**co_role** | **str** | The co-role for the asset assigned to this leg. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


