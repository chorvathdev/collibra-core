# collibra_core.SAMLApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_sp_metadata_as_string**](SAMLApi.md#get_sp_metadata_as_string) | **GET** /security/saml | Returns the SAML Service Provider metadata for this instance.


# **get_sp_metadata_as_string**
> get_sp_metadata_as_string(complete=complete)

Returns the SAML Service Provider metadata for this instance.

Returns the SAML Service Provider metadata for this instance.

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
    api_instance = collibra_core.SAMLApi(api_client)
    complete = True # bool | Whether or not the meta data generated should include the non-required attributes (completeMetadata = true means all the non-essential attributes too). (optional)

    try:
        # Returns the SAML Service Provider metadata for this instance.
        api_instance.get_sp_metadata_as_string(complete=complete)
    except ApiException as e:
        print("Exception when calling SAMLApi->get_sp_metadata_as_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complete** | **bool**| Whether or not the meta data generated should include the non-required attributes (completeMetadata &#x3D; true means all the non-essential attributes too). | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | metadata successfully found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

