# AddDataQualityRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new Data Quality Rule. Should be unique within all data quality rules.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with&lt;br/&gt;&lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**name** | **str** | The name of the new data quality rule. Should be unique within all data quality rules. | 
**description** | **str** | The description of the new data quality rule. | [optional] 
**categorization_relation_type_id** | **str** | The ID of the categorization relation type. | 
**data_quality_metrics** | [**list[DataQualityMetricRequest]**](DataQualityMetricRequest.md) | The Data Quality Metrics that should be assigned to the rule that is going to be created. | [optional] 
**relation_trace_entries** | [**list[RelationTraceEntryRequest]**](RelationTraceEntryRequest.md) | The list of entries that describes relations along which the data quality result is calculated. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


