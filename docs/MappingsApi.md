# collibra_core.MappingsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mapping**](MappingsApi.md#add_mapping) | **POST** /mappings | Adds a new mapping.
[**add_mappings**](MappingsApi.md#add_mappings) | **POST** /mappings/bulk | Adds new mappings.
[**change_mapping**](MappingsApi.md#change_mapping) | **PATCH** /mappings/{mappingId} | Changes the mapping identified by its id.
[**change_mapping_by_external_entity**](MappingsApi.md#change_mapping_by_external_entity) | **PATCH** /mappings/externalSystem/{externalSystemId}/externalEntity/{externalEntityId} | Changes the mapping identified by its external ids.
[**change_mapping_by_mapped_resource**](MappingsApi.md#change_mapping_by_mapped_resource) | **PATCH** /mappings/externalSystem/{externalSystemId}/mappedResource/{mappedResourceId} | Changes the mapping identified by its external system id and mapped resource id.
[**change_mappings**](MappingsApi.md#change_mappings) | **PATCH** /mappings/bulk | Changes multiple mappings identified by their ids.
[**change_mappings_by_external_entities**](MappingsApi.md#change_mappings_by_external_entities) | **PATCH** /mappings/externalSystem/externalEntity/bulk | Changes the mappings identified by their external ids.
[**change_mappings_by_mapped_resources**](MappingsApi.md#change_mappings_by_mapped_resources) | **PATCH** /mappings/externalSystem/mappedResource/bulk | Changes the mapping identified by their external system ids and mapped resource ids.
[**find_mappings**](MappingsApi.md#find_mappings) | **GET** /mappings | Returns mappings matching the given search criteria.
[**get_mapping**](MappingsApi.md#get_mapping) | **GET** /mappings/{mappingId} | Returns a mapping identified by given id.
[**get_mapping_by_external_entity**](MappingsApi.md#get_mapping_by_external_entity) | **GET** /mappings/externalSystem/{externalSystemId}/externalEntity/{externalEntityId} | Returns a mapping identified by its external ids.
[**get_mapping_by_mapped_resource**](MappingsApi.md#get_mapping_by_mapped_resource) | **GET** /mappings/externalSystem/{externalSystemId}/mappedResource/{mappedResourceId} | Returns a mapping identified by its external system id and mapped resource id.
[**remove_mapping**](MappingsApi.md#remove_mapping) | **DELETE** /mappings/{mappingId} | Removes the mapping identified by its id.
[**remove_mapping_by_external_entity**](MappingsApi.md#remove_mapping_by_external_entity) | **DELETE** /mappings/externalSystem/{externalSystemId}/externalEntity/{externalEntityId} | Removes the mapping identified by its external ids.
[**remove_mapping_by_mapped_resource**](MappingsApi.md#remove_mapping_by_mapped_resource) | **DELETE** /mappings/externalSystem/{externalSystemId}/mappedResource/{mappedResourceId} | Removes the mapping identified by its external system id and mapped resource id.
[**remove_mappings_by_external_system_in_job**](MappingsApi.md#remove_mappings_by_external_system_in_job) | **POST** /mappings/externalSystem/{externalSystemId}/removalJobs | Removes all the mappings identified by given external system id.
[**remove_mappings_in_job**](MappingsApi.md#remove_mappings_in_job) | **POST** /mappings/removalJobs | Removes multiple mappings in job.


# **add_mapping**
> Mapping add_mapping(add_mapping_request=add_mapping_request)

Adds a new mapping.

Adds a new mapping.

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
    api_instance = collibra_core.MappingsApi(api_client)
    add_mapping_request = collibra_core.AddMappingRequest() # AddMappingRequest | The properties of the mapping to be added. (optional)

    try:
        # Adds a new mapping.
        api_response = api_instance.add_mapping(add_mapping_request=add_mapping_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->add_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_mapping_request** | [**AddMappingRequest**](AddMappingRequest.md)| The properties of the mapping to be added. | [optional] 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Mapping successfully added. |  -  |
**400** | A mapping with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mappings**
> list[Mapping] add_mappings(add_mapping_request=add_mapping_request)

Adds new mappings.

Adds new mappings.

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
    api_instance = collibra_core.MappingsApi(api_client)
    add_mapping_request = [collibra_core.AddMappingRequest()] # list[AddMappingRequest] | The properties of the mappings to be added. (optional)

    try:
        # Adds new mappings.
        api_response = api_instance.add_mappings(add_mapping_request=add_mapping_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->add_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_mapping_request** | [**list[AddMappingRequest]**](AddMappingRequest.md)| The properties of the mappings to be added. | [optional] 

### Return type

[**list[Mapping]**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Mappings successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mapping**
> Mapping change_mapping(mapping_id, change_mapping_request=change_mapping_request)

Changes the mapping identified by its id.

Changes the mapping identified by its <code>id</code>.<p>Change the mapping identified by its <code>id</code> with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    mapping_id = 'mapping_id_example' # str | The ID of the mapping to be changed.
change_mapping_request = collibra_core.ChangeMappingRequest() # ChangeMappingRequest | The properties of the mapping to be changed. (optional)

    try:
        # Changes the mapping identified by its id.
        api_response = api_instance.change_mapping(mapping_id, change_mapping_request=change_mapping_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->change_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | [**str**](.md)| The ID of the mapping to be changed. | 
 **change_mapping_request** | [**ChangeMappingRequest**](ChangeMappingRequest.md)| The properties of the mapping to be changed. | [optional] 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping successfully changed. |  -  |
**404** | Mapping could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mapping_by_external_entity**
> Mapping change_mapping_by_external_entity(external_system_id, external_entity_id, change_mapping_by_external_entity_request=change_mapping_by_external_entity_request)

Changes the mapping identified by its external ids.

Changes the mapping identified by its external <code>id</code>s.<p>Changes the mapping identified by its external <code>id</code>s with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'external_system_id_example' # str | The external system ID of the mapping to be changed.
external_entity_id = 'external_entity_id_example' # str | The external entity ID of the mapping to be changed.
change_mapping_by_external_entity_request = collibra_core.ChangeMappingByExternalEntityRequest() # ChangeMappingByExternalEntityRequest | The properties of the mapping to be changed. (optional)

    try:
        # Changes the mapping identified by its external ids.
        api_response = api_instance.change_mapping_by_external_entity(external_system_id, external_entity_id, change_mapping_by_external_entity_request=change_mapping_by_external_entity_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->change_mapping_by_external_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**| The external system ID of the mapping to be changed. | 
 **external_entity_id** | **str**| The external entity ID of the mapping to be changed. | 
 **change_mapping_by_external_entity_request** | [**ChangeMappingByExternalEntityRequest**](ChangeMappingByExternalEntityRequest.md)| The properties of the mapping to be changed. | [optional] 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping successfully changed. |  -  |
**404** | Mapping could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mapping_by_mapped_resource**
> Mapping change_mapping_by_mapped_resource(external_system_id, mapped_resource_id, change_mapping_by_mapped_resource_request=change_mapping_by_mapped_resource_request)

Changes the mapping identified by its external system id and mapped resource id.

Changes the mapping identified by its external system <code>id</code> and mapped resource <code>id</code>.<p>Changes the mapping identified by its external system <code>id</code> and mapped resource <code>id</code> with the information that is present in the requests. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'external_system_id_example' # str | The external system id of the mapping to be changed.
mapped_resource_id = 'mapped_resource_id_example' # str | The mapped resource id of the mapping to be changed.
change_mapping_by_mapped_resource_request = collibra_core.ChangeMappingByMappedResourceRequest() # ChangeMappingByMappedResourceRequest | The properties of the mapping to be changed. (optional)

    try:
        # Changes the mapping identified by its external system id and mapped resource id.
        api_response = api_instance.change_mapping_by_mapped_resource(external_system_id, mapped_resource_id, change_mapping_by_mapped_resource_request=change_mapping_by_mapped_resource_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->change_mapping_by_mapped_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**| The external system id of the mapping to be changed. | 
 **mapped_resource_id** | [**str**](.md)| The mapped resource id of the mapping to be changed. | 
 **change_mapping_by_mapped_resource_request** | [**ChangeMappingByMappedResourceRequest**](ChangeMappingByMappedResourceRequest.md)| The properties of the mapping to be changed. | [optional] 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping successfully changed. |  -  |
**404** | Mapping could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mappings**
> list[Mapping] change_mappings(change_mapping_request=change_mapping_request)

Changes multiple mappings identified by their ids.

Changes multiple mappings identified by their <code>id</code>s.<p>Change the mappings identified by its <code>id</code>s with the information that is present in the requests. Only properties that are specified in these requests and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    change_mapping_request = [collibra_core.ChangeMappingRequest()] # list[ChangeMappingRequest] | The properties of the mappings to be changed. (optional)

    try:
        # Changes multiple mappings identified by their ids.
        api_response = api_instance.change_mappings(change_mapping_request=change_mapping_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->change_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_mapping_request** | [**list[ChangeMappingRequest]**](ChangeMappingRequest.md)| The properties of the mappings to be changed. | [optional] 

### Return type

[**list[Mapping]**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mappings successfully changed. |  -  |
**404** | One of the mappings could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mappings_by_external_entities**
> list[Mapping] change_mappings_by_external_entities(change_mapping_by_external_entity_request=change_mapping_by_external_entity_request)

Changes the mappings identified by their external ids.

Changes the mappings identified by their external <code>id</code>s.<p>Changes the mappings identified by their external <code>id</code>s with the information that is present in the requests. Only properties that are specified in these requests and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    change_mapping_by_external_entity_request = [collibra_core.ChangeMappingByExternalEntityRequest()] # list[ChangeMappingByExternalEntityRequest] | The properties of the mappings to be changed. (optional)

    try:
        # Changes the mappings identified by their external ids.
        api_response = api_instance.change_mappings_by_external_entities(change_mapping_by_external_entity_request=change_mapping_by_external_entity_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->change_mappings_by_external_entities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_mapping_by_external_entity_request** | [**list[ChangeMappingByExternalEntityRequest]**](ChangeMappingByExternalEntityRequest.md)| The properties of the mappings to be changed. | [optional] 

### Return type

[**list[Mapping]**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mappings successfully changed. |  -  |
**404** | One of the mappings could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_mappings_by_mapped_resources**
> list[Mapping] change_mappings_by_mapped_resources(change_mapping_by_mapped_resource_request=change_mapping_by_mapped_resource_request)

Changes the mapping identified by their external system ids and mapped resource ids.

Changes the mapping identified by their external system <code>id</code>s and mapped resource <code>id</code>s.<p>Changes the mapping identified by their external system <code>id</code>s and mapped resource <code>id</code>s with the information that is present in the requests. Only properties that are specified in these requests and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    change_mapping_by_mapped_resource_request = [collibra_core.ChangeMappingByMappedResourceRequest()] # list[ChangeMappingByMappedResourceRequest] | The properties of the mappings to be changed. (optional)

    try:
        # Changes the mapping identified by their external system ids and mapped resource ids.
        api_response = api_instance.change_mappings_by_mapped_resources(change_mapping_by_mapped_resource_request=change_mapping_by_mapped_resource_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->change_mappings_by_mapped_resources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_mapping_by_mapped_resource_request** | [**list[ChangeMappingByMappedResourceRequest]**](ChangeMappingByMappedResourceRequest.md)| The properties of the mappings to be changed. | [optional] 

### Return type

[**list[Mapping]**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mappings successfully changed. |  -  |
**404** | One of the mappings could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_mappings**
> MappingPagedResponse find_mappings(offset=offset, limit=limit, external_system_id=external_system_id, mapped_resource_type=mapped_resource_type, sync_action=sync_action)

Returns mappings matching the given search criteria.

Returns mappings matching the given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p>The returned synchronization information satisfies all constraints that are specified in this search criteria. By default a result containing 1000 mappings is returned.</p>

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
    api_instance = collibra_core.MappingsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
external_system_id = 'EXT_BI_SYS' # str | The ID of the external system that the mapped resource belongs to. (optional)
mapped_resource_type = 'Asset' # str | The type of the mapped resource. (optional)
sync_action = 'sync_action_example' # str | The type of the action performed during last successful synchronization. (optional)

    try:
        # Returns mappings matching the given search criteria.
        api_response = api_instance.find_mappings(offset=offset, limit=limit, external_system_id=external_system_id, mapped_resource_type=mapped_resource_type, sync_action=sync_action)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->find_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **external_system_id** | **str**| The ID of the external system that the mapped resource belongs to. | [optional] 
 **mapped_resource_type** | **str**| The type of the mapped resource. | [optional] 
 **sync_action** | **str**| The type of the action performed during last successful synchronization. | [optional] 

### Return type

[**MappingPagedResponse**](MappingPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found synchronization information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping**
> Mapping get_mapping(mapping_id)

Returns a mapping identified by given id.

Returns a mapping identified by given <code>id</code>.

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
    api_instance = collibra_core.MappingsApi(api_client)
    mapping_id = 'mapping_id_example' # str | The id of the mapping.

    try:
        # Returns a mapping identified by given id.
        api_response = api_instance.get_mapping(mapping_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->get_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | [**str**](.md)| The id of the mapping. | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping successfully found. |  -  |
**404** | Mapping could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_by_external_entity**
> Mapping get_mapping_by_external_entity(external_system_id, external_entity_id)

Returns a mapping identified by its external ids.

Returns a mapping identified by its external <code>id</code>s.

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'EXT_BI_SYS' # str | 
external_entity_id = 'ID_1234' # str | 

    try:
        # Returns a mapping identified by its external ids.
        api_response = api_instance.get_mapping_by_external_entity(external_system_id, external_entity_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->get_mapping_by_external_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**|  | 
 **external_entity_id** | **str**|  | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping successfully found. |  -  |
**404** | Mapping could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping_by_mapped_resource**
> Mapping get_mapping_by_mapped_resource(external_system_id, mapped_resource_id)

Returns a mapping identified by its external system id and mapped resource id.

Returns a mapping identified by its external system <code>id</code> and mapped resource <code>id</code>.

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'EXT_BI_SYS' # str | 
mapped_resource_id = 'mapped_resource_id_example' # str | 

    try:
        # Returns a mapping identified by its external system id and mapped resource id.
        api_response = api_instance.get_mapping_by_mapped_resource(external_system_id, mapped_resource_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->get_mapping_by_mapped_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**|  | 
 **mapped_resource_id** | [**str**](.md)|  | 

### Return type

[**Mapping**](Mapping.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mapping successfully found. |  -  |
**404** | Mapping could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mapping**
> remove_mapping(mapping_id)

Removes the mapping identified by its id.

Removes the mapping identified by its <code>id</code>.<p>If the mapping does not exist, an exception is NOT thrown.

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
    api_instance = collibra_core.MappingsApi(api_client)
    mapping_id = 'mapping_id_example' # str | The id of the mapping.

    try:
        # Removes the mapping identified by its id.
        api_instance.remove_mapping(mapping_id)
    except ApiException as e:
        print("Exception when calling MappingsApi->remove_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | [**str**](.md)| The id of the mapping. | 

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
**204** | Mapping successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mapping_by_external_entity**
> remove_mapping_by_external_entity(external_system_id, external_entity_id)

Removes the mapping identified by its external ids.

Removes the mapping identified by its external <code>id</code>s.<p>If the mapping does not exist, an exception is NOT thrown.

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'external_system_id_example' # str | The external system id of the mapping to be removed.
external_entity_id = 'external_entity_id_example' # str | The external entity id of the mapping to be removed.

    try:
        # Removes the mapping identified by its external ids.
        api_instance.remove_mapping_by_external_entity(external_system_id, external_entity_id)
    except ApiException as e:
        print("Exception when calling MappingsApi->remove_mapping_by_external_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**| The external system id of the mapping to be removed. | 
 **external_entity_id** | **str**| The external entity id of the mapping to be removed. | 

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
**204** | Mapping successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mapping_by_mapped_resource**
> remove_mapping_by_mapped_resource(external_system_id, mapped_resource_id)

Removes the mapping identified by its external system id and mapped resource id.

Removes the mapping identified by its external system <code>id</code> and mapped resource <code>id</code>.<p>If the mapping does not exist, an exception is NOT thrown.

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'external_system_id_example' # str | The external system id of the mapping to be changed.
mapped_resource_id = 'mapped_resource_id_example' # str | The mapped resource id of the mapping to be changed.

    try:
        # Removes the mapping identified by its external system id and mapped resource id.
        api_instance.remove_mapping_by_mapped_resource(external_system_id, mapped_resource_id)
    except ApiException as e:
        print("Exception when calling MappingsApi->remove_mapping_by_mapped_resource: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**| The external system id of the mapping to be changed. | 
 **mapped_resource_id** | **str**| The mapped resource id of the mapping to be changed. | 

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
**204** | Mapping successfully removed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mappings_by_external_system_in_job**
> Job remove_mappings_by_external_system_in_job(external_system_id)

Removes all the mappings identified by given external system id.

Removes all the mappings identified by given external system <code>id</code>.

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
    api_instance = collibra_core.MappingsApi(api_client)
    external_system_id = 'external_system_id_example' # str | The id of the external system of the mappings that will be removed.

    try:
        # Removes all the mappings identified by given external system id.
        api_response = api_instance.remove_mappings_by_external_system_in_job(external_system_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->remove_mappings_by_external_system_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **external_system_id** | **str**| The id of the external system of the mappings that will be removed. | 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mappings removal successfully started. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_mappings_in_job**
> Job remove_mappings_in_job(request_body=request_body)

Removes multiple mappings in job.

Removes multiple mappings in job.<p>If any mapping does not exist, an exception is NOT thrown.

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
    api_instance = collibra_core.MappingsApi(api_client)
    request_body = ['request_body_example'] # list[str] | The ids of the mappings to be removed. (optional)

    try:
        # Removes multiple mappings in job.
        api_response = api_instance.remove_mappings_in_job(request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling MappingsApi->remove_mappings_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| The ids of the mappings to be removed. | [optional] 

### Return type

[**Job**](Job.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Mappings removal successfully started. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

