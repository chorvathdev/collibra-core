# collibra_core.StatusesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_status**](StatusesApi.md#add_status) | **POST** /statuses | Adds a new Status.
[**add_statuses**](StatusesApi.md#add_statuses) | **POST** /statuses/bulk | Adds multiple statuses in one go.
[**change_status**](StatusesApi.md#change_status) | **PATCH** /statuses/{statusId} | Changes the status with the information that is present in the request.
[**change_statuses**](StatusesApi.md#change_statuses) | **PATCH** /statuses/bulk | Changes multiple statuses in one go.
[**find_statuses**](StatusesApi.md#find_statuses) | **GET** /statuses | Returns statuses matching the given search criteria.
[**get_status**](StatusesApi.md#get_status) | **GET** /statuses/{statusId} | Returns the Status identified by the given id.
[**get_status_by_name**](StatusesApi.md#get_status_by_name) | **GET** /statuses/name/{statusName} | Returns the Status identified by the given name.
[**remove_status**](StatusesApi.md#remove_status) | **DELETE** /statuses/{statusId} | Removes the Status identified by the given id.
[**remove_statuses**](StatusesApi.md#remove_statuses) | **DELETE** /statuses/bulk | Removes multiple statuses.


# **add_status**
> StatusImpl add_status(add_status_request=add_status_request)

Adds a new Status.

Adds a new Status.

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
    api_instance = collibra_core.StatusesApi(api_client)
    add_status_request = collibra_core.AddStatusRequest() # AddStatusRequest |  (optional)

    try:
        # Adds a new Status.
        api_response = api_instance.add_status(add_status_request=add_status_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->add_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_status_request** | [**AddStatusRequest**](AddStatusRequest.md)|  | [optional] 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Status successfully added. |  -  |
**400** | A status with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_statuses**
> list[StatusImpl] add_statuses(add_status_request=add_status_request)

Adds multiple statuses in one go.

Adds multiple statuses in one go.

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
    api_instance = collibra_core.StatusesApi(api_client)
    add_status_request = [collibra_core.AddStatusRequest()] # list[AddStatusRequest] |  (optional)

    try:
        # Adds multiple statuses in one go.
        api_response = api_instance.add_statuses(add_status_request=add_status_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->add_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_status_request** | [**list[AddStatusRequest]**](AddStatusRequest.md)|  | [optional] 

### Return type

[**list[StatusImpl]**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Statuses successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_status**
> StatusImpl change_status(status_id, change_status_request=change_status_request)

Changes the status with the information that is present in the request.

Changes the status with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.StatusesApi(api_client)
    status_id = 'status_id_example' # str | The unique identifier of the status.
change_status_request = collibra_core.ChangeStatusRequest() # ChangeStatusRequest |  (optional)

    try:
        # Changes the status with the information that is present in the request.
        api_response = api_instance.change_status(status_id, change_status_request=change_status_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->change_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | [**str**](.md)| The unique identifier of the status. | 
 **change_status_request** | [**ChangeStatusRequest**](ChangeStatusRequest.md)|  | [optional] 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuses were successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_statuses**
> list[StatusImpl] change_statuses(change_status_request=change_status_request)

Changes multiple statuses in one go.

Changes multiple statuses in one go.

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
    api_instance = collibra_core.StatusesApi(api_client)
    change_status_request = [collibra_core.ChangeStatusRequest()] # list[ChangeStatusRequest] |  (optional)

    try:
        # Changes multiple statuses in one go.
        api_response = api_instance.change_statuses(change_status_request=change_status_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->change_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_status_request** | [**list[ChangeStatusRequest]**](ChangeStatusRequest.md)|  | [optional] 

### Return type

[**list[StatusImpl]**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Statuses were successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_statuses**
> StatusPagedResponse find_statuses(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, description=description)

Returns statuses matching the given search criteria.

Returns statuses matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned statuses satisfy all constraints that are specified in this search criteria. By default a result containing 1000 statuses is returned. 

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
    api_instance = collibra_core.StatusesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the status to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')
description = 'description_example' # str | The description of the status to search for. (optional)

    try:
        # Returns statuses matching the given search criteria.
        api_response = api_instance.find_statuses(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, description=description)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->find_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the status to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]
 **description** | **str**| The description of the status to search for. | [optional] 

### Return type

[**StatusPagedResponse**](StatusPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found Status information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status**
> StatusImpl get_status(status_id)

Returns the Status identified by the given id.

Returns the Status identified by the given id.

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
    api_instance = collibra_core.StatusesApi(api_client)
    status_id = 'status_id_example' # str | The <code>id</code> of the Status

    try:
        # Returns the Status identified by the given id.
        api_response = api_instance.get_status(status_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->get_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | [**str**](.md)| The &lt;code&gt;id&lt;/code&gt; of the Status | 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status found. |  -  |
**404** | Status not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_by_name**
> StatusImpl get_status_by_name(status_name)

Returns the Status identified by the given name.

Returns the Status identified by the given name.

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
    api_instance = collibra_core.StatusesApi(api_client)
    status_name = 'status_name_example' # str | The name that identifies the Status.

    try:
        # Returns the Status identified by the given name.
        api_response = api_instance.get_status_by_name(status_name)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling StatusesApi->get_status_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_name** | **str**| The name that identifies the Status. | 

### Return type

[**StatusImpl**](StatusImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Status found. |  -  |
**404** | Status not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_status**
> remove_status(status_id)

Removes the Status identified by the given id.

Removes the Status identified by the given id.

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
    api_instance = collibra_core.StatusesApi(api_client)
    status_id = 'status_id_example' # str | The <code>id</code> of the Status.

    try:
        # Removes the Status identified by the given id.
        api_instance.remove_status(status_id)
    except ApiException as e:
        print("Exception when calling StatusesApi->remove_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status_id** | [**str**](.md)| The &lt;code&gt;id&lt;/code&gt; of the Status. | 

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
**200** | Status removed. |  -  |
**404** | Status not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_statuses**
> remove_statuses(request_body=request_body)

Removes multiple statuses.

Removes multiple statuses.

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
    api_instance = collibra_core.StatusesApi(api_client)
    request_body = ['request_body_example'] # list[str] | The indentifiers of the Statuses. (optional)

    try:
        # Removes multiple statuses.
        api_instance.remove_statuses(request_body=request_body)
    except ApiException as e:
        print("Exception when calling StatusesApi->remove_statuses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| The indentifiers of the Statuses. | [optional] 

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
**200** | Statuses removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

