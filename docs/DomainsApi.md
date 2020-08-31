# collibra_core.DomainsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_domain**](DomainsApi.md#add_domain) | **POST** /domains | Add domain
[**add_domains**](DomainsApi.md#add_domains) | **POST** /domains/bulk | Add multpile domains
[**change_domain**](DomainsApi.md#change_domain) | **PATCH** /domains/{domainId} | Change domain
[**change_domains**](DomainsApi.md#change_domains) | **PATCH** /domains/bulk | Change multiple domains
[**find_domains**](DomainsApi.md#find_domains) | **GET** /domains | Search domains
[**get_domain**](DomainsApi.md#get_domain) | **GET** /domains/{domainId} | Get domain
[**get_domain_breadcrumb**](DomainsApi.md#get_domain_breadcrumb) | **GET** /domains/{domainId}/breadcrumb | Get domain breadcrumb
[**remove_domain**](DomainsApi.md#remove_domain) | **DELETE** /domains/{domainId} | Remove domain
[**remove_domains**](DomainsApi.md#remove_domains) | **DELETE** /domains/bulk | Remove multiple domains
[**remove_domains_in_job**](DomainsApi.md#remove_domains_in_job) | **POST** /domains/removalJobs | Remove multiple domains asynchronously


# **add_domain**
> DomainImpl add_domain(add_domain_request=add_domain_request)

Add domain

Adds a new domain with given data into a community.

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
    api_instance = collibra_core.DomainsApi(api_client)
    add_domain_request = collibra_core.AddDomainRequest() # AddDomainRequest | the properties of the domain to be added (optional)

    try:
        # Add domain
        api_response = api_instance.add_domain(add_domain_request=add_domain_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->add_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_domain_request** | [**AddDomainRequest**](AddDomainRequest.md)| the properties of the domain to be added | [optional] 

### Return type

[**DomainImpl**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domain successfully added. |  -  |
**400** | A domain with the given ID already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_domains**
> list[DomainImpl] add_domains(add_domain_request=add_domain_request)

Add multpile domains

Adds multiple domains using the given parameters

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
    api_instance = collibra_core.DomainsApi(api_client)
    add_domain_request = [collibra_core.AddDomainRequest()] # list[AddDomainRequest] | List of the properties of the domains to be added. (optional)

    try:
        # Add multpile domains
        api_response = api_instance.add_domains(add_domain_request=add_domain_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->add_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_domain_request** | [**list[AddDomainRequest]**](AddDomainRequest.md)| List of the properties of the domains to be added. | [optional] 

### Return type

[**list[DomainImpl]**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Domains successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domain**
> DomainImpl change_domain(domain_id, change_domain_request=change_domain_request)

Change domain

Changes the domain with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.

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
    api_instance = collibra_core.DomainsApi(api_client)
    domain_id = 'domain_id_example' # str | the ID of the domain to be changed.
change_domain_request = collibra_core.ChangeDomainRequest() # ChangeDomainRequest | the properties of the domain to be changed (optional)

    try:
        # Change domain
        api_response = api_instance.change_domain(domain_id, change_domain_request=change_domain_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->change_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| the ID of the domain to be changed. | 
 **change_domain_request** | [**ChangeDomainRequest**](ChangeDomainRequest.md)| the properties of the domain to be changed | [optional] 

### Return type

[**DomainImpl**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The domain has been changed successfully. |  -  |
**404** | Domain not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_domains**
> list[DomainImpl] change_domains(change_domain_request=change_domain_request)

Change multiple domains

Changes multiple domains using the given parameters

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
    api_instance = collibra_core.DomainsApi(api_client)
    change_domain_request = [collibra_core.ChangeDomainRequest()] # list[ChangeDomainRequest] | List of the properties of the domains to be changed. (optional)

    try:
        # Change multiple domains
        api_response = api_instance.change_domains(change_domain_request=change_domain_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->change_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_domain_request** | [**list[ChangeDomainRequest]**](ChangeDomainRequest.md)| List of the properties of the domains to be changed. | [optional] 

### Return type

[**list[DomainImpl]**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domains changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_domains**
> DomainPagedResponse find_domains(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, exclude_meta=exclude_meta, community_id=community_id, type_id=type_id, include_sub_communities=include_sub_communities)

Search domains

Finds the domains that match the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. By default a result containing 1000 domains is returned.

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
    api_instance = collibra_core.DomainsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
name = 'name_example' # str | The name of the domain to search for (optional)
name_match_mode = 'ANYWHERE' # str | The match mode used to compare <code>name</code> (optional) (default to 'ANYWHERE')
exclude_meta = True # bool | The exclude meta flag. If this is set to true then the meta domains will not be returned<br/>(meta domains are i.e. domains not created manually by the user) (optional) (default to True)
community_id = 'community_id_example' # str | The ID of the community to find the domains in (optional)
type_id = 'type_id_example' # str | The ID of the domain type to search for. Returned domains are of this type (optional)
include_sub_communities = False # bool | The include sub-communities flag. When set to true, sub-communities (of the community indicated via<br/>the <code>communityId</code> parameter) will be searched in. (optional) (default to False)

    try:
        # Search domains
        api_response = api_instance.find_domains(offset=offset, limit=limit, name=name, name_match_mode=name_match_mode, exclude_meta=exclude_meta, community_id=community_id, type_id=type_id, include_sub_communities=include_sub_communities)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->find_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **name** | **str**| The name of the domain to search for | [optional] 
 **name_match_mode** | **str**| The match mode used to compare &lt;code&gt;name&lt;/code&gt; | [optional] [default to &#39;ANYWHERE&#39;]
 **exclude_meta** | **bool**| The exclude meta flag. If this is set to true then the meta domains will not be returned&lt;br/&gt;(meta domains are i.e. domains not created manually by the user) | [optional] [default to True]
 **community_id** | [**str**](.md)| The ID of the community to find the domains in | [optional] 
 **type_id** | [**str**](.md)| The ID of the domain type to search for. Returned domains are of this type | [optional] 
 **include_sub_communities** | **bool**| The include sub-communities flag. When set to true, sub-communities (of the community indicated via&lt;br/&gt;the &lt;code&gt;communityId&lt;/code&gt; parameter) will be searched in. | [optional] [default to False]

### Return type

[**DomainPagedResponse**](DomainPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domains searched |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain**
> DomainImpl get_domain(domain_id)

Get domain

Returns the domain with the given ID

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
    api_instance = collibra_core.DomainsApi(api_client)
    domain_id = 'domain_id_example' # str | the ID of the domain

    try:
        # Get domain
        api_response = api_instance.get_domain(domain_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->get_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| the ID of the domain | 

### Return type

[**DomainImpl**](DomainImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Domain found |  -  |
**401** | User lacks view permission |  -  |
**404** | Domain not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_domain_breadcrumb**
> list[NamedResourceReferenceImpl] get_domain_breadcrumb(domain_id)

Get domain breadcrumb

Returns the list of resources that lead to the domain identified by the given ID.

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
    api_instance = collibra_core.DomainsApi(api_client)
    domain_id = 'domain_id_example' # str | The ID of the domain

    try:
        # Get domain breadcrumb
        api_response = api_instance.get_domain_breadcrumb(domain_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->get_domain_breadcrumb: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| The ID of the domain | 

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
**200** | Domain breadcrumb retrieved |  -  |
**401** | User lacks view permission |  -  |
**404** | Domain not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domain**
> Job remove_domain(domain_id)

Remove domain

This endpoint will be removed in the next major release. Please use POST /domains/removalJobs.

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
    api_instance = collibra_core.DomainsApi(api_client)
    domain_id = 'domain_id_example' # str | the ID of the domain to remove

    try:
        # Remove domain
        api_response = api_instance.remove_domain(domain_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->remove_domain: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | [**str**](.md)| the ID of the domain to remove | 

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
**204** | Domain removed |  -  |
**404** | Domain not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domains**
> remove_domains(request_body=request_body)

Remove multiple domains

This endpoint will be removed in the next major release. Please use POST /domains/removalJobs.

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
    api_instance = collibra_core.DomainsApi(api_client)
    request_body = ['request_body_example'] # list[str] | the IDs of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

    try:
        # Remove multiple domains
        api_instance.remove_domains(request_body=request_body)
    except ApiException as e:
        print("Exception when calling DomainsApi->remove_domains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| the IDs of the domains to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

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
**204** | Domains removed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_domains_in_job**
> Job remove_domains_in_job(request_body=request_body)

Remove multiple domains asynchronously

Removes multiple domains with the given IDs in a job.

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
    api_instance = collibra_core.DomainsApi(api_client)
    request_body = ['request_body_example'] # list[str] | the IDs of the domains to be removed, i.e. [\"6f685f90-1036-4d30-983a-a9bbcdd7b8f6\", \"6f685f90-1036-4d30-983a-a9bbcdd7b123\"] (optional)

    try:
        # Remove multiple domains asynchronously
        api_response = api_instance.remove_domains_in_job(request_body=request_body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DomainsApi->remove_domains_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**list[str]**](str.md)| the IDs of the domains to be removed, i.e. [\&quot;6f685f90-1036-4d30-983a-a9bbcdd7b8f6\&quot;, \&quot;6f685f90-1036-4d30-983a-a9bbcdd7b123\&quot;] | [optional] 

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
**204** | Domain removal job created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

