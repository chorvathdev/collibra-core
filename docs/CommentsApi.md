# collibra_core.CommentsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_comment**](CommentsApi.md#add_comment) | **POST** /comments | Add comment.
[**change_comment**](CommentsApi.md#change_comment) | **PATCH** /comments/{commentId} | Change comment.
[**find_comments**](CommentsApi.md#find_comments) | **GET** /comments | Find comments.
[**get_comment**](CommentsApi.md#get_comment) | **GET** /comments/{commentId} | Get comment.
[**remove_comment**](CommentsApi.md#remove_comment) | **DELETE** /comments/{commentId} | Remove comment.


# **add_comment**
> Comment add_comment(add_comment_request=add_comment_request)

Add comment.

Adds a new comment.

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
    api_instance = collibra_core.CommentsApi(api_client)
    add_comment_request = collibra_core.AddCommentRequest() # AddCommentRequest | The properties of new comment. (optional)

    try:
        # Add comment.
        api_response = api_instance.add_comment(add_comment_request=add_comment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_comment_request** | [**AddCommentRequest**](AddCommentRequest.md)| The properties of new comment. | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Comment successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_comment**
> Comment change_comment(comment_id, change_comment_request=change_comment_request)

Change comment.

<p>Modifies the comment with the specified ID.</p><p>Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.</p>

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
    api_instance = collibra_core.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | The ID of the comment to be changed.
change_comment_request = collibra_core.ChangeCommentRequest() # ChangeCommentRequest | The properties to change comment. (optional)

    try:
        # Change comment.
        api_response = api_instance.change_comment(comment_id, change_comment_request=change_comment_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->change_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**str**](.md)| The ID of the comment to be changed. | 
 **change_comment_request** | [**ChangeCommentRequest**](ChangeCommentRequest.md)| The properties to change comment. | [optional] 

### Return type

[**Comment**](Comment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Comment successfully updated. |  -  |
**404** | Comment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_comments**
> CommentPagedResponse find_comments(offset=offset, limit=limit, parent_id=parent_id, user_id=user_id, base_resource_id=base_resource_id, root_comment=root_comment, sort_order=sort_order)

Find comments.

<p>Returns comments matching the given search criteria.</p><p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p><p>The returned comments satisfy all constraints that are specified in this search criteria.</p><p>By default, the result contains up to 1000 comments.</p>

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
    api_instance = collibra_core.CommentsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
parent_id = '8253ed81-0889-49d7-98db-defef5b5cd3b' # str | The ID of the comment which the reply comments should be searched for (optional)
user_id = '8253ed81-0889-49d7-98db-defef5b5cd3b' # str | The ID of the user who created the comment. (optional)
base_resource_id = '8253ed81-0889-49d7-98db-defef5b5cd3b' # str | The ID of the resource which the searched comments refer to. (optional)
root_comment = true # bool | Whether the searched comments should be root comments (not reply comments). (optional)
sort_order = 'DESC' # str | The order of sorting on the date the comment was created. (optional) (default to 'DESC')

    try:
        # Find comments.
        api_response = api_instance.find_comments(offset=offset, limit=limit, parent_id=parent_id, user_id=user_id, base_resource_id=base_resource_id, root_comment=root_comment, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->find_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **parent_id** | [**str**](.md)| The ID of the comment which the reply comments should be searched for | [optional] 
 **user_id** | [**str**](.md)| The ID of the user who created the comment. | [optional] 
 **base_resource_id** | [**str**](.md)| The ID of the resource which the searched comments refer to. | [optional] 
 **root_comment** | **bool**| Whether the searched comments should be root comments (not reply comments). | [optional] 
 **sort_order** | **str**| The order of sorting on the date the comment was created. | [optional] [default to &#39;DESC&#39;]

### Return type

[**CommentPagedResponse**](CommentPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The paged response with found comments. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_comment**
> Comment get_comment(comment_id)

Get comment.

Returns the comment with the specified ID.

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
    api_instance = collibra_core.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | The ID of the comment.

    try:
        # Get comment.
        api_response = api_instance.get_comment(comment_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CommentsApi->get_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**str**](.md)| The ID of the comment. | 

### Return type

[**Comment**](Comment.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response with found comment. |  -  |
**404** | Comment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_comment**
> remove_comment(comment_id)

Remove comment.

Removes the comment with the specified ID.

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
    api_instance = collibra_core.CommentsApi(api_client)
    comment_id = 'comment_id_example' # str | The ID of the comment to be removed.

    try:
        # Remove comment.
        api_instance.remove_comment(comment_id)
    except ApiException as e:
        print("Exception when calling CommentsApi->remove_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | [**str**](.md)| The ID of the comment to be removed. | 

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
**200** | Comment successfully removed. |  -  |
**404** | Comment not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

