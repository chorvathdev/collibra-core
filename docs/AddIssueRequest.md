# AddIssueRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**responsible_community_id** | **str** | The ID of the community responsible for handling the issue. | [optional] 
**name** | **str** | The name of the subject for which the issue is being created. | 
**type_id** | **str** | The type ID of the issue to be created. | 
**description** | **str** | The description for the issue. | 
**priority** | **str** | The priority for the issue. | [optional] 
**requester_id** | **str** | The requester of the issue. | [optional] 
**related_assets** | [**list[RelatedAssetReference]**](RelatedAssetReference.md) | The list of assets which the issue is related to. | [optional] 
**category_ids** | **list[str]** | The list of IDs of assets which represent categories for this issue. Each asset in this list should be of type Issue Category. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


