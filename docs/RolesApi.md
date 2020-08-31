# collibra_core.RolesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role**](RolesApi.md#add_role) | **POST** /roles | Adds a new role.
[**change_role**](RolesApi.md#change_role) | **PATCH** /roles/{roleId} | Change the role with the given id.
[**find_roles**](RolesApi.md#find_roles) | **GET** /roles | Returns roles matching the given search criteria.
[**get_role**](RolesApi.md#get_role) | **GET** /roles/{roleId} | Returns the role identified by the given id.
[**remove_role**](RolesApi.md#remove_role) | **DELETE** /roles/{roleId} | Removes the role identified by the given id.


# **add_role**
> RoleImpl add_role(add_role_request=add_role_request)

Adds a new role.

Adds new role.

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
    api_instance = collibra_core.RolesApi(api_client)
    add_role_request = collibra_core.AddRoleRequest() # AddRoleRequest |  (optional)

    try:
        # Adds a new role.
        api_response = api_instance.add_role(add_role_request=add_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->add_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_role_request** | [**AddRoleRequest**](AddRoleRequest.md)|  | [optional] 

### Return type

[**RoleImpl**](RoleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Role successfully added. |  -  |
**400** | A role with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_role**
> RoleImpl change_role(role_id, change_role_request=change_role_request)

Change the role with the given id.

Changes the role with the information that is present in the request.  Only properties that are specified in this request and have not <code>null</code> values are updated.  All other properties are ignored.

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
    api_instance = collibra_core.RolesApi(api_client)
    role_id = 'role_id_example' # str | The unique identifier of the role.
change_role_request = collibra_core.ChangeRoleRequest() # ChangeRoleRequest |  (optional)

    try:
        # Change the role with the given id.
        api_response = api_instance.change_role(role_id, change_role_request=change_role_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->change_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| The unique identifier of the role. | 
 **change_role_request** | [**ChangeRoleRequest**](ChangeRoleRequest.md)|  | [optional] 

### Return type

[**RoleImpl**](RoleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_roles**
> PagedResponseRole find_roles(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, description=description, _global=_global, type=type)

Returns roles matching the given search criteria.

Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned roles satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 roles is returned.

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
    api_instance = collibra_core.RolesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the role to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')
description = 'description_example' # str | The description of the role to search for. (optional)
_global = True # bool | Whether global roles should be searched for. (optional)
type = 'type_example' # str | Indicates which type of roles should be searched for. Usage is mutually exclusive with the deprecated global flag. (optional)

    try:
        # Returns roles matching the given search criteria.
        api_response = api_instance.find_roles(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, description=description, _global=_global, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->find_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the role to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]
 **description** | **str**| The description of the role to search for. | [optional] 
 **_global** | **bool**| Whether global roles should be searched for. | [optional] 
 **type** | **str**| Indicates which type of roles should be searched for. Usage is mutually exclusive with the deprecated global flag. | [optional] 

### Return type

[**PagedResponseRole**](PagedResponseRole.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> RoleImpl get_role(role_id)

Returns the role identified by the given id.

Returns the role identified by the given id.

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
    api_instance = collibra_core.RolesApi(api_client)
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Returns the role identified by the given id.
        api_response = api_instance.get_role(role_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| The unique identifier of the role. | 

### Return type

[**RoleImpl**](RoleImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role**
> remove_role(role_id)

Removes the role identified by the given id.

Removes the role identified by the given id.

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
    api_instance = collibra_core.RolesApi(api_client)
    role_id = 'role_id_example' # str | The unique identifier of the role.

    try:
        # Removes the role identified by the given id.
        api_instance.remove_role(role_id)
    except ApiException as e:
        print("Exception when calling RolesApi->remove_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | [**str**](.md)| The unique identifier of the role. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

