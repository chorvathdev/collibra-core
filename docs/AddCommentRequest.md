# AddCommentRequest

The properties of the comment to be added.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** | The actual HTML content of the comment to be added. Can contain user mentions using syntax [@User:$userId] where $userId is the ID of mentioned user.For example: [@User:00000000-0000-0000-0000-000000900002]. | 
**base_resource** | [**ResourceReference**](ResourceReference.md) |  | 
**parent_id** | **str** | The ID of the parent comment. If not null - the comment is the reply for the parent comment. | [optional] 
**base_resource_id** | **str** |  | [optional] 
**base_resource_type** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


