# AddMappingRequest

The properties of the mapping to be added.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new mapping. Should be unique within all mappings.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**external_system_id** | **str** | The ID of the external system that the mapped resource belongs to. | 
**external_entity_id** | **str** | The external ID of the mapped resource. | 
**external_entity_url** | **str** | The external URL of the mapped resource. | [optional] 
**description** | **str** | The description of the mapped resource. | [optional] 
**mapped_resource_id** | **str** | The ID of the mapped resource. | [optional] 
**last_sync_date** | **int** | The timestamp (in UTC time standard) of the last synchronization of mapped resource. | [optional] 
**sync_action** | **str** | Represents the type of the action performed during last successful synchronization | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


