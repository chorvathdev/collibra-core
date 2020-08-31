# ChangeWorkflowDefinitionRequest

Parameters for the workflow definition to be changed.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the workflow definition. | [optional] 
**description** | **str** | The new description for the workflow definition. | [optional] 
**configuration_variables** | **dict(str, str)** | The configuration variables. | [optional] 
**start_events** | **list[str]** | The list of workflow start event types. | [optional] 
**business_item_resource_type** | **str** | The type of the business item corresponding to the workflow. | [optional] 
**exclusivity** | **str** | Defines the number of times a resource workflow is able to be start. | [optional] 
**guest_user_accessible** | **bool** |  | [optional] 
**registered_user_accessible** | **bool** | Whether the workflow should be accessible by the registered user. | [optional] 
**candidate_user_check_disabled** | **bool** | Whether the candidate user check for the workflow should be disabled. | [optional] 
**global_create** | **bool** | Whether the workflow is accessible from the global create menu. | [optional] 
**enable** | **bool** | Whether the workflow definition should be enabled. | [optional] 
**start_label** | **str** | The start label of the workflow. | [optional] 
**start_role_ids** | **list[str]** | The list of IDs identifying the roles allowing to start the workflow. | [optional] 
**stop_role_ids** | **list[str]** | The list of IDs identifying the roles allowing to stop the workflow. | [optional] 
**reassign_role_ids** | **list[str]** | The list of IDs identifying the roles allowing to reassign the workflow. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


