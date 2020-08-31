# FormProperty

Represents one field in the form.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the property. | [optional] 
**name** | **str** | The name of the property. | [optional] 
**type** | **str** | The property type. | [optional] 
**value** | **str** | The property (default) value. | [optional] 
**writable** | **bool** | Whether the property is writable. | [optional] 
**required** | **bool** | Whether the property is required. | [optional] 
**enum_values** | [**list[DropdownValue]**](DropdownValue.md) | The property&#39;s enum values. | [optional] 
**check_buttons** | [**list[OptionValue]**](OptionValue.md) | The property&#39;s checkbox buttons. | [optional] 
**radio_buttons** | [**list[OptionValue]**](OptionValue.md) | The property&#39;s radio buttons. | [optional] 
**default_dropdown_values** | [**list[DropdownValue]**](DropdownValue.md) | The property&#39;s default dropdown values. | [optional] 
**proposed_dropdown_values** | [**list[DropdownValue]**](DropdownValue.md) | The property&#39;s proposed dropdown values. | [optional] 
**date_time_type** | **str** | The datetime type in case the property is of type datetime. | [optional] 
**multi_value** | **bool** | Whether the property allows multiple values. | [optional] 
**proposed_fixed** | **bool** | Whether the property&#39;s proposed values are the only set of allowed values to select. | [optional] 
**default_from_resource** | **bool** | Whether the property&#39;s default value is the current resource. | [optional] 
**multi_default_dropdown_values** | **dict(str, list[DropdownValue])** | The multi default dropdown values. | [optional] 
**multi_proposed_dropdown_values** | **dict(str, list[DropdownValue])** | The multi proposed dropdown values. | [optional] 
**asset_type** | [**ResourceReference**](ResourceReference.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


