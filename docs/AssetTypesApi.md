# collibra_core.AssetTypesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_type**](AssetTypesApi.md#add_asset_type) | **POST** /assetTypes | Add asset type
[**add_asset_types**](AssetTypesApi.md#add_asset_types) | **POST** /assetTypes/bulk | Add multiple asset types
[**change_asset_type**](AssetTypesApi.md#change_asset_type) | **PATCH** /assetTypes/{assetTypeId} | Change asset type
[**change_asset_types**](AssetTypesApi.md#change_asset_types) | **PATCH** /assetTypes/bulk | Change multiple asset types
[**find_asset_types**](AssetTypesApi.md#find_asset_types) | **GET** /assetTypes | Find asset types matching criteria
[**find_parent_types**](AssetTypesApi.md#find_parent_types) | **GET** /assetTypes/{assetTypeId}/parents | Find parent types
[**find_sub_asset_types**](AssetTypesApi.md#find_sub_asset_types) | **GET** /assetTypes/{assetTypeId}/subTypes | Find asset subtypes
[**get_asset_type**](AssetTypesApi.md#get_asset_type) | **GET** /assetTypes/{assetTypeId} | Get asset type by ID
[**remove_asset_type**](AssetTypesApi.md#remove_asset_type) | **DELETE** /assetTypes/{assetTypeId} | Remove asset type by ID
[**remove_asset_types**](AssetTypesApi.md#remove_asset_types) | **DELETE** /assetTypes/bulk | Remove multiple asset types


# **add_asset_type**
> AssetTypeImpl add_asset_type(add_asset_type_request=add_asset_type_request)

Add asset type

Adds a new asset type with the given parameters.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    add_asset_type_request = collibra_core.AddAssetTypeRequest() # AddAssetTypeRequest | The properties of the asset type to be added (optional)

    try:
        # Add asset type
        api_response = api_instance.add_asset_type(add_asset_type_request=add_asset_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->add_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_asset_type_request** | [**AddAssetTypeRequest**](AddAssetTypeRequest.md)| The properties of the asset type to be added | [optional] 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset type successfully added. |  -  |
**400** | An asset type with the given ID already exists |  -  |
**404** | Parent asset type not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_asset_types**
> AssetTypeImpl add_asset_types(add_asset_type_request=add_asset_type_request)

Add multiple asset types

Adds multiple asset types in one go.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    add_asset_type_request = [collibra_core.AddAssetTypeRequest()] # list[AddAssetTypeRequest] |  (optional)

    try:
        # Add multiple asset types
        api_response = api_instance.add_asset_types(add_asset_type_request=add_asset_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->add_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_asset_type_request** | [**list[AddAssetTypeRequest]**](AddAssetTypeRequest.md)|  | [optional] 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Asset types successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset_type**
> AssetTypeImpl change_asset_type(asset_type_id, change_asset_type_request=change_asset_type_request)

Change asset type

Changes the asset type using the given parameters. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    asset_type_id = 'asset_type_id_example' # str | The ID of the asset type
change_asset_type_request = collibra_core.ChangeAssetTypeRequest() # ChangeAssetTypeRequest |  (optional)

    try:
        # Change asset type
        api_response = api_instance.change_asset_type(asset_type_id, change_asset_type_request=change_asset_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->change_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the asset type | 
 **change_asset_type_request** | [**ChangeAssetTypeRequest**](ChangeAssetTypeRequest.md)|  | [optional] 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset type changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_asset_types**
> list[AssetTypeImpl] change_asset_types(change_asset_type_request=change_asset_type_request)

Change multiple asset types

Changes multiple asset types using the given parameters.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    change_asset_type_request = [collibra_core.ChangeAssetTypeRequest()] # list[ChangeAssetTypeRequest] |  (optional)

    try:
        # Change multiple asset types
        api_response = api_instance.change_asset_types(change_asset_type_request=change_asset_type_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->change_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_asset_type_request** | [**list[ChangeAssetTypeRequest]**](ChangeAssetTypeRequest.md)|  | [optional] 

### Return type

[**list[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset types changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_asset_types**
> AssetTypePagedResponse find_asset_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, top_level=top_level, display_name_enabled=display_name_enabled)

Find asset types matching criteria

Returns asset types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 asset types is returned.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the asset type to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')
parent_id = 'parent_id_example' # str | The ID of the parent to find the asset types in. (optional)
exclude_meta = True # bool | Whether the meta asset types should be excluded from search or not. (optional) (default to True)
top_level = False # bool | Whether only top level asset types should be searched or not. (optional) (default to False)
display_name_enabled = True # bool | Whether only asset types with display names enabled (or disabled) should be searched. (optional)

    try:
        # Find asset types matching criteria
        api_response = api_instance.find_asset_types(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, top_level=top_level, display_name_enabled=display_name_enabled)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->find_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the asset type to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]
 **parent_id** | [**str**](.md)| The ID of the parent to find the asset types in. | [optional] 
 **exclude_meta** | **bool**| Whether the meta asset types should be excluded from search or not. | [optional] [default to True]
 **top_level** | **bool**| Whether only top level asset types should be searched or not. | [optional] [default to False]
 **display_name_enabled** | **bool**| Whether only asset types with display names enabled (or disabled) should be searched. | [optional] 

### Return type

[**AssetTypePagedResponse**](AssetTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Search ran successfully |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_parent_types**
> list[AssetTypeImpl] find_parent_types(asset_type_id)

Find parent types

Finds all the parent asset types of the asset with the given ID.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    asset_type_id = 'asset_type_id_example' # str | The unique identifier of the AssetType.

    try:
        # Find parent types
        api_response = api_instance.find_parent_types(asset_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->find_parent_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The unique identifier of the AssetType. | 

### Return type

[**list[AssetTypeImpl]**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Parent asset types found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_sub_asset_types**
> AssetTypePagedResponse find_sub_asset_types(asset_type_id, include_parent=include_parent)

Find asset subtypes

Finds all asset subtypes of an asset type, as specified by the request parameters.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    asset_type_id = 'asset_type_id_example' # str | The ID of the AssetType
include_parent = True # bool | Whether parent asset type should be included in the search result. (optional)

    try:
        # Find asset subtypes
        api_response = api_instance.find_sub_asset_types(asset_type_id, include_parent=include_parent)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->find_sub_asset_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the AssetType | 
 **include_parent** | **bool**| Whether parent asset type should be included in the search result. | [optional] 

### Return type

[**AssetTypePagedResponse**](AssetTypePagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset types found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type**
> AssetTypeImpl get_asset_type(asset_type_id)

Get asset type by ID

Returns the asset type having the given ID.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    asset_type_id = 'asset_type_id_example' # str | The ID of the asset type

    try:
        # Get asset type by ID
        api_response = api_instance.get_asset_type(asset_type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->get_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the asset type | 

### Return type

[**AssetTypeImpl**](AssetTypeImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Asset type found |  -  |
**404** | Asset type not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_asset_type**
> remove_asset_type(asset_type_id)

Remove asset type by ID

Removes the asset type having the given ID.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    asset_type_id = 'asset_type_id_example' # str | The ID of the asset type

    try:
        # Remove asset type by ID
        api_instance.remove_asset_type(asset_type_id)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->remove_asset_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_id** | [**str**](.md)| The ID of the asset type | 

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

# **remove_asset_types**
> remove_asset_types(request_body=request_body)

Remove multiple asset types

Removes multiple asset types identified by the given IDs.

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
    api_instance = collibra_core.AssetTypesApi(api_client)
    request_body = ['request_body_example'] # list[str] |  (optional)

    try:
        # Remove multiple asset types
        api_instance.remove_asset_types(request_body=request_body)
    except ApiException as e:
        print("Exception when calling AssetTypesApi->remove_asset_types: %s\n" % e)
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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Asset types removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

