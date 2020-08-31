# AssignmentImpl

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
**statuses** | [**list[NamedDescribedResourceReference]**](NamedDescribedResourceReference.md) | The list of references to the statuses. | [optional] 
**default_status_id** | **str** | The ID of the default status. | [optional] 
**characteristic_types** | [**list[AssignedCharacteristicType]**](AssignedCharacteristicType.md) | The list of assigned characteristic types (attribute types, relation types and complex relation types). | [optional] 
**articulation_rules** | [**list[ArticulationRuleImpl]**](ArticulationRuleImpl.md) | The list of articulation rules applying with the assignment. | [optional] 
**validation_rules** | [**list[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md) | The list of references to validation rules applying with the assignment. | [optional] 
**data_quality_rules** | [**list[NamedDescribedResourceReference]**](NamedDescribedResourceReference.md) | The list of references to data quality rules applying with the assignment. | [optional] 
**domain_types** | [**list[NamedDescribedResourceReference]**](NamedDescribedResourceReference.md) | The list of references to domain types which the assignment refers to. | [optional] 
**scope** | [**ScopeImpl**](ScopeImpl.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


