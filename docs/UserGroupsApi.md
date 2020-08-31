# collibra_core.UserGroupsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_group**](UserGroupsApi.md#add_user_group) | **POST** /userGroups | Add new user group
[**add_users_to_user_group**](UserGroupsApi.md#add_users_to_user_group) | **POST** /userGroups/{userGroupId}/users | Add users to user group
[**change_user_group**](UserGroupsApi.md#change_user_group) | **PATCH** /userGroups/{userGroupId} | Change user group
[**find_user_groups**](UserGroupsApi.md#find_user_groups) | **GET** /userGroups | Find user groups
[**get_user_group**](UserGroupsApi.md#get_user_group) | **GET** /userGroups/{userGroupId} | Get user group
[**remove_user_group**](UserGroupsApi.md#remove_user_group) | **DELETE** /userGroups/{userGroupId} | Remove user group
[**remove_users_from_user_group**](UserGroupsApi.md#remove_users_from_user_group) | **DELETE** /userGroups/{userGroupId}/users | Remove users from user group


# **add_user_group**
> UserGroupImpl add_user_group(add_user_group_request=add_user_group_request)

Add new user group

Adds a new user group.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    add_user_group_request = collibra_core.AddUserGroupRequest() # AddUserGroupRequest |  (optional)

    try:
        # Add new user group
        api_response = api_instance.add_user_group(add_user_group_request=add_user_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->add_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_user_group_request** | [**AddUserGroupRequest**](AddUserGroupRequest.md)|  | [optional] 

### Return type

[**UserGroupImpl**](UserGroupImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User group successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_users_to_user_group**
> list[User] add_users_to_user_group(user_group_id, add_users_to_user_group_request=add_users_to_user_group_request)

Add users to user group

Adds users to an existing user group.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of the user group
add_users_to_user_group_request = collibra_core.AddUsersToUserGroupRequest() # AddUsersToUserGroupRequest |  (optional)

    try:
        # Add users to user group
        api_response = api_instance.add_users_to_user_group(user_group_id, add_users_to_user_group_request=add_users_to_user_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->add_users_to_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | [**str**](.md)| The ID of the user group | 
 **add_users_to_user_group_request** | [**AddUsersToUserGroupRequest**](AddUsersToUserGroupRequest.md)|  | [optional] 

### Return type

[**list[User]**](User.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users successfully added to user group. |  -  |
**404** | User group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_user_group**
> UserGroupImpl change_user_group(user_group_id, change_user_group_request=change_user_group_request)

Change user group

Changes the user group with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of the user group
change_user_group_request = collibra_core.ChangeUserGroupRequest() # ChangeUserGroupRequest |  (optional)

    try:
        # Change user group
        api_response = api_instance.change_user_group(user_group_id, change_user_group_request=change_user_group_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->change_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | [**str**](.md)| The ID of the user group | 
 **change_user_group_request** | [**ChangeUserGroupRequest**](ChangeUserGroupRequest.md)|  | [optional] 

### Return type

[**UserGroupImpl**](UserGroupImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group changed |  -  |
**404** | User group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_user_groups**
> UserGroupPagedResponse find_user_groups(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, user_id=user_id, include_everyone=include_everyone)

Find user groups

Returns user groups matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 user groups is returned.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the user group. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')
user_id = 'user_id_example' # str | The ID of the user who should belong to searched user groups. (optional)
include_everyone = True # bool | Indicates if we should include the everyone group or not. (optional)

    try:
        # Find user groups
        api_response = api_instance.find_user_groups(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, user_id=user_id, include_everyone=include_everyone)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->find_user_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the user group. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]
 **user_id** | [**str**](.md)| The ID of the user who should belong to searched user groups. | [optional] 
 **include_everyone** | **bool**| Indicates if we should include the everyone group or not. | [optional] 

### Return type

[**UserGroupPagedResponse**](UserGroupPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search completed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_group**
> UserGroupImpl get_user_group(user_group_id)

Get user group

Returns the user group with the given ID.

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of the user group

    try:
        # Get user group
        api_response = api_instance.get_user_group(user_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->get_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | [**str**](.md)| The ID of the user group | 

### Return type

[**UserGroupImpl**](UserGroupImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group found |  -  |
**404** | User group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_group**
> remove_user_group(user_group_id)

Remove user group

Removes the user group with the given ID

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of the user group

    try:
        # Remove user group
        api_instance.remove_user_group(user_group_id)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->remove_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | [**str**](.md)| The ID of the user group | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User group removed |  -  |
**404** | User group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users_from_user_group**
> remove_users_from_user_group(user_group_id, remove_users_from_user_group_request=remove_users_from_user_group_request)

Remove users from user group

Removes users from the user group with the given ID

### Example

* Basic Authentication (basicAuth):
```python
from __future__ import print_function
import time
import collibra_core
from collibra_core.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/rest/2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = collibra_core.Configuration(
    host = "http://localhost/rest/2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = collibra_core.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with collibra_core.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = collibra_core.UserGroupsApi(api_client)
    user_group_id = 'user_group_id_example' # str | The ID of the user group
remove_users_from_user_group_request = collibra_core.RemoveUsersFromUserGroupRequest() # RemoveUsersFromUserGroupRequest |  (optional)

    try:
        # Remove users from user group
        api_instance.remove_users_from_user_group(user_group_id, remove_users_from_user_group_request=remove_users_from_user_group_request)
    except ApiException as e:
        print("Exception when calling UserGroupsApi->remove_users_from_user_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_group_id** | [**str**](.md)| The ID of the user group | 
 **remove_users_from_user_group_request** | [**RemoveUsersFromUserGroupRequest**](RemoveUsersFromUserGroupRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users removed from user group |  -  |
**404** | User group not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

