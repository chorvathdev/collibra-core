# ChangeDataQualityRuleRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The new name for the data quality rule. | [optional] 
**description** | **str** | The new description for the data quality rule. | [optional] 
**categorization_relation_type_id** | **str** | The ID of the categorization relation type. | [optional] 
**data_quality_metrics** | [**list[DataQualityMetricRequest]**](DataQualityMetricRequest.md) | The list of data quality metrics. | [optional] 
**relation_trace_entries** | [**list[RelationTraceEntryRequest]**](RelationTraceEntryRequest.md) | The list of relation trace entries that describes relations along which the data quality result is calculated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


