# User

Represents a user in the system.
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
**user_name** | **str** | The user name. | [optional] 
**first_name** | **str** | The first name of the user. | [optional] 
**last_name** | **str** | The last name of the user. | [optional] 
**email_address** | **str** | The main email address. | [optional] 
**gender** | **str** | The gender of the user. | [optional] 
**language** | **str** | The current language preference for this user. | [optional] 
**additional_email_addresses** | [**list[Email]**](Email.md) | The list of additional email addresses. | [optional] 
**phone_numbers** | [**list[PhoneNumber]**](PhoneNumber.md) | The list of phone numbers. | [optional] 
**instant_messaging_accounts** | [**list[InstantMessagingAccount]**](InstantMessagingAccount.md) | The list of instant messaging accounts. | [optional] 
**websites** | [**list[Website]**](Website.md) | The list of websites. | [optional] 
**addresses** | [**list[Address]**](Address.md) | The list of addresses. | [optional] 
**activated** | **bool** | Whether this user account is already activated or not. | [optional] 
**enabled** | **bool** | Whether this user account is already enabled or not. | [optional] 
**ldap_user** | **bool** | Whether this is an LDAP user or not. | [optional] 
**guest_user** | **bool** | Whether this is a guest user or not. | [optional] 
**api_user** | **bool** | Whether this is API user or not. | [optional] 
**license_type** | **str** | The licence type of the user. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


