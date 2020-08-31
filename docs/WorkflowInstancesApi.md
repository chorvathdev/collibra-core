# collibra_core.WorkflowInstancesApi

All URIs are relative to *http://localhost/rest/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_workflow_instances**](WorkflowInstancesApi.md#cancel_workflow_instances) | **POST** /workflowInstances/{workflowInstanceId}/canceled | Cancel workflow instance.
[**find_workflow_instances**](WorkflowInstancesApi.md#find_workflow_instances) | **GET** /workflowInstances | Find workflow instances.
[**get_workflow_instance_diagram**](WorkflowInstancesApi.md#get_workflow_instance_diagram) | **GET** /workflowInstances/{workflowInstanceId}/diagram | Returns the file representing the diagram of workflow instance identified by the given ID.
[**message_event_received**](WorkflowInstancesApi.md#message_event_received) | **POST** /workflowInstances/{processInstanceId}/messageEvents/{messageName} | Pass message event to workflow engine.
[**start_workflow_instances**](WorkflowInstancesApi.md#start_workflow_instances) | **POST** /workflowInstances | Start workflow instances.
[**start_workflow_instances_in_job**](WorkflowInstancesApi.md#start_workflow_instances_in_job) | **POST** /workflowInstances/startJobs | Start workflow instances.


# **cancel_workflow_instances**
> cancel_workflow_instances(workflow_instance_id, body=body)

Cancel workflow instance.

Cancels the workflow instance with the specified ID with a reason. Canceling the workflow instance also cancels the workflow sub-processes.

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
    api_instance = collibra_core.WorkflowInstancesApi(api_client)
    workflow_instance_id = 'workflow_instance_id_example' # str | The identifier of the workflow instance to be cancelled.
body = 'body_example' # str | The reason for the cancellation of the workflow instance. (optional)

    try:
        # Cancel workflow instance.
        api_instance.cancel_workflow_instances(workflow_instance_id, body=body)
    except ApiException as e:
        print("Exception when calling WorkflowInstancesApi->cancel_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | [**str**](.md)| The identifier of the workflow instance to be cancelled. | 
 **body** | **str**| The reason for the cancellation of the workflow instance. | [optional] 

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
**204** | The workflow instance has been successfully canceled. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workflow_instances**
> PagedResponse find_workflow_instances(offset=offset, limit=limit, business_item_name=business_item_name, business_item_id=business_item_id, workflow_definition_id=workflow_definition_id, sort_field=sort_field, sort_order=sort_order)

Find workflow instances.

Returns workflow instances matching given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned workflow instances satisfy all constraints that are specified in this search criteria.

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
    api_instance = collibra_core.WorkflowInstancesApi(api_client)
    offset = 0 # int | The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>. (optional) (default to 0)
limit = 0 # int | The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used. (optional) (default to 0)
business_item_name = 'business_item_name_example' # str | The display name of the business item that should be contained by the searched workflows. (optional)
business_item_id = 'business_item_id_example' # str | The ID of the business item that should be contained by the searched workflows. (optional)
workflow_definition_id = 'workflow_definition_id_example' # str | The ID of the workflow definition. (optional)
sort_field = 'START_DATE' # str | The field on which the results are sorted. (optional) (default to 'START_DATE')
sort_order = 'DESC' # str | The sorting order. (optional) (default to 'DESC')

    try:
        # Find workflow instances.
        api_response = api_instance.find_workflow_instances(offset=offset, limit=limit, business_item_name=business_item_name, business_item_id=business_item_id, workflow_definition_id=workflow_definition_id, sort_field=sort_field, sort_order=sort_order)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowInstancesApi->find_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The first result to retrieve. If not set (offset &#x3D; &lt;code&gt;0&lt;/code&gt;), results will be retrieved starting from row &lt;code&gt;0&lt;/code&gt;. | [optional] [default to 0]
 **limit** | **int**| The maximum number of results to retrieve. If not set (limit &#x3D; &lt;code&gt;0&lt;/code&gt;), the default limit will be used. | [optional] [default to 0]
 **business_item_name** | **str**| The display name of the business item that should be contained by the searched workflows. | [optional] 
 **business_item_id** | [**str**](.md)| The ID of the business item that should be contained by the searched workflows. | [optional] 
 **workflow_definition_id** | **str**| The ID of the workflow definition. | [optional] 
 **sort_field** | **str**| The field on which the results are sorted. | [optional] [default to &#39;START_DATE&#39;]
 **sort_order** | **str**| The sorting order. | [optional] [default to &#39;DESC&#39;]

### Return type

[**PagedResponse**](PagedResponse.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The found workflow instances. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workflow_instance_diagram**
> object get_workflow_instance_diagram(workflow_instance_id)

Returns the file representing the diagram of workflow instance identified by the given ID.

Returns the file representing the diagram of workflow instance identified by the given ID. The diagram input stream returned can be null as deployed workflow defintions without graphical notation included don't have a diagram

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
    api_instance = collibra_core.WorkflowInstancesApi(api_client)
    workflow_instance_id = 'workflow_instance_id_example' # str | The ID of the workflow instance to return the diagram for.

    try:
        # Returns the file representing the diagram of workflow instance identified by the given ID.
        api_response = api_instance.get_workflow_instance_diagram(workflow_instance_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowInstancesApi->get_workflow_instance_diagram: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workflow_instance_id** | [**str**](.md)| The ID of the workflow instance to return the diagram for. | 

### Return type

**object**

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The input stream containing the diagram of the workflow instance. |  -  |
**204** | No diagram has been found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **message_event_received**
> message_event_received(process_instance_id, message_name, message_event_received_request=message_event_received_request)

Pass message event to workflow engine.

Passes the message event to the workflow engine. It will pass on this specific event to the engine with the given name, process instance and variables.

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
    api_instance = collibra_core.WorkflowInstancesApi(api_client)
    process_instance_id = 'process_instance_id_example' # str | The ID of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail.
message_name = 'message_name_example' # str | The name of the message to trigger.
message_event_received_request = collibra_core.MessageEventReceivedRequest() # MessageEventReceivedRequest | The properties of the message event to be received. (optional)

    try:
        # Pass message event to workflow engine.
        api_instance.message_event_received(process_instance_id, message_name, message_event_received_request=message_event_received_request)
    except ApiException as e:
        print("Exception when calling WorkflowInstancesApi->message_event_received: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **process_instance_id** | **str**| The ID of an instance of a process. Given process instance should have only one execution running at the time. Otherwise this method will fail. | 
 **message_name** | **str**| The name of the message to trigger. | 
 **message_event_received_request** | [**MessageEventReceivedRequest**](MessageEventReceivedRequest.md)| The properties of the message event to be received. | [optional] 

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
**204** | The message event has been successfully passed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_workflow_instances**
> list[WorkflowInstance] start_workflow_instances(start_workflow_instances_request=start_workflow_instances_request)

Start workflow instances.

Starts multiple workflow instances based on the provided request.

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
    api_instance = collibra_core.WorkflowInstancesApi(api_client)
    start_workflow_instances_request = collibra_core.StartWorkflowInstancesRequest() # StartWorkflowInstancesRequest | The properties of the workflow to be started. (optional)

    try:
        # Start workflow instances.
        api_response = api_instance.start_workflow_instances(start_workflow_instances_request=start_workflow_instances_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowInstancesApi->start_workflow_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_workflow_instances_request** | [**StartWorkflowInstancesRequest**](StartWorkflowInstancesRequest.md)| The properties of the workflow to be started. | [optional] 

### Return type

[**list[WorkflowInstance]**](WorkflowInstance.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Workflow instances successfully started. |  -  |
**404** | Workflow definition could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_workflow_instances_in_job**
> Job start_workflow_instances_in_job(start_workflow_instances_request=start_workflow_instances_request)

Start workflow instances.

Starts multiple workflow instances asynchronously based on the provided request.

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
    api_instance = collibra_core.WorkflowInstancesApi(api_client)
    start_workflow_instances_request = collibra_core.StartWorkflowInstancesRequest() # StartWorkflowInstancesRequest | Properties of the workflow to be started. (optional)

    try:
        # Start workflow instances.
        api_response = api_instance.start_workflow_instances_in_job(start_workflow_instances_request=start_workflow_instances_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling WorkflowInstancesApi->start_workflow_instances_in_job: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_workflow_instances_request** | [**StartWorkflowInstancesRequest**](StartWorkflowInstancesRequest.md)| Properties of the workflow to be started. | [optional] 

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
**200** | Workflow instances successfully started. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

