# AddDomainRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the new domain. Should be unique within the community. | 
**community_id** | **str** | The ID of the community that the new domain should be added to. | 
**type_id** | **str** | The ID of the domain type of the new domain. | 
**description** | **str** | The description of the new domain. | [optional] 
**id** | **str** | The ID of the new domain. Should be unique within all domains.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**excluded_from_auto_hyperlinking** | **bool** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


