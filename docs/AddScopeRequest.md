# AddScopeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new scope. Should be unique within all scopes.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with&lt;br/&gt;&lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**name** | **str** | The name of the new scope | 
**description** | **str** | The description of the new scope | [optional] 
**domain_ids** | **list[str]** | The list of IDs for domains assigned to the new scope | [optional] 
**community_ids** | **list[str]** | The list of IDs for communities assigned to the new scope | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


