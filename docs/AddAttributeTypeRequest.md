# AddAttributeTypeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new attribute type. Should be unique within all attribute types.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**name** | **str** | The name of the new attribute type. Should be unique within all attribute types. | 
**description** | **str** | The description of the new attribute type. | [optional] 
**kind** | **str** | The kind of the new attribute type. | 
**language** | **str** | The language of the new attribute type. | [optional] 
**statistics_enabled** | **bool** | Whether statistics should be enabled. | [optional] 
**allowed_values** | **list[str]** | List of allowed values. | [optional] 
**string_type** | **str** | Rich text or plain text (only applicable for String attribute type). | [optional] 
**id_string** | **str** |  | [optional] 
**is_integer** | **bool** | Whether attribute type holds integer value. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


