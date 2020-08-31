# Mapping

Represents a mapping. A mapping is a representation of a link between external entity from external system and corresponding resource in the Data Governance Center. A single mapping refers to at most one resource which can either be a community, a domain, or an asset.
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
**external_system_id** | **str** | The id of the external system that the mapped resource belongs to. | [optional] 
**external_entity_id** | **str** | The external id of the mapped resource. | [optional] 
**external_entity_url** | **str** | The external URL of the mapped resource. | [optional] 
**description** | **str** | The description of the mapped resource. | [optional] 
**mapped_resource** | [**NamedResourceReferenceImpl**](NamedResourceReferenceImpl.md) |  | [optional] 
**last_sync_date** | **int** | The timestamp (in UTC time standard) of the last synchronization of mapped resource. | [optional] 
**sync_action** | **str** | Represents the type of the action performed during last successful synchronization | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


