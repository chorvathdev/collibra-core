# collibra_core.CommunitiesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_communities**](CommunitiesApi.md#add_communities) | **POST** /communities/bulk | Add multiple communities
[**add_community**](CommunitiesApi.md#add_community) | **POST** /communities | Add community
[**change_communities**](CommunitiesApi.md#change_communities) | **PATCH** /communities/bulk | Change multiple communities
[**change_community**](CommunitiesApi.md#change_community) | **PATCH** /communities/{communityId} | Change community
[**change_to_root_community**](CommunitiesApi.md#change_to_root_community) | **POST** /communities/{communityId}/root | Change to root community
[**find_communities**](CommunitiesApi.md#find_communities) | **GET** /communities | Find communities
[**get_community**](CommunitiesApi.md#get_community) | **GET** /communities/{communityId} | Get community
[**get_community_breadcrumb**](CommunitiesApi.md#get_community_breadcrumb) | **GET** /communities/{communityId}/breadcrumb | Get community breadcrumb
[**remove_communities**](CommunitiesApi.md#remove_communities) | **DELETE** /communities/bulk | Remove multiple communities
[**remove_communities_in_job**](CommunitiesApi.md#remove_communities_in_job) | **POST** /communities/removalJobs | Remove multiple communities asynchronously
[**remove_community**](CommunitiesApi.md#remove_community) | **DELETE** /communities/{communityId} | Remove community


# **add_communities**
> list[CommunityImpl] add_communities(add_community_request=add_community_request)

Add multiple communities

Adds multiple communities with the given parameters

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    add_community_request = [collibra_core.AddCommunityRequest()] # list[AddCommunityRequest] | List of the properties of the communities to be added. (optional)

    try:
        # Add multiple communities
        api_response = api_instance.add_communities(add_community_request=add_community_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->add_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_community_request** | [**list[AddCommunityRequest]**](AddCommunityRequest.md)| List of the properties of the communities to be added. | [optional] 

### Return type

[**list[CommunityImpl]**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Communities successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_community**
> CommunityImpl add_community(add_community_request=add_community_request)

Add community

Adds a new community with the given parameters.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    add_community_request = collibra_core.AddCommunityRequest() # AddCommunityRequest | the properties of the community to be added (optional)

    try:
        # Add community
        api_response = api_instance.add_community(add_community_request=add_community_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->add_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_community_request** | [**AddCommunityRequest**](AddCommunityRequest.md)| the properties of the community to be added | [optional] 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Community successfully added. |  -  |
**400** | A community with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_communities**
> list[CommunityImpl] change_communities(change_community_request=change_community_request)

Change multiple communities

Changes multiple communities using the given request parameters

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    change_community_request = [collibra_core.ChangeCommunityRequest()] # list[ChangeCommunityRequest] | List of the properties of the communities to be changed. (optional)

    try:
        # Change multiple communities
        api_response = api_instance.change_communities(change_community_request=change_community_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->change_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_community_request** | [**list[ChangeCommunityRequest]**](ChangeCommunityRequest.md)| List of the properties of the communities to be changed. | [optional] 

### Return type

[**list[CommunityImpl]**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Communities changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_community**
> CommunityImpl change_community(community_id, change_community_request=change_community_request)

Change community

Changes the community with the information that is present in the request. Only properties that are specified in this request and have non-<code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    community_id = 'community_id_example' # str | the id of the community to be changed.
change_community_request = collibra_core.ChangeCommunityRequest() # ChangeCommunityRequest | the properties of the community to be changed (optional)

    try:
        # Change community
        api_response = api_instance.change_community(community_id, change_community_request=change_community_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->change_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| the id of the community to be changed. | 
 **change_community_request** | [**ChangeCommunityRequest**](ChangeCommunityRequest.md)| the properties of the community to be changed | [optional] 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Community changed |  -  |
**404** | Community not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_to_root_community**
> CommunityImpl change_to_root_community(community_id)

Change to root community

Changes the community with given ID to a root community.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    community_id = 'community_id_example' # str | The ID of the community that will be changed to a root community

    try:
        # Change to root community
        api_response = api_instance.change_to_root_community(community_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->change_to_root_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| The ID of the community that will be changed to a root community | 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Community changed |  -  |
**404** | Community not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_communities**
> CommunityPagedResponse find_communities(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, sort_field=sort_field, sort_order=sort_order)

Find communities

Returns communities matching the given search criteria. Only parameters that are specified in this request and have non-<code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 communities is returned.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the community to search for. (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code>. (optional) (default to 'ANYWHERE')
parent_id = 'parent_id_example' # str | The ID of the parent community to find the communities in. (optional)
exclude_meta = True # bool | The exclude meta flag. If this is set to true then the meta communities will not be returned<br/>(meta communities are i.e. communities not created manually by the user). (optional) (default to True)
sort_field = 'NAME' # str | The field on which the results are sorted. (optional) (default to 'NAME')
sort_order = 'ASC' # str | The sorting order. (optional) (default to 'ASC')

    try:
        # Find communities
        api_response = api_instance.find_communities(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, parent_id=parent_id, exclude_meta=exclude_meta, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->find_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the community to search for. | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt;. | [optional] [default to &#39;ANYWHERE&#39;]
 **parent_id** | [**str**](.md)| The ID of the parent community to find the communities in. | [optional] 
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the meta communities will not be returned&lt;br/&gt;(meta communities are i.e. communities not created manually by the user). | [optional] [default to True]
 **sort_field** | **str**| The field on which the results are sorted. | [optional] [default to &#39;NAME&#39;]
 **sort_order** | **str**| The sorting order. | [optional] [default to &#39;ASC&#39;]

### Return type

[**CommunityPagedResponse**](CommunityPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Communities searched |  -  |
**404** | Community not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community**
> CommunityImpl get_community(community_id)

Get community

Returns the community with the given ID.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    community_id = 'community_id_example' # str | the ID of the community

    try:
        # Get community
        api_response = api_instance.get_community(community_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->get_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| the ID of the community | 

### Return type

[**CommunityImpl**](CommunityImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Community found |  -  |
**401** | User lacks view permission |  -  |
**404** | Community not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_community_breadcrumb**
> list[NamedResourceReferenceImpl] get_community_breadcrumb(community_id)

Get community breadcrumb

Returns the list of communities that lead to the community identified by the given ID.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    community_id = 'community_id_example' # str | The ID of the community

    try:
        # Get community breadcrumb
        api_response = api_instance.get_community_breadcrumb(community_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->get_community_breadcrumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | **str**| The ID of the community | 

### Return type

[**list[NamedResourceReferenceImpl]**](NamedResourceReferenceImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Community breadcrumb retrieved |  -  |
**401** | User lacks view permission |  -  |
**404** | Community not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_communities**
> remove_communities(request_body=request_body)

Remove multiple communities

This endpoint will be removed in the next major release. Please use POST /communities/removalJobs.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    request_body = ['request_body_example'] # list[str] | the IDs of the communities to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

    try:
        # Remove multiple communities
        api_instance.remove_communities(request_body=request_body)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->remove_communities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| the IDs of the communities to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

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
**204** | Communities removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_communities_in_job**
> Job remove_communities_in_job(request_body=request_body)

Remove multiple communities asynchronously

Removes multiple communities in a job.

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    request_body = ['request_body_example'] # list[str] | the IDs of the communities to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

    try:
        # Remove multiple communities asynchronously
        api_response = api_instance.remove_communities_in_job(request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->remove_communities_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| the IDs of the communities to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

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
**204** | Removal job started |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_community**
> remove_community(community_id)

Remove community

This endpoint will be removed in the next major release. Please use POST /communities/removalJobs

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
    api_instance = collibra_core.CommunitiesApi(api_client)
    community_id = 'community_id_example' # str | the ID of the community to remove

    try:
        # Remove community
        api_instance.remove_community(community_id)
    except ApiException as e:
        print("Exception when calling CommunitiesApi->remove_community: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **community_id** | [**str**](.md)| the ID of the community to remove | 

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
**204** | Community removed |  -  |
**404** | Community not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

