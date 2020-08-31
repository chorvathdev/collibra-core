# Job

Represents a job. Job is a single atomic task that is to be performed asynchronously
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id of the represented object (entity). | 
**created_by** | **str** | The id of the user that created this resource. | [optional] 
**created_on** | **int** | The timestamp (in UTC time standard) of the creation of this resource. | [optional] 
**last_modified_by** | **str** | The id of the user who modified this resource the last time. | [optional] 
**last_modified_on** | **int** | The timestamp (in UTC time standard) of the last modification of this resource. | [optional] 
**system** | **bool** | Whether this is a system resource or not. | [optional] 
**resource_type** | **str** | The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance]. | 
**name** | **str** | The name of the resource. | [optional] 
**type** | **str** | The type of the job. | [optional] 
**user_id** | **str** | The ID of the user that initiated this job. | [optional] 
**visibility** | **int** | The visibility of the job. | [optional] 
**progress_percentage** | **float** | The progress percentage of the job. | [optional] 
**cancelable** | **bool** | Whether this job is cancelable or not. | [optional] 
**start_date** | **int** | The start date of the job. | [optional] 
**end_date** | **int** | The end date of the job. | [optional] 
**state** | **str** | The state of the job. | [optional] 
**message** | **str** | The message of the job. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


