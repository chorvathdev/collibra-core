# AddAssetTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The UUID that will be assigned to the new asset type. It should be unique within all asset types, and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**name** | **str** | The name of the new asset type. Should be unique within all asset types. | 
**description** | **str** | The description of the new asset type. | [optional] 
**color** | **str** | The color of the symbol in hex format. | [optional] 
**symbol_type** | **str** | The symbol type. | 
**icon_code** | **str** | The icon code, a code representing the icon that should be shown. | [optional] 
**acronym_code** | **str** | A code representing the acronym that should be shown. | [optional] 
**parent_id** | **str** | The ID of the parent for the new asset type. | [optional] 
**display_name_enabled** | **bool** | Whether the display name should be enabled for all assets of the type being created. | 
**rating_enabled** | **bool** | Whether ratings should be enabled for all assets of the type being created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


