# collibra_core.ComplexRelationsApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_complex_relation**](ComplexRelationsApi.md#add_complex_relation) | **POST** /complexRelations | Adds new complex relation.
[**change_complex_relation**](ComplexRelationsApi.md#change_complex_relation) | **PATCH** /complexRelations/{complexRelationId} | Change the complex relation with the information that is present in the request.
[**export_to_csv**](ComplexRelationsApi.md#export_to_csv) | **POST** /complexRelations/export/csv-job | Export complex relations of the given type to CSV.
[**export_to_csv_as_string**](ComplexRelationsApi.md#export_to_csv_as_string) | **POST** /complexRelations/export/csv | Export all complex relations of the given type to CSV as a String.
[**export_to_csv_without_job**](ComplexRelationsApi.md#export_to_csv_without_job) | **POST** /complexRelations/export/csv-file | Export all complex relations of the given type to a CSV file.
[**export_to_excel**](ComplexRelationsApi.md#export_to_excel) | **POST** /complexRelations/export/excel-job | Export complex relations of the given type to Excel.
[**export_to_excel_without_job**](ComplexRelationsApi.md#export_to_excel_without_job) | **POST** /complexRelations/export/excel-file | Export all complex relations of the given type to an Excel file.
[**find_complex_relations**](ComplexRelationsApi.md#find_complex_relations) | **GET** /complexRelations | Returns complex relations matching the given search criteria.
[**get_complex_relation**](ComplexRelationsApi.md#get_complex_relation) | **GET** /complexRelations/{complexRelationId} | Returns a ComplexRelation identified by given id.
[**remove_complex_relation**](ComplexRelationsApi.md#remove_complex_relation) | **DELETE** /complexRelations/{complexRelationId} | Removes complex relation identified by given id.


# **add_complex_relation**
> ComplexRelationImpl add_complex_relation(add_complex_relation_request=add_complex_relation_request)

Adds new complex relation.

Adds new complex relation.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    add_complex_relation_request = collibra_core.AddComplexRelationRequest() # AddComplexRelationRequest |  (optional)

    try:
        # Adds new complex relation.
        api_response = api_instance.add_complex_relation(add_complex_relation_request=add_complex_relation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->add_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_complex_relation_request** | [**AddComplexRelationRequest**](AddComplexRelationRequest.md)|  | [optional] 

### Return type

[**ComplexRelationImpl**](ComplexRelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Complex relation successfully added. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_complex_relation**
> ComplexRelationImpl change_complex_relation(complex_relation_id, change_complex_relation_request=change_complex_relation_request)

Change the complex relation with the information that is present in the request.

Change the complex relation with the information that is present in the request.  Only properties that are specified in this request and have not <code>null</code> values are updated.  All other properties are ignored.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    complex_relation_id = 'complex_relation_id_example' # str | the id of the complex relation to be modified.
change_complex_relation_request = collibra_core.ChangeComplexRelationRequest() # ChangeComplexRelationRequest |  (optional)

    try:
        # Change the complex relation with the information that is present in the request.
        api_response = api_instance.change_complex_relation(complex_relation_id, change_complex_relation_request=change_complex_relation_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->change_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | [**str**](.md)| the id of the complex relation to be modified. | 
 **change_complex_relation_request** | [**ChangeComplexRelationRequest**](ChangeComplexRelationRequest.md)|  | [optional] 

### Return type

[**ComplexRelationImpl**](ComplexRelationImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_csv**
> Job export_to_csv(export_complex_relations_to_csv_request=export_complex_relations_to_csv_request)

Export complex relations of the given type to CSV.

Export complex relations of the given type to CSV.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    export_complex_relations_to_csv_request = collibra_core.ExportComplexRelationsToCSVRequest() # ExportComplexRelationsToCSVRequest |  (optional)

    try:
        # Export complex relations of the given type to CSV.
        api_response = api_instance.export_to_csv(export_complex_relations_to_csv_request=export_complex_relations_to_csv_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->export_to_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_complex_relations_to_csv_request** | [**ExportComplexRelationsToCSVRequest**](ExportComplexRelationsToCSVRequest.md)|  | [optional] 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_csv_as_string**
> str export_to_csv_as_string(export_complex_relations_to_csv_request=export_complex_relations_to_csv_request)

Export all complex relations of the given type to CSV as a String.

Export all complex relations of the given type to CSV as a String.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    export_complex_relations_to_csv_request = collibra_core.ExportComplexRelationsToCSVRequest() # ExportComplexRelationsToCSVRequest |  (optional)

    try:
        # Export all complex relations of the given type to CSV as a String.
        api_response = api_instance.export_to_csv_as_string(export_complex_relations_to_csv_request=export_complex_relations_to_csv_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->export_to_csv_as_string: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_complex_relations_to_csv_request** | [**ExportComplexRelationsToCSVRequest**](ExportComplexRelationsToCSVRequest.md)|  | [optional] 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_csv_without_job**
> FileInfoImpl export_to_csv_without_job(export_complex_relations_to_csv_request=export_complex_relations_to_csv_request)

Export all complex relations of the given type to a CSV file.

Export all complex relations of the given type to a CSV file.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    export_complex_relations_to_csv_request = collibra_core.ExportComplexRelationsToCSVRequest() # ExportComplexRelationsToCSVRequest |  (optional)

    try:
        # Export all complex relations of the given type to a CSV file.
        api_response = api_instance.export_to_csv_without_job(export_complex_relations_to_csv_request=export_complex_relations_to_csv_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->export_to_csv_without_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_complex_relations_to_csv_request** | [**ExportComplexRelationsToCSVRequest**](ExportComplexRelationsToCSVRequest.md)|  | [optional] 

### Return type

[**FileInfoImpl**](FileInfoImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_excel**
> Job export_to_excel(export_complex_relations_to_excel_request=export_complex_relations_to_excel_request)

Export complex relations of the given type to Excel.

Export complex relations of the given type to Excel.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    export_complex_relations_to_excel_request = collibra_core.ExportComplexRelationsToExcelRequest() # ExportComplexRelationsToExcelRequest |  (optional)

    try:
        # Export complex relations of the given type to Excel.
        api_response = api_instance.export_to_excel(export_complex_relations_to_excel_request=export_complex_relations_to_excel_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->export_to_excel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_complex_relations_to_excel_request** | [**ExportComplexRelationsToExcelRequest**](ExportComplexRelationsToExcelRequest.md)|  | [optional] 

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
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_to_excel_without_job**
> FileInfoImpl export_to_excel_without_job(export_complex_relations_to_excel_request=export_complex_relations_to_excel_request)

Export all complex relations of the given type to an Excel file.

Export all complex relations of the given type to an Excel file.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    export_complex_relations_to_excel_request = collibra_core.ExportComplexRelationsToExcelRequest() # ExportComplexRelationsToExcelRequest |  (optional)

    try:
        # Export all complex relations of the given type to an Excel file.
        api_response = api_instance.export_to_excel_without_job(export_complex_relations_to_excel_request=export_complex_relations_to_excel_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->export_to_excel_without_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **export_complex_relations_to_excel_request** | [**ExportComplexRelationsToExcelRequest**](ExportComplexRelationsToExcelRequest.md)|  | [optional] 

### Return type

[**FileInfoImpl**](FileInfoImpl.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**0** | default response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_complex_relations**
> PagedResponseComplexRelation find_complex_relations(offset=offset, limit=limit, asset_id=asset_id, type_id=type_id)

Returns complex relations matching the given search criteria.

Returns complex relations matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering.  All other parameters are ignored.  The returned complex relations satisfy all constraints that are specified in this search criteria.  By default a result containing 1000 complex relations is returned.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
asset_id = 'asset_id_example' # str | The ID of the asset for which complex relations should be found. (optional)
type_id = 'type_id_example' # str | The ID of the type of complex relations to search for. (optional)

    try:
        # Returns complex relations matching the given search criteria.
        api_response = api_instance.find_complex_relations(offset=offset, limit=limit, asset_id=asset_id, type_id=type_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->find_complex_relations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **asset_id** | [**str**](.md)| The ID of the asset for which complex relations should be found. | [optional] 
 **type_id** | [**str**](.md)| The ID of the type of complex relations to search for. | [optional] 

### Return type

[**PagedResponseComplexRelation**](PagedResponseComplexRelation.md)

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

# **get_complex_relation**
> ComplexRelationImpl get_complex_relation(complex_relation_id)

Returns a ComplexRelation identified by given id.

Returns a complex relation identified by given <code>id</code>.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    complex_relation_id = 'complex_relation_id_example' # str | the id of the complex relation.

    try:
        # Returns a ComplexRelation identified by given id.
        api_response = api_instance.get_complex_relation(complex_relation_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->get_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | [**str**](.md)| the id of the complex relation. | 

### Return type

[**ComplexRelationImpl**](ComplexRelationImpl.md)

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

# **remove_complex_relation**
> remove_complex_relation(complex_relation_id)

Removes complex relation identified by given id.

Removes complex relation identified by given id.

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
    api_instance = collibra_core.ComplexRelationsApi(api_client)
    complex_relation_id = 'complex_relation_id_example' # str | the id of the complex relation to be removed.

    try:
        # Removes complex relation identified by given id.
        api_instance.remove_complex_relation(complex_relation_id)
    except ApiException as e:
        print("Exception when calling ComplexRelationsApi->remove_complex_relation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **complex_relation_id** | [**str**](.md)| the id of the complex relation to be removed. | 

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

