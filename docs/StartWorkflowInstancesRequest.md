# StartWorkflowInstancesRequest

The properties of the workflow to be started.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**workflow_definition_id** | **str** | The ID of the workflow definition. | 
**business_item_ids** | **list[str]** | The list of IDs for the business items. | [optional] 
**business_item_type** | **str** | The resource type of the passed in business items. | [optional] 
**form_properties** | **dict(str, str)** | The properties of the workflow. | [optional] 
**guest_user_id** | **str** | The ID of the guest user starting the workflow. | [optional] 
**send_notification** | **bool** | Whether a mail notification on starting the workflows should be sent. This notification is only used in the asynchronous api version (in a job). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


