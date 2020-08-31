# ComplexRelationLegTypeRequest

The new list of leg types for the complex relation type.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** | The minimum number of leg type occurrences. | [optional] 
**max** | **int** | The maximum number of leg type occurrences. | [optional] 
**role** | **str** | The name of the role that the source plays. | 
**co_role** | **str** | The name of the role that the target plays. | [optional] 
**asset_type_id** | **str** | The ID of the asset type for relation.&lt;br/&gt;In the next major release, this parameter will only be valid when adding a new leg to the ComplexRelationType. Changing the assetType of an existing leg won&#39;t be allowed and will result in an error. | 
**id** | **str** | The id of the complex relation leg type. The leg type will be created with this id or updated.&lt;br/&gt;If left empty on update the leg type will be recreated. | [optional] 
**relation_type_id** | **str** | The id of relation type for leg type. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


