# collibra_core.RelationsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_relation**](RelationsApi.md#add_relation) | **POST** /relations | Adds a new relation.
[**add_relations**](RelationsApi.md#add_relations) | **POST** /relations/bulk | Adds multiple relations in one go.
[**change_relation**](RelationsApi.md#change_relation) | **PATCH** /relations/{relationId} | Changes the relation with the information that is present in the request.
[**change_relations**](RelationsApi.md#change_relations) | **PATCH** /relations/bulk | Changes multiple relations.
[**find_relations**](RelationsApi.md#find_relations) | **GET** /relations | Returns relations matching the given search criteria.
[**get_relation**](RelationsApi.md#get_relation) | **GET** /relations/{relationId} | Returns a relation identified by given id.
[**remove_relation**](RelationsApi.md#remove_relation) | **DELETE** /relations/{relationId} | Removes a relation identified by given id.
[**remove_relation1**](RelationsApi.md#remove_relation1) | **DELETE** /relations/bulk | Removes multiple relations.


# **add_relation**
> RelationImpl add_relation(add_relation_request=add_relation_request)

Adds a new relation.

Adds a new relation.

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
    api_instance = collibra_core.RelationsApi(api_client)
    add_relation_request = collibra_core.AddRelationRequest() # AddRelationRequest | The properties of the relation to be added (optional)

    try:
        # Adds a new relation.
        api_response = api_instance.add_relation(add_relation_request=add_relation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationsApi->add_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_relation_request** | [**AddRelationRequest**](AddRelationRequest.md)| The properties of the relation to be added | [optional] 

### Return type

[**RelationImpl**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Relation successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_relations**
> list[RelationImpl] add_relations(add_relation_request=add_relation_request)

Adds multiple relations in one go.

Adds multiple relations in one gos.

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
    api_instance = collibra_core.RelationsApi(api_client)
    add_relation_request = [collibra_core.AddRelationRequest()] # list[AddRelationRequest] | List of the properties of the relations to be added. (optional)

    try:
        # Adds multiple relations in one go.
        api_response = api_instance.add_relations(add_relation_request=add_relation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationsApi->add_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_relation_request** | [**list[AddRelationRequest]**](AddRelationRequest.md)| List of the properties of the relations to be added. | [optional] 

### Return type

[**list[RelationImpl]**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Relations successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relation**
> RelationImpl change_relation(relation_id, change_relation_request=change_relation_request)

Changes the relation with the information that is present in the request.

Changes the relation with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.RelationsApi(api_client)
    relation_id = 'relation_id_example' # str | The ID of the relation to be changed.
change_relation_request = collibra_core.ChangeRelationRequest() # ChangeRelationRequest | The properties of the relation to be changed. (optional)

    try:
        # Changes the relation with the information that is present in the request.
        api_response = api_instance.change_relation(relation_id, change_relation_request=change_relation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationsApi->change_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | [**str**](.md)| The ID of the relation to be changed. | 
 **change_relation_request** | [**ChangeRelationRequest**](ChangeRelationRequest.md)| The properties of the relation to be changed. | [optional] 

### Return type

[**RelationImpl**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The changed relation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_relations**
> list[RelationImpl] change_relations(change_relation_request=change_relation_request)

Changes multiple relations.

Changes multiple relations.

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
    api_instance = collibra_core.RelationsApi(api_client)
    change_relation_request = [collibra_core.ChangeRelationRequest()] # list[ChangeRelationRequest] | The list of properties of the relations to be changed. (optional)

    try:
        # Changes multiple relations.
        api_response = api_instance.change_relations(change_relation_request=change_relation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationsApi->change_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_relation_request** | [**list[ChangeRelationRequest]**](ChangeRelationRequest.md)| The list of properties of the relations to be changed. | [optional] 

### Return type

[**list[RelationImpl]**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The relations have been changed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_relations**
> RelationPagedResponse find_relations(offset=offset, limit=limit, relation_type_id=relation_type_id, source_id=source_id, target_id=target_id, source_target_logical_operator=source_target_logical_operator)

Returns relations matching the given search criteria.

Returns relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned relations satisfy all constraints that are specified in this search criteria. By default a result containing 1000 relations is returned.

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
    api_instance = collibra_core.RelationsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
relation_type_id = 'relation_type_id_example' # str | The ID of the type of relations to search for. (optional)
source_id = 'source_id_example' # str | The ID of the source of relations to search for. (optional)
target_id = 'target_id_example' # str | The ID of the target of relations to search for. (optional)
source_target_logical_operator = 'AND' # str | The logical operator determining how to combine the source and target criteria: AND or OR. (optional) (default to 'AND')

    try:
        # Returns relations matching the given search criteria.
        api_response = api_instance.find_relations(offset=offset, limit=limit, relation_type_id=relation_type_id, source_id=source_id, target_id=target_id, source_target_logical_operator=source_target_logical_operator)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationsApi->find_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **relation_type_id** | [**str**](.md)| The ID of the type of relations to search for. | [optional] 
 **source_id** | [**str**](.md)| The ID of the source of relations to search for. | [optional] 
 **target_id** | [**str**](.md)| The ID of the target of relations to search for. | [optional] 
 **source_target_logical_operator** | **str**| The logical operator determining how to combine the source and target criteria: AND or OR. | [optional] [default to &#39;AND&#39;]

### Return type

[**RelationPagedResponse**](RelationPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found relations. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_relation**
> RelationImpl get_relation(relation_id)

Returns a relation identified by given id.

Returns a relation identified by given id.

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
    api_instance = collibra_core.RelationsApi(api_client)
    relation_id = 'relation_id_example' # str | the ID of the relation

    try:
        # Returns a relation identified by given id.
        api_response = api_instance.get_relation(relation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RelationsApi->get_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | [**str**](.md)| the ID of the relation | 

### Return type

[**RelationImpl**](RelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found relation. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relation**
> remove_relation(relation_id)

Removes a relation identified by given id.

Removes a relation identified by given id.

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
    api_instance = collibra_core.RelationsApi(api_client)
    relation_id = 'relation_id_example' # str | the ID of the relation to remove

    try:
        # Removes a relation identified by given id.
        api_instance.remove_relation(relation_id)
    except ApiException as e:
        print("Exception when calling RelationsApi->remove_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **relation_id** | [**str**](.md)| the ID of the relation to remove | 

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
**204** | The relation has been removed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_relation1**
> remove_relation1(request_body=request_body)

Removes multiple relations.

Removes multiple relations.

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
    api_instance = collibra_core.RelationsApi(api_client)
    request_body = ['request_body_example'] # list[str] | the IDs of the relations to be removed (optional)

    try:
        # Removes multiple relations.
        api_instance.remove_relation1(request_body=request_body)
    except ApiException as e:
        print("Exception when calling RelationsApi->remove_relation1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| the IDs of the relations to be removed | [optional] 

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
**204** | The relations have been removed successfully. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

