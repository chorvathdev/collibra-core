# collibra_core.ScopesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_scope**](ScopesApi.md#add_scope) | **POST** /scopes | Add scope
[**change_scope**](ScopesApi.md#change_scope) | **PATCH** /scopes/{scopeId} | Change scope
[**get_all_scopes**](ScopesApi.md#get_all_scopes) | **GET** /scopes | Find scopes
[**get_scope**](ScopesApi.md#get_scope) | **GET** /scopes/{scopeId} | Get scope
[**remove_scope**](ScopesApi.md#remove_scope) | **DELETE** /scopes/{scopeId} | Remove scope


# **add_scope**
> ScopeImpl add_scope(add_scope_request=add_scope_request)

Add scope

Adds a new scope.

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
    api_instance = collibra_core.ScopesApi(api_client)
    add_scope_request = collibra_core.AddScopeRequest() # AddScopeRequest | the properties of the scope to be added (optional)

    try:
        # Add scope
        api_response = api_instance.add_scope(add_scope_request=add_scope_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopesApi->add_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_scope_request** | [**AddScopeRequest**](AddScopeRequest.md)| the properties of the scope to be added | [optional] 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Scope successfully added. |  -  |
**400** | A scope with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_scope**
> ScopeImpl change_scope(scope_id, change_scope_request=change_scope_request)

Change scope

Changes the scope with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.ScopesApi(api_client)
    scope_id = 'scope_id_example' # str | the id of the scope to be changed
change_scope_request = collibra_core.ChangeScopeRequest() # ChangeScopeRequest | the properties of the scope to be changed (optional)

    try:
        # Change scope
        api_response = api_instance.change_scope(scope_id, change_scope_request=change_scope_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopesApi->change_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | [**str**](.md)| the id of the scope to be changed | 
 **change_scope_request** | [**ChangeScopeRequest**](ChangeScopeRequest.md)| the properties of the scope to be changed | [optional] 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_scopes**
> ScopePagedResponse get_all_scopes()

Find scopes

Returns all scopes.

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
    api_instance = collibra_core.ScopesApi(api_client)
    
    try:
        # Find scopes
        api_response = api_instance.get_all_scopes()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopesApi->get_all_scopes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ScopePagedResponse**](ScopePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found scopes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scope**
> ScopeImpl get_scope(scope_id)

Get scope

Returns scope identified by given id.

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
    api_instance = collibra_core.ScopesApi(api_client)
    scope_id = 'scope_id_example' # str | The unique identifier of the scope.

    try:
        # Get scope
        api_response = api_instance.get_scope(scope_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ScopesApi->get_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | [**str**](.md)| The unique identifier of the scope. | 

### Return type

[**ScopeImpl**](ScopeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found scope |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_scope**
> remove_scope(scope_id)

Remove scope

Removes scope identified by given id.

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
    api_instance = collibra_core.ScopesApi(api_client)
    scope_id = 'scope_id_example' # str | the id of the scope

    try:
        # Remove scope
        api_instance.remove_scope(scope_id)
    except ApiException as e:
        print("Exception when calling ScopesApi->remove_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scope_id** | [**str**](.md)| the id of the scope | 

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
**204** | The scope has been successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

