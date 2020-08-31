# ExportComplexRelationsToExcelRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**complex_relation_type_id** | **str** | The Id of the ComplexRelationType for which the export will be executed. | 
**domain_id** | **str** | The Id of the Domain to filter on (optional). | [optional] 
**store_as_attachment** | **bool** | Sets if the export should be stored as an attachment (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;)&lt;br/&gt;of the provided {@link #domainId}. | [optional] 
**file_name** | **str** | The name of the file. (optional) if not provided a name is generated. | [optional] 
**include_header_row** | **bool** | Set if the file will include a header (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;)&lt;br/&gt;Default value is &lt;code&gt;false&lt;/code&gt;. | [optional] 
**support_roundtrip** | **bool** | Adds characteristics to support reimport (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;)&lt;br/&gt;Default value is &lt;code&gt;false&lt;/code&gt;. | [optional] 
**remove_formatting** | **bool** | Remove text formatting (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;)&lt;br/&gt;Default value is &lt;code&gt;false&lt;/code&gt;. | [optional] 
**sheet_name** | **str** | The name of the sheet. | [optional] 
**xlsx** | **bool** | Set if the Excel file to export will be &#39;.xlsx&#39; file (&lt;code&gt;true&lt;/code&gt;) or a &#39;.xls&#39; file (&lt;code&gt;false&lt;/code&gt;)&lt;br/&gt;Default value is (&lt;code&gt;true&lt;/code&gt;). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


