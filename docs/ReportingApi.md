# collibra_core.ReportingApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_insights_zip**](ReportingApi.md#get_insights_zip) | **GET** /reporting/insights/download | Reporting insights download


# **get_insights_zip**
> file get_insights_zip(snapshot_date=snapshot_date, format=format)

Reporting insights download

Returns a Reporting Data archive (zip) file that contains Apache Parquet files with table content for each of the six concepts (community, domain, asset, attribute, relation and responsibility) for one day (=snapshot date). Each morning, at 00:01 in the timezone of the Collibra platform, the reporting data of that platform is captured. The reporting data is retained for one rolling month and each month’s end before that. The tables structure (DDL) for this content is published [here](https://marketplace.collibra.com/listings/reporting-data-layer).

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
    api_instance = collibra_core.ReportingApi(api_client)
    snapshot_date = 'snapshot_date_example' # str | Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14) (optional)
format = 'zip' # str | Archive format. Currently only ZIP format is accepted (optional) (default to 'zip')

    try:
        # Reporting insights download
        api_response = api_instance.get_insights_zip(snapshot_date=snapshot_date, format=format)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ReportingApi->get_insights_zip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_date** | **str**| Snapshot date for reporting insights data in ISO8601 format (e.g.: 2019-05-14) | [optional] 
 **format** | **str**| Archive format. Currently only ZIP format is accepted | [optional] [default to &#39;zip&#39;]

### Return type

**file**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Insights has been downloaded |  -  |
**406** | The selected format is not acceptable |  -  |
**404** | There is no insights for given date |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

