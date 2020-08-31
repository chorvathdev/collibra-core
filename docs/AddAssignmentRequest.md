# AddAssignmentRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the new assignment. Should be unique within all assignments.&lt;br/&gt;It should have a format of universally unique identifier (UUID) and should not start with &lt;code&gt;00000000-0000-0000-&lt;/code&gt; which is a reserved prefix. | [optional] 
**asset_type_id** | **str** | The ID of the asset type corresponding to the assignment | 
**status_ids** | **list[str]** | The list of IDs of the statuses | 
**characteristic_types** | [**list[CharacteristicTypeAssignmentReference]**](CharacteristicTypeAssignmentReference.md) | The list of the references to characteristic types corresponding to the assignment. | [optional] 
**articulation_rules** | [**list[ArticulationRuleRequest]**](ArticulationRuleRequest.md) | The list of the articulation rules. | [optional] 
**validation_rule_ids** | **list[str]** | The list of IDs of the validation rules | [optional] 
**data_quality_rule_ids** | **list[str]** | The list of IDs of the data quality rules | [optional] 
**domain_type_ids** | **list[str]** | The list of IDs of the domain types | [optional] 
**default_status_id** | **str** | The ID of the default status for the asset type | 
**scope_id** | **str** | The ID of the scope the assignment corresponds to | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


