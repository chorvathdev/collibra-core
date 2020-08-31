# AddAssetRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The full name of the new asset. Should be unique within the domain. | 
**display_name** | **str** | The display name of the new asset. | [optional] 
**domain_id** | **str** | The ID of the domain that the new asset should be added to. | 
**type_id** | **str** | The ID of the asset type of the new asset. | 
**id** | **str** | The ID of the new asset. Should be unique within all assets.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**status_id** | **str** | The ID of the status of the new asset. | [optional] 
**excluded_from_auto_hyperlinking** | **bool** | Whether or not to exclude the new asset from auto hyperlinking. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


