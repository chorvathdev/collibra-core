# collibra_core.IssuesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_issue**](IssuesApi.md#add_issue) | **POST** /issues | Adds a new issue.
[**find_issues**](IssuesApi.md#find_issues) | **GET** /issues | Returns issues matching the given search criteria.
[**move_issue**](IssuesApi.md#move_issue) | **PATCH** /issues/{issueId}/community/{communityId} | Moves an issue to another community.


# **add_issue**
> AssetImpl add_issue(add_issue_request=add_issue_request)

Adds a new issue.

Adds a new issue with the given parameters.

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
    api_instance = collibra_core.IssuesApi(api_client)
    add_issue_request = collibra_core.AddIssueRequest() # AddIssueRequest | The properties of the issue to be added (optional)

    try:
        # Adds a new issue.
        api_response = api_instance.add_issue(add_issue_request=add_issue_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IssuesApi->add_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_issue_request** | [**AddIssueRequest**](AddIssueRequest.md)| The properties of the issue to be added | [optional] 

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Issue successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_issues**
> AssetPagedResponse find_issues(offset=offset, limit=limit, sort_order=sort_order, sort_field=sort_field, only_open_issues=only_open_issues, user_relation=user_relation)

Returns issues matching the given search criteria.

Returns issues matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned issues satisfy all constraints that are specified in this search criteria. By default a result containing 1000 issues is returned.

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
    api_instance = collibra_core.IssuesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
sort_order = 'ASC' # str | The sorting order of the results. (optional) (default to 'ASC')
sort_field = 'NAME' # str | The field on which the results are sorted. Default is NAME. (optional) (default to 'NAME')
only_open_issues = True # bool | Whether only open issues should be returned. (optional) (default to True)
user_relation = 'ALL' # str | The relation of the user with the issues to be returned. By default all issues for the current user will be returned. (optional) (default to 'ALL')

    try:
        # Returns issues matching the given search criteria.
        api_response = api_instance.find_issues(offset=offset, limit=limit, sort_order=sort_order, sort_field=sort_field, only_open_issues=only_open_issues, user_relation=user_relation)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IssuesApi->find_issues: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **sort_order** | **str**| The sorting order of the results. | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| The field on which the results are sorted. Default is NAME. | [optional] [default to &#39;NAME&#39;]
 **only_open_issues** | **bool**| Whether only open issues should be returned. | [optional] [default to True]
 **user_relation** | **str**| The relation of the user with the issues to be returned. By default all issues for the current user will be returned. | [optional] [default to &#39;ALL&#39;]

### Return type

[**AssetPagedResponse**](AssetPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found issues. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_issue**
> AssetImpl move_issue(issue_id, community_id)

Moves an issue to another community.

Moves an issue to another community.

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
    api_instance = collibra_core.IssuesApi(api_client)
    issue_id = 'issue_id_example' # str | ID of the issue to be moved
community_id = 'community_id_example' # str | ID of the community to move the issue to

    try:
        # Moves an issue to another community.
        api_response = api_instance.move_issue(issue_id, community_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling IssuesApi->move_issue: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | [**str**](.md)| ID of the issue to be moved | 
 **community_id** | [**str**](.md)| ID of the community to move the issue to | 

### Return type

[**AssetImpl**](AssetImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The moved issue. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

