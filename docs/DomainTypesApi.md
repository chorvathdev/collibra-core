# collibra_core.DomainTypesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain_type**](DomainTypesApi.md#add_domain_type) | **POST** /domainTypes | Adds a new domain type.
[**add_domain_types**](DomainTypesApi.md#add_domain_types) | **POST** /domainTypes/bulk | Adds multiple new domain types.
[**change_domain_type**](DomainTypesApi.md#change_domain_type) | **PATCH** /domainTypes/{domainTypeId} | Changes the domain type.
[**change_domain_types**](DomainTypesApi.md#change_domain_types) | **PATCH** /domainTypes/bulk | Changes the domain types.
[**find_domain_types**](DomainTypesApi.md#find_domain_types) | **GET** /domainTypes | Returns domain types matching the given search criteria.
[**find_sub_domain_types**](DomainTypesApi.md#find_sub_domain_types) | **GET** /domainTypes/{domainTypeId}/subTypes | Returns sub domain types matching the given search criteria.
[**get_domain_type**](DomainTypesApi.md#get_domain_type) | **GET** /domainTypes/{domainTypeId} | Returns domain type identified by given UUID.
[**remove_domain_type**](DomainTypesApi.md#remove_domain_type) | **DELETE** /domainTypes/{domainTypeId} | Removes domain type identified by given UUID.
[**remove_domain_types**](DomainTypesApi.md#remove_domain_types) | **DELETE** /domainTypes/bulk | Removes multiple domain types.


# **add_domain_type**
> DomainTypeImpl add_domain_type(add_domain_type_request=add_domain_type_request)

Adds a new domain type.

Adds a new domain type.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    add_domain_type_request = collibra_core.AddDomainTypeRequest() # AddDomainTypeRequest |  (optional)

    try:
        # Adds a new domain type.
        api_response = api_instance.add_domain_type(add_domain_type_request=add_domain_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->add_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_domain_type_request** | [**AddDomainTypeRequest**](AddDomainTypeRequest.md)|  | [optional] 

### Return type

[**DomainTypeImpl**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain type successfully added. |  -  |
**400** | A domain type with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domain_types**
> list[DomainTypeImpl] add_domain_types(add_domain_type_request=add_domain_type_request)

Adds multiple new domain types.

Adds multiple new domain types.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    add_domain_type_request = [collibra_core.AddDomainTypeRequest()] # list[AddDomainTypeRequest] |  (optional)

    try:
        # Adds multiple new domain types.
        api_response = api_instance.add_domain_types(add_domain_type_request=add_domain_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->add_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_domain_type_request** | [**list[AddDomainTypeRequest]**](AddDomainTypeRequest.md)|  | [optional] 

### Return type

[**list[DomainTypeImpl]**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain types successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain_type**
> DomainTypeImpl change_domain_type(domain_type_id, change_domain_type_request=change_domain_type_request)

Changes the domain type.

Changes the domain type with the information present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored. 

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    domain_type_id = 'domain_type_id_example' # str | the unique identifier of the domain type
change_domain_type_request = collibra_core.ChangeDomainTypeRequest() # ChangeDomainTypeRequest |  (optional)

    try:
        # Changes the domain type.
        api_response = api_instance.change_domain_type(domain_type_id, change_domain_type_request=change_domain_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->change_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 
 **change_domain_type_request** | [**ChangeDomainTypeRequest**](ChangeDomainTypeRequest.md)|  | [optional] 

### Return type

[**DomainTypeImpl**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain type successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain_types**
> list[DomainTypeImpl] change_domain_types(change_domain_type_request=change_domain_type_request)

Changes the domain types.

Changes the domain types with the information present in the request.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    change_domain_type_request = [collibra_core.ChangeDomainTypeRequest()] # list[ChangeDomainTypeRequest] |  (optional)

    try:
        # Changes the domain types.
        api_response = api_instance.change_domain_types(change_domain_type_request=change_domain_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->change_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_domain_type_request** | [**list[ChangeDomainTypeRequest]**](ChangeDomainTypeRequest.md)|  | [optional] 

### Return type

[**list[DomainTypeImpl]**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain types successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_domain_types**
> DomainTypePagedResponse find_domain_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, top_level=top_level)

Returns domain types matching the given search criteria.

Returns domain types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned domain types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 domain types is returned.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the domain type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')
parent_id = 'parent_id_example' # str | The ID of the parent to find the domain types in. (optional)
exclude_meta = True # bool | Whether the meta domain types should be excluded from search or not. (optional) (default to True)
top_level = False # bool | Whether only top level domain types should be searched or not. (optional) (default to False)

    try:
        # Returns domain types matching the given search criteria.
        api_response = api_instance.find_domain_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, top_level=top_level)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->find_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the domain type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]
 **parent_id** | [**str**](.md)| The ID of the parent to find the domain types in. | [optional] 
 **exclude_meta** | **bool**| Whether the meta domain types should be excluded from search or not. | [optional] [default to True]
 **top_level** | **bool**| Whether only top level domain types should be searched or not. | [optional] [default to False]

### Return type

[**DomainTypePagedResponse**](DomainTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response of found Domain types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sub_domain_types**
> DomainTypePagedResponse find_sub_domain_types(domain_type_id, domain_type_id2, include_parent=include_parent)

Returns sub domain types matching the given search criteria.

Returns sub domain types matching the given search criteria.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    domain_type_id = 'domain_type_id_example' # str | the unique identifier of the domain type
domain_type_id2 = 'domain_type_id_example' # str | The ID of the domain type to search the sub types for.
include_parent = True # bool | Whether parent domain type should be included in the search result. (optional)

    try:
        # Returns sub domain types matching the given search criteria.
        api_response = api_instance.find_sub_domain_types(domain_type_id, domain_type_id2, include_parent=include_parent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->find_sub_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 
 **domain_type_id2** | [**str**](.md)| The ID of the domain type to search the sub types for. | 
 **include_parent** | **bool**| Whether parent domain type should be included in the search result. | [optional] 

### Return type

[**DomainTypePagedResponse**](DomainTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response of found sub Domain types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_type**
> DomainTypeImpl get_domain_type(domain_type_id)

Returns domain type identified by given UUID.

Returns domain type identified by given UUID.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    domain_type_id = 'domain_type_id_example' # str | the unique identifier of the domain type

    try:
        # Returns domain type identified by given UUID.
        api_response = api_instance.get_domain_type(domain_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->get_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 

### Return type

[**DomainTypeImpl**](DomainTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain Type found. |  -  |
**404** | Domain Type not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain_type**
> remove_domain_type(domain_type_id)

Removes domain type identified by given UUID.

Removes domain type identified by given UUID.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    domain_type_id = 'domain_type_id_example' # str | the unique identifier of the domain type

    try:
        # Removes domain type identified by given UUID.
        api_instance.remove_domain_type(domain_type_id)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->remove_domain_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_type_id** | [**str**](.md)| the unique identifier of the domain type | 

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

# **remove_domain_types**
> remove_domain_types(request_body=request_body)

Removes multiple domain types.

Removes multiple domain types identified by the UUIDs passed as parameter.

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
    api_instance = collibra_core.DomainTypesApi(api_client)
    request_body = ['request_body_example'] # list[str] |  (optional)

    try:
        # Removes multiple domain types.
        api_instance.remove_domain_types(request_body=request_body)
    except ApiException as e:
        print("Exception when calling DomainTypesApi->remove_domain_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)|  | [optional] 

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

