# collibra_core.DiagramPicturesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_diagram_picture**](DiagramPicturesApi.md#add_diagram_picture) | **POST** /diagramPictures | Adds a diagram picture.


# **add_diagram_picture**
> str add_diagram_picture(add_diagram_picture_request=add_diagram_picture_request)

Adds a diagram picture.

Take a diagram picture for a given asset and diagram view. A diagram picture is a copy of traceability diagram (result diagram) at a given time (for more information on traceability diagram check DGC User Guide).  The motivation behind diagram picture is to be able to reopen them at a later point in time and be able to see them them exactly as they were created. This feature is not possible for result diagram which are always showing the current situation.

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
    api_instance = collibra_core.DiagramPicturesApi(api_client)
    add_diagram_picture_request = collibra_core.AddDiagramPictureRequest() # AddDiagramPictureRequest |  (optional)

    try:
        # Adds a diagram picture.
        api_response = api_instance.add_diagram_picture(add_diagram_picture_request=add_diagram_picture_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DiagramPicturesApi->add_diagram_picture: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_diagram_picture_request** | [**AddDiagramPictureRequest**](AddDiagramPictureRequest.md)|  | [optional] 

### Return type

**str**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Diagram picture successfully added.The response contains a UUID of the added diagram picture. The UUID can be used to compose an URL to retrive the diagram picture. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

