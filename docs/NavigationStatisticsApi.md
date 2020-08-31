# collibra_core.NavigationStatisticsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**find_most_viewed_assets**](NavigationStatisticsApi.md#find_most_viewed_assets) | **GET** /navigation/most_viewed | Find most viewed assets.
[**find_recently_viewed_assets**](NavigationStatisticsApi.md#find_recently_viewed_assets) | **GET** /navigation/recently_viewed | Find recently viewed assets.


# **find_most_viewed_assets**
> NavigationStatisticsEntryPagedResponse find_most_viewed_assets(offset=offset, limit=limit, period=period, is_guest_excluded=is_guest_excluded)

Find most viewed assets.

Returns the most viewed assets by all users, with navigation-related info.

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
    api_instance = collibra_core.NavigationStatisticsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
period = 0 # int | The time span for which most viewed assets should be found. This time span must be expressed in milliseconds.<br/>For instance, to get most viewed assets for last 24 hours, period would be <code>86400000</code>.<br/>If it's unset (period = 0) looks for all time most viewed assets. (optional) (default to 0)
is_guest_excluded = False # bool | Whether guest visits should be excluded from result. (optional) (default to False)

    try:
        # Find most viewed assets.
        api_response = api_instance.find_most_viewed_assets(offset=offset, limit=limit, period=period, is_guest_excluded=is_guest_excluded)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NavigationStatisticsApi->find_most_viewed_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **period** | **int**| The time span for which most viewed assets should be found. This time span must be expressed in milliseconds.&lt;br/&gt;For instance, to get most viewed assets for last 24 hours, period would be &lt;code&gt;86400000&lt;/code&gt;.&lt;br/&gt;If it&#39;s unset (period &#x3D; 0) looks for all time most viewed assets. | [optional] [default to 0]
 **is_guest_excluded** | **bool**| Whether guest visits should be excluded from result. | [optional] [default to False]

### Return type

[**NavigationStatisticsEntryPagedResponse**](NavigationStatisticsEntryPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged response with found navigation statistics ordered by number of views descending. By default, the result contains up to 1000 navigation statistics. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_recently_viewed_assets**
> NavigationStatisticsEntryPagedResponse find_recently_viewed_assets(offset=offset, limit=limit)

Find recently viewed assets.

Returns the assets that were recently viewed by the current user.

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
    api_instance = collibra_core.NavigationStatisticsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)

    try:
        # Find recently viewed assets.
        api_response = api_instance.find_recently_viewed_assets(offset=offset, limit=limit)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NavigationStatisticsApi->find_recently_viewed_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]

### Return type

[**NavigationStatisticsEntryPagedResponse**](NavigationStatisticsEntryPagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Paged response with found navigation statistics ordered by last viewed date descending. Views number is not calculated. By default, the result contains up to 1000 navigation statistics. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

