# AddRoleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new role. Should be unique within all roles&lt;br/&gt;&lt;p&gt;&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start&lt;br/&gt;with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**name** | **str** | The name of the new role. Should be unique within all roles. | 
**_global** | **bool** | Whether the role should be a global or resource role. | [optional] 
**description** | **str** | The description of the role. | [optional] 
**permissions** | **list[str]** | The permissions to be granted for this role. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


