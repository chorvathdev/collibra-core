# collibra_core.ComplexRelationTypesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_complex_relation_type**](ComplexRelationTypesApi.md#add_complex_relation_type) | **POST** /complexRelationTypes | Adds a new complex relation type.
[**change_complex_relation_type**](ComplexRelationTypesApi.md#change_complex_relation_type) | **PATCH** /complexRelationTypes/{complexRelationTypeId} | Changes the complex relation type.
[**find_complex_relation_types**](ComplexRelationTypesApi.md#find_complex_relation_types) | **GET** /complexRelationTypes | Returns complex relation types matching the given search criteria.
[**get_complex_relation_type**](ComplexRelationTypesApi.md#get_complex_relation_type) | **GET** /complexRelationTypes/{complexRelationTypeId} | Returns complex relation type identified by given UUID.
[**remove_complex_relation_type**](ComplexRelationTypesApi.md#remove_complex_relation_type) | **DELETE** /complexRelationTypes/{complexRelationTypeId} | Removes complex relation type identified by given UUID.


# **add_complex_relation_type**
> ComplexRelationTypeImpl add_complex_relation_type(add_complex_relation_type_request=add_complex_relation_type_request)

Adds a new complex relation type.

Adds a new complex relation type.

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
    api_instance = collibra_core.ComplexRelationTypesApi(api_client)
    add_complex_relation_type_request = collibra_core.AddComplexRelationTypeRequest() # AddComplexRelationTypeRequest |  (optional)

    try:
        # Adds a new complex relation type.
        api_response = api_instance.add_complex_relation_type(add_complex_relation_type_request=add_complex_relation_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationTypesApi->add_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_complex_relation_type_request** | [**AddComplexRelationTypeRequest**](AddComplexRelationTypeRequest.md)|  | [optional] 

### Return type

[**ComplexRelationTypeImpl**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Complex relation type successfully added. |  -  |
**400** | A complex relation type with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_complex_relation_type**
> ComplexRelationTypeImpl change_complex_relation_type(complex_relation_type_id, change_complex_relation_type_request=change_complex_relation_type_request)

Changes the complex relation type.

Changes the complex relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.ComplexRelationTypesApi(api_client)
    complex_relation_type_id = 'complex_relation_type_id_example' # str | the unique identifier of the complex relation type
change_complex_relation_type_request = collibra_core.ChangeComplexRelationTypeRequest() # ChangeComplexRelationTypeRequest |  (optional)

    try:
        # Changes the complex relation type.
        api_response = api_instance.change_complex_relation_type(complex_relation_type_id, change_complex_relation_type_request=change_complex_relation_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationTypesApi->change_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | [**str**](.md)| the unique identifier of the complex relation type | 
 **change_complex_relation_type_request** | [**ChangeComplexRelationTypeRequest**](ChangeComplexRelationTypeRequest.md)|  | [optional] 

### Return type

[**ComplexRelationTypeImpl**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complex relation type successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_complex_relation_types**
> ComplexRelationTypePagedResponse find_complex_relation_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode)

Returns complex relation types matching the given search criteria.

Returns complex relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned complex relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 complex relation types is returned.

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
    api_instance = collibra_core.ComplexRelationTypesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the complex relation type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')

    try:
        # Returns complex relation types matching the given search criteria.
        api_response = api_instance.find_complex_relation_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationTypesApi->find_complex_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the complex relation type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]

### Return type

[**ComplexRelationTypePagedResponse**](ComplexRelationTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response of found Complex Relation Types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_complex_relation_type**
> ComplexRelationTypeImpl get_complex_relation_type(complex_relation_type_id)

Returns complex relation type identified by given UUID.

Returns complex relation type identified by given UUID.

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
    api_instance = collibra_core.ComplexRelationTypesApi(api_client)
    complex_relation_type_id = 'complex_relation_type_id_example' # str | the unique identifier of the complex relation type

    try:
        # Returns complex relation type identified by given UUID.
        api_response = api_instance.get_complex_relation_type(complex_relation_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationTypesApi->get_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | [**str**](.md)| the unique identifier of the complex relation type | 

### Return type

[**ComplexRelationTypeImpl**](ComplexRelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Complex relation type found. |  -  |
**404** | Complex relation type not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_complex_relation_type**
> remove_complex_relation_type(complex_relation_type_id)

Removes complex relation type identified by given UUID.

Removes complex relation type identified by given UUID.

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
    api_instance = collibra_core.ComplexRelationTypesApi(api_client)
    complex_relation_type_id = 'complex_relation_type_id_example' # str | the unique identifier of the complex relation type

    try:
        # Removes complex relation type identified by given UUID.
        api_instance.remove_complex_relation_type(complex_relation_type_id)
    except ApiException as e:
        print("Exception when calling ComplexRelationTypesApi->remove_complex_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_type_id** | [**str**](.md)| the unique identifier of the complex relation type | 

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

