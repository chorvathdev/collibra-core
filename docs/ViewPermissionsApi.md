# collibra_core.ViewPermissionsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_view_permission**](ViewPermissionsApi.md#add_view_permission) | **POST** /viewPermissions | Adds a view permission.
[**find_view_permissions**](ViewPermissionsApi.md#find_view_permissions) | **GET** /viewPermissions | Finds view permissions with given criteria.
[**get_view_permission**](ViewPermissionsApi.md#get_view_permission) | **GET** /viewPermissions/{viewPermissionId} | Retrieves a view permission.
[**remove_view_permission**](ViewPermissionsApi.md#remove_view_permission) | **DELETE** /viewPermissions/{viewPermissionId} | Removes a view permission.


# **add_view_permission**
> ViewPermissionImpl add_view_permission(add_view_permission_request=add_view_permission_request)

Adds a view permission.

Adds a view permission.

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
    api_instance = collibra_core.ViewPermissionsApi(api_client)
    add_view_permission_request = collibra_core.AddViewPermissionRequest() # AddViewPermissionRequest | Properties of the new view permission. (optional)

    try:
        # Adds a view permission.
        api_response = api_instance.add_view_permission(add_view_permission_request=add_view_permission_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ViewPermissionsApi->add_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_view_permission_request** | [**AddViewPermissionRequest**](AddViewPermissionRequest.md)| Properties of the new view permission. | [optional] 

### Return type

[**ViewPermissionImpl**](ViewPermissionImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | View permission successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_view_permissions**
> PagedResponseViewPermission find_view_permissions(offset=offset, limit=limit, user_id=user_id, user_group_id=user_group_id, resource_id=resource_id, resource_type=resource_type, include_inherited=include_inherited)

Finds view permissions with given criteria.

Finds view permissions with given criteria.

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
    api_instance = collibra_core.ViewPermissionsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
user_id = 'user_id_example' # str | The ID of the user for whom the view permission applies. (optional)
user_group_id = 'user_group_id_example' # str | The ID of the user group for whose members the view permission applies. (optional)
resource_id = 'resource_id_example' # str | The ID of the resource to which the view permission applies. (optional)
resource_type = 'resource_type_example' # str | The type of resource addressed by the view permission. (optional)
include_inherited = True # bool | Whether to include inherited permissions in search results. (optional)

    try:
        # Finds view permissions with given criteria.
        api_response = api_instance.find_view_permissions(offset=offset, limit=limit, user_id=user_id, user_group_id=user_group_id, resource_id=resource_id, resource_type=resource_type, include_inherited=include_inherited)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ViewPermissionsApi->find_view_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **user_id** | [**str**](.md)| The ID of the user for whom the view permission applies. | [optional] 
 **user_group_id** | [**str**](.md)| The ID of the user group for whose members the view permission applies. | [optional] 
 **resource_id** | [**str**](.md)| The ID of the resource to which the view permission applies. | [optional] 
 **resource_type** | **str**| The type of resource addressed by the view permission. | [optional] 
 **include_inherited** | **bool**| Whether to include inherited permissions in search results. | [optional] 

### Return type

[**PagedResponseViewPermission**](PagedResponseViewPermission.md)

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

# **get_view_permission**
> ViewPermissionImpl get_view_permission(view_permission_id)

Retrieves a view permission.

Retrieves a view permission.

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
    api_instance = collibra_core.ViewPermissionsApi(api_client)
    view_permission_id = 'view_permission_id_example' # str | Identifier of the view permission to retrieve.

    try:
        # Retrieves a view permission.
        api_response = api_instance.get_view_permission(view_permission_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ViewPermissionsApi->get_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_permission_id** | **str**| Identifier of the view permission to retrieve. | 

### Return type

[**ViewPermissionImpl**](ViewPermissionImpl.md)

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

# **remove_view_permission**
> remove_view_permission(view_permission_id)

Removes a view permission.

Removes a view permission.

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
    api_instance = collibra_core.ViewPermissionsApi(api_client)
    view_permission_id = 'view_permission_id_example' # str | Identifier of the view permission to remove.

    try:
        # Removes a view permission.
        api_instance.remove_view_permission(view_permission_id)
    except ApiException as e:
        print("Exception when calling ViewPermissionsApi->remove_view_permission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_permission_id** | **str**| Identifier of the view permission to remove. | 

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

