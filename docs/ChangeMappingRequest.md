# ChangeMappingRequest

The properties of the mapping to be changed, for the mapping identified by its ID.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the mapping to be changed. Silently ignored if the ID is provided as path parameter of the request. | 
**external_system_id** | **str** | The ID of the external system that the mapped resource belongs to. | [optional] 
**external_entity_id** | **str** | The external ID of the mapped resource. | [optional] 
**external_entity_url** | **str** | The external URL of the mapped resource. | [optional] 
**description** | **str** | The description of the mapped resource. | [optional] 
**mapped_resource_id** | **str** | The ID of the mapped resource. | [optional] 
**last_sync_date** | **int** | The timestamp (in UTC time standard) of the last synchronization of mapped resource. | [optional] 
**sync_action** | **str** | Represents the type of the action performed during last successful synchronization | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


