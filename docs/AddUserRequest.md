# AddUserRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The username, which should be unique | 
**first_name** | **str** | The first name of the new user | [optional] 
**last_name** | **str** | The last name of the new user | [optional] 
**email_address** | **str** | The e-mail address of the new user | 
**gender** | **str** | The gender of the user | [optional] 
**language** | **str** | The language for the user | [optional] 
**user_group_ids** | **list[str]** | The groups this newly created user should be added to | [optional] 
**license_type** | **str** | The license type of the user. LicenseType will be removed in the next major release. | [optional] 
**addresses** | [**list[Address]**](Address.md) | The postal addresses of the user | [optional] 
**phones** | [**list[PhoneNumber]**](PhoneNumber.md) | The phone numbers of the user | [optional] 
**additional_email_addresses** | [**list[Email]**](Email.md) | The additional e-mail addresses of the user | [optional] 
**instant_messaging_accounts** | [**list[InstantMessagingAccount]**](InstantMessagingAccount.md) | The instant messaging accounts of the user | [optional] 
**websites** | [**list[Website]**](Website.md) | The websites of the user | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


