# collibra_core.OutputModuleApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**export_csv**](OutputModuleApi.md#export_csv) | **POST** /outputModule/export/csv | Exports results in CSV format, returns the results immediately.
[**export_csv_in_job**](OutputModuleApi.md#export_csv_in_job) | **POST** /outputModule/export/csv-job | Exports results in CSV format, returns JSON representation of the async Job.
[**export_csv_to_file**](OutputModuleApi.md#export_csv_to_file) | **POST** /outputModule/export/csv-file | Exports results in CSV format, returns information about created file.
[**export_excel_in_job**](OutputModuleApi.md#export_excel_in_job) | **POST** /outputModule/export/excel-job | Exports results in Excel format, returns JSON representation of the async Job.
[**export_excel_to_file**](OutputModuleApi.md#export_excel_to_file) | **POST** /outputModule/export/excel-file | Exports results in Excel format, returns information about created file.
[**export_json**](OutputModuleApi.md#export_json) | **POST** /outputModule/export/json | Exports results in JSON format, returns the results immediately.
[**export_json_in_job**](OutputModuleApi.md#export_json_in_job) | **POST** /outputModule/export/json-job | Exports results in JSON format, returns JSON representation of the async Job.
[**export_json_to_file**](OutputModuleApi.md#export_json_to_file) | **POST** /outputModule/export/json-file | Exports results in JSON format, returns information about created file.
[**export_xml**](OutputModuleApi.md#export_xml) | **POST** /outputModule/export/xml | Exports results in XML format, returns the results immediately.
[**export_xml_in_job**](OutputModuleApi.md#export_xml_in_job) | **POST** /outputModule/export/xml-job | Exports results in XML format, returns JSON representation of the async Job.
[**export_xml_to_file**](OutputModuleApi.md#export_xml_to_file) | **POST** /outputModule/export/xml-file | Exports results in XML format, returns information about created file.
[**get_table_view_config_by_view_id**](OutputModuleApi.md#get_table_view_config_by_view_id) | **GET** /outputModule/tableViewConfigs/viewId/{viewId} | Returns TableViewConfig based on id of given View and its Location.


# **export_csv**
> export_csv(validation_enabled=validation_enabled, separator=separator, quote=quote, escape=escape, header_row=header_row, body=body)

Exports results in CSV format, returns the results immediately.

<p>Performs an Output Module query and exports the results immediately in CSV format.</p><p>Please note that the TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the TableViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is <code>false</code> for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
separator = 'separator_example' # str | The delimiter character used to separate entries. Default value is <code>';'</code>. (optional)
quote = 'quote_example' # str | The delimiter character used for quoted entries. Default value  is <code>'\"'</code>. (optional)
escape = 'escape_example' # str | The delimiter character used to escape separator or quote character. Default value is <code>'\\\\'</code>. (optional)
header_row = True # bool | Whether a response should include a header (<code>true</code>) or not (<code>false</code>). Default value is <code>true</code>. (optional) (default to True)
body = 'body_example' # str | The JSON representation of TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in CSV format, returns the results immediately.
        api_instance.export_csv(validation_enabled=validation_enabled, separator=separator, quote=quote, escape=escape, header_row=header_row, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_csv: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the TableViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is &lt;code&gt;false&lt;/code&gt; for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **separator** | **str**| The delimiter character used to separate entries. Default value is &lt;code&gt;&#39;;&#39;&lt;/code&gt;. | [optional] 
 **quote** | **str**| The delimiter character used for quoted entries. Default value  is &lt;code&gt;&#39;\&quot;&#39;&lt;/code&gt;. | [optional] 
 **escape** | **str**| The delimiter character used to escape separator or quote character. Default value is &lt;code&gt;&#39;\\\\&#39;&lt;/code&gt;. | [optional] 
 **header_row** | **bool**| Whether a response should include a header (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is &lt;code&gt;true&lt;/code&gt;. | [optional] [default to True]
 **body** | **str**| The JSON representation of TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The string response in CSV format. |  -  |
**400** | The parameter is invalid JSON TableViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_csv_in_job**
> export_csv_in_job(validation_enabled=validation_enabled, file_name=file_name, separator=separator, quote=quote, escape=escape, header_row=header_row, send_notification=send_notification, body=body)

Exports results in CSV format, returns JSON representation of the async Job.

<p>Starts a job that performs an Output Module query and stores the results in a file in CSV format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.</p><p>Please note that the TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the TableViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
separator = 'separator_example' # str | The delimiter character used to separate entries. Default value is <code>';'</code>. (optional)
quote = 'quote_example' # str | The delimiter character used for quoted entries. Default value  is <code>'\"'</code>. (optional)
escape = 'escape_example' # str | The delimiter character used to escape separator or quote character. Default value is <code>'\\\\'</code>. (optional)
header_row = True # bool | Whether a response should include a header (<code>true</code>) or not (<code>false</code>). Default value is <code>true</code>. (optional) (default to True)
send_notification = False # bool | Whether an e-mail must be sent on completion of the job. (optional) (default to False)
body = 'body_example' # str | The JSON representation of TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in CSV format, returns JSON representation of the async Job.
        api_instance.export_csv_in_job(validation_enabled=validation_enabled, file_name=file_name, separator=separator, quote=quote, escape=escape, header_row=header_row, send_notification=send_notification, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_csv_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the TableViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **separator** | **str**| The delimiter character used to separate entries. Default value is &lt;code&gt;&#39;;&#39;&lt;/code&gt;. | [optional] 
 **quote** | **str**| The delimiter character used for quoted entries. Default value  is &lt;code&gt;&#39;\&quot;&#39;&lt;/code&gt;. | [optional] 
 **escape** | **str**| The delimiter character used to escape separator or quote character. Default value is &lt;code&gt;&#39;\\\\&#39;&lt;/code&gt;. | [optional] 
 **header_row** | **bool**| Whether a response should include a header (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is &lt;code&gt;true&lt;/code&gt;. | [optional] [default to True]
 **send_notification** | **bool**| Whether an e-mail must be sent on completion of the job. | [optional] [default to False]
 **body** | **str**| The JSON representation of TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON representation of the job that performs an Output Module query. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_csv_to_file**
> export_csv_to_file(validation_enabled=validation_enabled, file_name=file_name, separator=separator, quote=quote, escape=escape, header_row=header_row, body=body)

Exports results in CSV format, returns information about created file.

<p>Performs an Output Module query and stores the query results in a file in CSV format. The id of the file is returned in the response.</p><p>Please note that the TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the TableViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated (optional)
separator = 'separator_example' # str | The delimiter character used to separate entries. Default value is <code>';'</code> (optional)
quote = 'quote_example' # str | The delimiter character used for quoted entries. Default value  is <code>'\"'</code> (optional)
escape = 'escape_example' # str | The delimiter character used to escape separator or quote character. Default value is <code>'\\\\'</code> (optional)
header_row = True # bool | Whether a response should include a header (<code>true</code>) or not (<code>false</code>). Default value is <code>true</code> (optional) (default to True)
body = 'body_example' # str | The JSON representation of TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in CSV format, returns information about created file.
        api_instance.export_csv_to_file(validation_enabled=validation_enabled, file_name=file_name, separator=separator, quote=quote, escape=escape, header_row=header_row, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_csv_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the TableViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated | [optional] 
 **separator** | **str**| The delimiter character used to separate entries. Default value is &lt;code&gt;&#39;;&#39;&lt;/code&gt; | [optional] 
 **quote** | **str**| The delimiter character used for quoted entries. Default value  is &lt;code&gt;&#39;\&quot;&#39;&lt;/code&gt; | [optional] 
 **escape** | **str**| The delimiter character used to escape separator or quote character. Default value is &lt;code&gt;&#39;\\\\&#39;&lt;/code&gt; | [optional] 
 **header_row** | **bool**| Whether a response should include a header (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is &lt;code&gt;true&lt;/code&gt; | [optional] [default to True]
 **body** | **str**| The JSON representation of TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about the file where the results are stored. |  -  |
**400** | The parameter is invalid JSON TableViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_excel_in_job**
> export_excel_in_job(send_notification=send_notification, validation_enabled=validation_enabled, file_name=file_name, sheet_name=sheet_name, use_xlsx=use_xlsx, header_row=header_row, body=body)

Exports results in Excel format, returns JSON representation of the async Job.

<p>Starts a job that performs an Output Module query and stores the results in a file in Excel format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.</p></p>Please note that the TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    send_notification = False # bool | Whether an e-mail must be sent on completion of the job. (optional) (default to False)
validation_enabled = False # bool | Determines if the TableViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated. (optional)
sheet_name = 'sheet_name_example' # str | The name of the sheet. By default no sheet name is set. (optional)
use_xlsx = True # bool | Whether the Excel file to export will be '.xlsx' file (<code>true</code>) or a '.xls' file (<code>false</code>. Default value is true.<br/>The parameter will be removed in the next major release. From the next major version only XLSX files will be supported.. (optional) (default to True)
header_row = True # bool | Whether a response should include a header (<code>true</code>) or not (<code>false</code>). Default value is <code>true</code>. (optional) (default to True)
body = 'body_example' # str | The JSON representation of TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in Excel format, returns JSON representation of the async Job.
        api_instance.export_excel_in_job(send_notification=send_notification, validation_enabled=validation_enabled, file_name=file_name, sheet_name=sheet_name, use_xlsx=use_xlsx, header_row=header_row, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_excel_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification** | **bool**| Whether an e-mail must be sent on completion of the job. | [optional] [default to False]
 **validation_enabled** | **bool**| Determines if the TableViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated. | [optional] 
 **sheet_name** | **str**| The name of the sheet. By default no sheet name is set. | [optional] 
 **use_xlsx** | **bool**| Whether the Excel file to export will be &#39;.xlsx&#39; file (&lt;code&gt;true&lt;/code&gt;) or a &#39;.xls&#39; file (&lt;code&gt;false&lt;/code&gt;. Default value is true.&lt;br/&gt;The parameter will be removed in the next major release. From the next major version only XLSX files will be supported.. | [optional] [default to True]
 **header_row** | **bool**| Whether a response should include a header (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is &lt;code&gt;true&lt;/code&gt;. | [optional] [default to True]
 **body** | **str**| The JSON representation of TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON representation of the job that performs an Output Module query. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_excel_to_file**
> export_excel_to_file(validation_enabled=validation_enabled, file_name=file_name, sheet_name=sheet_name, use_xlsx=use_xlsx, header_row=header_row, body=body)

Exports results in Excel format, returns information about created file.

<p>Performs an Output Module query and stores the query results in a file in Excel format. The id of the file is returned in the response.</p><p>Please note that the TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the TableViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated. (optional)
sheet_name = 'sheet_name_example' # str | The name of the sheet. By default no sheet name is set. (optional)
use_xlsx = True # bool | Whether the Excel file to export will be '.xlsx' file (<code>true</code>) or a '.xls' file (<code>false</code>. Default value is true.<br/>The parameter will be removed in the next major release. From the next major version only XLSX files will be supported. (optional) (default to True)
header_row = True # bool | Whether a response should include a header (<code>true</code>) or not (<code>false</code>). Default value is <code>true</code>. (optional) (default to True)
body = 'body_example' # str | The JSON representation of TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in Excel format, returns information about created file.
        api_instance.export_excel_to_file(validation_enabled=validation_enabled, file_name=file_name, sheet_name=sheet_name, use_xlsx=use_xlsx, header_row=header_row, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_excel_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the TableViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated. | [optional] 
 **sheet_name** | **str**| The name of the sheet. By default no sheet name is set. | [optional] 
 **use_xlsx** | **bool**| Whether the Excel file to export will be &#39;.xlsx&#39; file (&lt;code&gt;true&lt;/code&gt;) or a &#39;.xls&#39; file (&lt;code&gt;false&lt;/code&gt;. Default value is true.&lt;br/&gt;The parameter will be removed in the next major release. From the next major version only XLSX files will be supported. | [optional] [default to True]
 **header_row** | **bool**| Whether a response should include a header (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is &lt;code&gt;true&lt;/code&gt;. | [optional] [default to True]
 **body** | **str**| The JSON representation of TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about the file where the results are stored. |  -  |
**400** | The parameter is invalid JSON TableViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_json**
> export_json(validation_enabled=validation_enabled, body=body)

Exports results in JSON format, returns the results immediately.

<p>Performs an Output Module query and exports the returns results immediately in JSON format.</p><p>Please note that the ViewConfig/TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the ViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
body = 'body_example' # str | The JSON representation of ViewConfig/TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in JSON format, returns the results immediately.
        api_instance.export_json(validation_enabled=validation_enabled, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the ViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **body** | **str**| The JSON representation of ViewConfig/TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The string response in JSON format. |  -  |
**400** | The parameter is invalid JSON ViewConfig/TableViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_json_in_job**
> export_json_in_job(send_notification=send_notification, validation_enabled=validation_enabled, file_name=file_name, body=body)

Exports results in JSON format, returns JSON representation of the async Job.

<p>Starts a job that performs an Output Module query and stores the results in a file in JSON format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.</p><p>Please note that the ViewConfig/TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    send_notification = False # bool | Whether an e-mail must be sent on completion of the job. (optional) (default to False)
validation_enabled = False # bool | Determines if the ViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated. (optional)
body = 'body_example' # str | The JSON representation of ViewConfig/TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in JSON format, returns JSON representation of the async Job.
        api_instance.export_json_in_job(send_notification=send_notification, validation_enabled=validation_enabled, file_name=file_name, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_json_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_notification** | **bool**| Whether an e-mail must be sent on completion of the job. | [optional] [default to False]
 **validation_enabled** | **bool**| Determines if the ViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated. | [optional] 
 **body** | **str**| The JSON representation of ViewConfig/TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON representation of the job that performs an Output Module query. |  -  |
**400** | The parameter is invalid JSON ViewConfig/TableViewConfig. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_json_to_file**
> export_json_to_file(validation_enabled=validation_enabled, file_name=file_name, body=body)

Exports results in JSON format, returns information about created file.

<p>Performs an Output Module query and stores the query results in a file in JSON format. The id of the file is returned in the response.</p><p>Please note that the ViewConfig/TableViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the ViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated. (optional)
body = 'body_example' # str | The JSON representation of ViewConfig/TableViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in JSON format, returns information about created file.
        api_instance.export_json_to_file(validation_enabled=validation_enabled, file_name=file_name, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_json_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the ViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated. | [optional] 
 **body** | **str**| The JSON representation of ViewConfig/TableViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about the file where the results are stored. |  -  |
**400** | The parameter is invalid JSON ViewConfig/TableViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_xml**
> export_xml(validation_enabled=validation_enabled, body=body)

Exports results in XML format, returns the results immediately.

<p>Performs an Output Module query and exports the returns results immediately in XML format.</p><p>Please note that the ViewConfig’s syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results).For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the ViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
body = 'body_example' # str | The JSON representation of ViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in XML format, returns the results immediately.
        api_instance.export_xml(validation_enabled=validation_enabled, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the ViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **body** | **str**| The JSON representation of ViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The string response in XML format. |  -  |
**400** | The parameter is invalid JSON ViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_xml_in_job**
> export_xml_in_job(validation_enabled=validation_enabled, file_name=file_name, body=body)

Exports results in XML format, returns JSON representation of the async Job.

<p>Starts a job that performs an Output Module query and stores the results in a file in XML format. Id of the file can be retrieved from the <code>message.id</code> property of the job once the job is finished.</p><p>Please note that the ViewConfig's syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the ViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated. (optional)
body = 'body_example' # str | The JSON representation of ViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in XML format, returns JSON representation of the async Job.
        api_instance.export_xml_in_job(validation_enabled=validation_enabled, file_name=file_name, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_xml_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the ViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Validation is then performed immediately instead of only when the job is started. Please note that the validation will always take place during the Job execution, regardless of this parameter. Default value is false. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated. | [optional] 
 **body** | **str**| The JSON representation of ViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The JSON representation of the job that performs an Output Module query. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_xml_to_file**
> export_xml_to_file(validation_enabled=validation_enabled, file_name=file_name, body=body)

Exports results in XML format, returns information about created file.

<p>Performs an Output Module query and stores the query results in a file in XML format. The id of the file is returned in the response.</p><p>Please note that the ViewConfig's syntax validation is not executed by default, see <code>validationEnabled</code></p><p>DGC admin console settings may impact the execution of the query (especially in terms of timeout and a limit on the number of results). For details please consult output module documentation.</p>

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    validation_enabled = False # bool | Determines if the ViewConfig’s syntax should be validated (<code>true</code>) or not (<code>false</code>). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. (optional) (default to False)
file_name = 'file_name_example' # str | The name of the file. By default the file name will be generated. (optional)
body = 'body_example' # str | The JSON representation of ViewConfig that describes the query to be performed. (optional)

    try:
        # Exports results in XML format, returns information about created file.
        api_instance.export_xml_to_file(validation_enabled=validation_enabled, file_name=file_name, body=body)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->export_xml_to_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validation_enabled** | **bool**| Determines if the ViewConfig’s syntax should be validated (&lt;code&gt;true&lt;/code&gt;) or not (&lt;code&gt;false&lt;/code&gt;). Default value is false for backward compatibility reasons but it is strongly advised to always enable this validation. | [optional] [default to False]
 **file_name** | **str**| The name of the file. By default the file name will be generated. | [optional] 
 **body** | **str**| The JSON representation of ViewConfig that describes the query to be performed. | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The information about the file where the results are stored. |  -  |
**400** | The parameter is invalid JSON ViewConfig. |  -  |
**408** | Query execution time exceeded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_view_config_by_view_id**
> get_table_view_config_by_view_id(view_id, view_location=view_location)

Returns TableViewConfig based on id of given View and its Location.

<b>EXPERIMENTAL</b> Returns Table View Config based on id of given View and its Location. This Table View Config can be used by Output Module to export data as visible in Collibra Data Governance Center User Interface.<p>This endpoint does not guarantee a one-to-one relation between what is visible in the User Interface and what will be exported by using the provided Table View Config. Due to the possibility of adding additional filters through User Interface the result can contain more rows then are visible in the User Interface. In such case the Table View Config produced by this endpoint should be manually adjusted. <p><b>Because obtaining the correct results needs a human intervention, this endpoint should not be used in any kind of automatic processing.</b><p>Example: given page under url https://dgc.collibra.com/glossary?view=133f7f30-033c-4e38-acc2-2c1ac599d19e the view <code>id</code> is <code>133f7f30-033c-4e38-acc2-2c1ac599d19e</code>.

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
    api_instance = collibra_core.OutputModuleApi(api_client)
    view_id = 'view_id_example' # str | The <code>id</code> of given View. Can be obtained from Collibra Data Governance Center User Interface
view_location = 'view_location_example' # str | The Location for which the view shall be generated.Views in Collibra Data Governance Center are available under specific locations.Each location is associated with set of filters that are automatically applied to given view.Setting appropriate View Location will produce Table View Config that describes the data seen under desired location and given View in the best way possible.If this field is not provided then the returned Table View Config is going to have additional filters applied based on viewLocation extracted from database.`  <table><tr><th>viewLocation value </th><th> Corresponding view in Collibra Data Governance Center User Interface</th></tr><tr><td>BUSINESS_GLOSSARY_BUSINESS_ASSETS </td><td> Business Glossary Subpages: Business Assets (/glossary)Glossaries (/glossary/glossaries)</td></tr><tr><td>REFERENCE_DATA_CODEVALUES_AND_SETS </td><td> Reference Data > Code Values/Sets (/reference-data)</td></tr><tr><td>CATALOG_DATA_SETS </td><td> Catalog > Data Sets (/catalog/data-sets)</td><td><tr><td>CATALOG_DATA_DICTIONARY </td><td> Catalog > Data Dictionary (/catalog/data-dictionary)</td></tr><tr><td>CATALOG_TECHNOLOGY_ASSETS </td><td> Catalog > Technology Assets (/catalog/technology-assets)</td></tr><tr><td>DATA_HELPDESK_ISSUES </td><td> Data Helpdesk Subpages: Issues(/data-helpdesk)>Data Quality (/data-helpdesk/data-quality)</td></tr><tr><td>STEWARDSHIP_BUSINESS_DIMENSIONS </td><td> Stewardship > Business Dimensions (/stewardship/business-dimensions)</td></tr><tr><td>POLICY_MANAGER_GOVERNANCE_ASSETS </td><td> Policy Manager > Governance Assets (/policy-manager)</td></tr></table> (optional)

    try:
        # Returns TableViewConfig based on id of given View and its Location.
        api_instance.get_table_view_config_by_view_id(view_id, view_location=view_location)
    except ApiException as e:
        print("Exception when calling OutputModuleApi->get_table_view_config_by_view_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **view_id** | [**str**](.md)| The &lt;code&gt;id&lt;/code&gt; of given View. Can be obtained from Collibra Data Governance Center User Interface | 
 **view_location** | **str**| The Location for which the view shall be generated.Views in Collibra Data Governance Center are available under specific locations.Each location is associated with set of filters that are automatically applied to given view.Setting appropriate View Location will produce Table View Config that describes the data seen under desired location and given View in the best way possible.If this field is not provided then the returned Table View Config is going to have additional filters applied based on viewLocation extracted from database.&#x60;  &lt;table&gt;&lt;tr&gt;&lt;th&gt;viewLocation value &lt;/th&gt;&lt;th&gt; Corresponding view in Collibra Data Governance Center User Interface&lt;/th&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;BUSINESS_GLOSSARY_BUSINESS_ASSETS &lt;/td&gt;&lt;td&gt; Business Glossary Subpages: Business Assets (/glossary)Glossaries (/glossary/glossaries)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;REFERENCE_DATA_CODEVALUES_AND_SETS &lt;/td&gt;&lt;td&gt; Reference Data &gt; Code Values/Sets (/reference-data)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;CATALOG_DATA_SETS &lt;/td&gt;&lt;td&gt; Catalog &gt; Data Sets (/catalog/data-sets)&lt;/td&gt;&lt;td&gt;&lt;tr&gt;&lt;td&gt;CATALOG_DATA_DICTIONARY &lt;/td&gt;&lt;td&gt; Catalog &gt; Data Dictionary (/catalog/data-dictionary)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;CATALOG_TECHNOLOGY_ASSETS &lt;/td&gt;&lt;td&gt; Catalog &gt; Technology Assets (/catalog/technology-assets)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;DATA_HELPDESK_ISSUES &lt;/td&gt;&lt;td&gt; Data Helpdesk Subpages: Issues(/data-helpdesk)&gt;Data Quality (/data-helpdesk/data-quality)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;STEWARDSHIP_BUSINESS_DIMENSIONS &lt;/td&gt;&lt;td&gt; Stewardship &gt; Business Dimensions (/stewardship/business-dimensions)&lt;/td&gt;&lt;/tr&gt;&lt;tr&gt;&lt;td&gt;POLICY_MANAGER_GOVERNANCE_ASSETS &lt;/td&gt;&lt;td&gt; Policy Manager &gt; Governance Assets (/policy-manager)&lt;/td&gt;&lt;/tr&gt;&lt;/table&gt; | [optional] 

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
**200** | View config generated. |  -  |
**404** | View not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

