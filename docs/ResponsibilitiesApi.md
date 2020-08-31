# collibra_core.ResponsibilitiesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_responsibilities**](ResponsibilitiesApi.md#add_responsibilities) | **POST** /responsibilities/bulk | Adds multiple responsibilities in one go.
[**add_responsibility**](ResponsibilitiesApi.md#add_responsibility) | **POST** /responsibilities | Adds a new responsibility.
[**find_responsibilities**](ResponsibilitiesApi.md#find_responsibilities) | **GET** /responsibilities | Finds responsibilities.
[**get_responsibility**](ResponsibilitiesApi.md#get_responsibility) | **GET** /responsibilities/{responsibilityId} | Returns the responsibility identified by the given id.
[**remove_responsibilities**](ResponsibilitiesApi.md#remove_responsibilities) | **DELETE** /responsibilities/bulk | Removes multiple responsibilities in one go.
[**remove_responsibility**](ResponsibilitiesApi.md#remove_responsibility) | **DELETE** /responsibilities/{responsibilityId} | Removes the responsibility identified by the given id.


# **add_responsibilities**
> list[ResponsibilityImpl] add_responsibilities(add_responsibility_request=add_responsibility_request)

Adds multiple responsibilities in one go.

Adds multiple responsibilities in one go. Assigns the given users to the resources with the given roles.

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
    api_instance = collibra_core.ResponsibilitiesApi(api_client)
    add_responsibility_request = [collibra_core.AddResponsibilityRequest()] # list[AddResponsibilityRequest] |  (optional)

    try:
        # Adds multiple responsibilities in one go.
        api_response = api_instance.add_responsibilities(add_responsibility_request=add_responsibility_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponsibilitiesApi->add_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_responsibility_request** | [**list[AddResponsibilityRequest]**](AddResponsibilityRequest.md)|  | [optional] 

### Return type

[**list[ResponsibilityImpl]**](ResponsibilityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Responsibilities successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_responsibility**
> ResponsibilityImpl add_responsibility(add_responsibility_request=add_responsibility_request)

Adds a new responsibility.

Adds new responsibility. Assigns given user to resource with given role.

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
    api_instance = collibra_core.ResponsibilitiesApi(api_client)
    add_responsibility_request = collibra_core.AddResponsibilityRequest() # AddResponsibilityRequest |  (optional)

    try:
        # Adds a new responsibility.
        api_response = api_instance.add_responsibility(add_responsibility_request=add_responsibility_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponsibilitiesApi->add_responsibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_responsibility_request** | [**AddResponsibilityRequest**](AddResponsibilityRequest.md)|  | [optional] 

### Return type

[**ResponsibilityImpl**](ResponsibilityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Responsibility successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_responsibilities**
> PagedResponseResponsibility find_responsibilities(offset=offset, limit=limit, resource_ids=resource_ids, owner_ids=owner_ids, role_ids=role_ids, include_inherited=include_inherited, global_only=global_only, sort_field=sort_field, sort_order=sort_order, type=type)

Finds responsibilities.

Returns responsibilities matching the given search criteria.  Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned responsibilities satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 responsibilities is returned.

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
    api_instance = collibra_core.ResponsibilitiesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
resource_ids = ['resource_ids_example'] # list[str] | The list of IDs of the resources for which the responsibilities should be found. (optional)
owner_ids = ['owner_ids_example'] # list[str] | The list of IDs of the owners for which the responsibilities should be found. (optional)
role_ids = ['role_ids_example'] # list[str] | The list of IDs of the roles for which the responsibilities should be found. (optional)
include_inherited = True # bool | Whether inherited responsibilities should be included in the search results. (optional) (default to True)
global_only = True # bool | Whether only global responsibilities should be searched. (optional)
sort_field = 'LAST_MODIFIED' # str | The field that should be used as reference for sorting. (optional) (default to 'LAST_MODIFIED')
sort_order = 'DESC' # str | The order of sorting. (optional) (default to 'DESC')
type = 'type_example' # str | Indicates which type of responsibilities should be searched for. Usage is mutually exclusive with the deprecated globalOnly flag. (optional)

    try:
        # Finds responsibilities.
        api_response = api_instance.find_responsibilities(offset=offset, limit=limit, resource_ids=resource_ids, owner_ids=owner_ids, role_ids=role_ids, include_inherited=include_inherited, global_only=global_only, sort_field=sort_field, sort_order=sort_order, type=type)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponsibilitiesApi->find_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **resource_ids** | [**list[str]**](str.md)| The list of IDs of the resources for which the responsibilities should be found. | [optional] 
 **owner_ids** | [**list[str]**](str.md)| The list of IDs of the owners for which the responsibilities should be found. | [optional] 
 **role_ids** | [**list[str]**](str.md)| The list of IDs of the roles for which the responsibilities should be found. | [optional] 
 **include_inherited** | **bool**| Whether inherited responsibilities should be included in the search results. | [optional] [default to True]
 **global_only** | **bool**| Whether only global responsibilities should be searched. | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to &#39;LAST_MODIFIED&#39;]
 **sort_order** | **str**| The order of sorting. | [optional] [default to &#39;DESC&#39;]
 **type** | **str**| Indicates which type of responsibilities should be searched for. Usage is mutually exclusive with the deprecated globalOnly flag. | [optional] 

### Return type

[**PagedResponseResponsibility**](PagedResponseResponsibility.md)

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

# **get_responsibility**
> ResponsibilityImpl get_responsibility(responsibility_id)

Returns the responsibility identified by the given id.

Returns the responsibility identified by the given id.

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
    api_instance = collibra_core.ResponsibilitiesApi(api_client)
    responsibility_id = 'responsibility_id_example' # str | The unique identifier of the responsibility.

    try:
        # Returns the responsibility identified by the given id.
        api_response = api_instance.get_responsibility(responsibility_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ResponsibilitiesApi->get_responsibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responsibility_id** | [**str**](.md)| The unique identifier of the responsibility. | 

### Return type

[**ResponsibilityImpl**](ResponsibilityImpl.md)

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

# **remove_responsibilities**
> remove_responsibilities(request_body=request_body)

Removes multiple responsibilities in one go.

Removes multiple responsibilities in one go identified by given ids.

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
    api_instance = collibra_core.ResponsibilitiesApi(api_client)
    request_body = ['request_body_example'] # list[str] | The unique identifiers of the responsibilities. (optional)

    try:
        # Removes multiple responsibilities in one go.
        api_instance.remove_responsibilities(request_body=request_body)
    except ApiException as e:
        print("Exception when calling ResponsibilitiesApi->remove_responsibilities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| The unique identifiers of the responsibilities. | [optional] 

### Return type

void (empty response body)

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

# **remove_responsibility**
> remove_responsibility(responsibility_id)

Removes the responsibility identified by the given id.

Removes the responsibility identified by the given id.

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
    api_instance = collibra_core.ResponsibilitiesApi(api_client)
    responsibility_id = 'responsibility_id_example' # str | The unique identifier of the responsibility.

    try:
        # Removes the responsibility identified by the given id.
        api_instance.remove_responsibility(responsibility_id)
    except ApiException as e:
        print("Exception when calling ResponsibilitiesApi->remove_responsibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **responsibility_id** | [**str**](.md)| The unique identifier of the responsibility. | 

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

