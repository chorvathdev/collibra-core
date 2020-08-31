# collibra_core.RelationTypesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation_type**](RelationTypesApi.md#add_relation_type) | **POST** /relationTypes | Adds a new relation type.
[**add_relation_types**](RelationTypesApi.md#add_relation_types) | **POST** /relationTypes/bulk | Adds multiple new relation type.
[**change_relation_type**](RelationTypesApi.md#change_relation_type) | **PATCH** /relationTypes/{relationTypeId} | Changes the relation type.
[**change_relation_types**](RelationTypesApi.md#change_relation_types) | **PATCH** /relationTypes/bulk | Changes the relation types.
[**find_relation_types**](RelationTypesApi.md#find_relation_types) | **GET** /relationTypes | Finds all the relation types matching the given criteria.
[**get_relation_type**](RelationTypesApi.md#get_relation_type) | **GET** /relationTypes/{relationTypeId} | Returns relation type identified by given UUID.
[**remove_relation_type**](RelationTypesApi.md#remove_relation_type) | **DELETE** /relationTypes/{relationTypeId} | Removes relation type identified by given UUID.
[**remove_relation_types**](RelationTypesApi.md#remove_relation_types) | **DELETE** /relationTypes/bulk | Removes multiple relation types.


# **add_relation_type**
> RelationTypeImpl add_relation_type(add_relation_type_request=add_relation_type_request)

Adds a new relation type.

Adds a new relation type.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    add_relation_type_request = collibra_core.AddRelationTypeRequest() # AddRelationTypeRequest |  (optional)

    try:
        # Adds a new relation type.
        api_response = api_instance.add_relation_type(add_relation_type_request=add_relation_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->add_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_relation_type_request** | [**AddRelationTypeRequest**](AddRelationTypeRequest.md)|  | [optional] 

### Return type

[**RelationTypeImpl**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Relation type successfully added. |  -  |
**400** | A relation type with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_relation_types**
> list[RelationTypeImpl] add_relation_types(add_relation_type_request=add_relation_type_request)

Adds multiple new relation type.

Adds multiple new relation type.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    add_relation_type_request = [collibra_core.AddRelationTypeRequest()] # list[AddRelationTypeRequest] |  (optional)

    try:
        # Adds multiple new relation type.
        api_response = api_instance.add_relation_types(add_relation_type_request=add_relation_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->add_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_relation_type_request** | [**list[AddRelationTypeRequest]**](AddRelationTypeRequest.md)|  | [optional] 

### Return type

[**list[RelationTypeImpl]**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Relation types successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relation_type**
> RelationTypeImpl change_relation_type(relation_type_id, change_relation_type_request=change_relation_type_request)

Changes the relation type.

Changes the relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    relation_type_id = 'relation_type_id_example' # str | The unique identifier of the relationType
change_relation_type_request = collibra_core.ChangeRelationTypeRequest() # ChangeRelationTypeRequest |  (optional)

    try:
        # Changes the relation type.
        api_response = api_instance.change_relation_type(relation_type_id, change_relation_type_request=change_relation_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->change_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | [**str**](.md)| The unique identifier of the relationType | 
 **change_relation_type_request** | [**ChangeRelationTypeRequest**](ChangeRelationTypeRequest.md)|  | [optional] 

### Return type

[**RelationTypeImpl**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relation type successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relation_types**
> list[RelationTypeImpl] change_relation_types(change_relation_type_request=change_relation_type_request)

Changes the relation types.

Changes the relation types with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    change_relation_type_request = [collibra_core.ChangeRelationTypeRequest()] # list[ChangeRelationTypeRequest] |  (optional)

    try:
        # Changes the relation types.
        api_response = api_instance.change_relation_types(change_relation_type_request=change_relation_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->change_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_relation_type_request** | [**list[ChangeRelationTypeRequest]**](ChangeRelationTypeRequest.md)|  | [optional] 

### Return type

[**list[RelationTypeImpl]**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relation types successfully changed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_relation_types**
> RelationTypePagedResponse find_relation_types(offset=offset, limit=limit, source_type_id=source_type_id, source_type_name=source_type_name, role=role, target_type_id=target_type_id, target_type_name=target_type_name, co_role=co_role, sort_field=sort_field, sort_order=sort_order, role_co_role_logical_operator=role_co_role_logical_operator)

Finds all the relation types matching the given criteria.

Returns relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relation types is returned. 

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
source_type_id = 'source_type_id_example' # str | The ID of the source type of the relation type to search for. (optional)
source_type_name = 'source_type_name_example' # str | The name of the source type of the relation type to search for. (optional)
role = 'role_example' # str | The name of the role that the source plays to search for. (optional)
target_type_id = 'target_type_id_example' # str | The ID of the target type of the relation type to search for. (optional)
target_type_name = 'target_type_name_example' # str | The name of the target type of the relation type to search for. (optional)
co_role = 'co_role_example' # str | The name of the role that the target plays to search for. (optional)
sort_field = 'ROLE' # str | The field that should be used as reference for sorting. (optional) (default to 'ROLE')
sort_order = 'ASC' # str | The order of sorting. (optional) (default to 'ASC')
role_co_role_logical_operator = 'AND' # str | The logical operator determining how to combine the role and coRole criteria: AND or OR. (optional) (default to 'AND')

    try:
        # Finds all the relation types matching the given criteria.
        api_response = api_instance.find_relation_types(offset=offset, limit=limit, source_type_id=source_type_id, source_type_name=source_type_name, role=role, target_type_id=target_type_id, target_type_name=target_type_name, co_role=co_role, sort_field=sort_field, sort_order=sort_order, role_co_role_logical_operator=role_co_role_logical_operator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->find_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **source_type_id** | [**str**](.md)| The ID of the source type of the relation type to search for. | [optional] 
 **source_type_name** | **str**| The name of the source type of the relation type to search for. | [optional] 
 **role** | **str**| The name of the role that the source plays to search for. | [optional] 
 **target_type_id** | [**str**](.md)| The ID of the target type of the relation type to search for. | [optional] 
 **target_type_name** | **str**| The name of the target type of the relation type to search for. | [optional] 
 **co_role** | **str**| The name of the role that the target plays to search for. | [optional] 
 **sort_field** | **str**| The field that should be used as reference for sorting. | [optional] [default to &#39;ROLE&#39;]
 **sort_order** | **str**| The order of sorting. | [optional] [default to &#39;ASC&#39;]
 **role_co_role_logical_operator** | **str**| The logical operator determining how to combine the role and coRole criteria: AND or OR. | [optional] [default to &#39;AND&#39;]

### Return type

[**RelationTypePagedResponse**](RelationTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response of found Relation types. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation_type**
> RelationTypeImpl get_relation_type(relation_type_id)

Returns relation type identified by given UUID.

Returns relation type identified by given UUID.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    relation_type_id = 'relation_type_id_example' # str | The unique identifier of the relationType

    try:
        # Returns relation type identified by given UUID.
        api_response = api_instance.get_relation_type(relation_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->get_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | [**str**](.md)| The unique identifier of the relationType | 

### Return type

[**RelationTypeImpl**](RelationTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Relation Type found. |  -  |
**404** | Relation Type not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relation_type**
> remove_relation_type(relation_type_id)

Removes relation type identified by given UUID.

Removes relation type identified by given UUID.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    relation_type_id = 'relation_type_id_example' # str | The unique identifier of the relationType

    try:
        # Removes relation type identified by given UUID.
        api_instance.remove_relation_type(relation_type_id)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->remove_relation_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_type_id** | [**str**](.md)| The unique identifier of the relationType | 

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

# **remove_relation_types**
> remove_relation_types(request_body=request_body)

Removes multiple relation types.

Removes multiple relation types identified by the UUIDs passed as parameter.

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
    api_instance = collibra_core.RelationTypesApi(api_client)
    request_body = ['request_body_example'] # list[str] | The unique identifiers of the relationTypes (optional)

    try:
        # Removes multiple relation types.
        api_instance.remove_relation_types(request_body=request_body)
    except ApiException as e:
        print("Exception when calling RelationTypesApi->remove_relation_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| The unique identifiers of the relationTypes | [optional] 

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

