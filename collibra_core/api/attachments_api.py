# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from collibra_core.api_client import ApiClient
from collibra_core.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AttachmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_attachment(self, **kwargs):  # noqa: E501
        """Add attachment  # noqa: E501

        Adds new attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_attachment(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: the file - attachment content
        :param str file_name: the display name of the file of this attachment
        :param str resource_type: the type of the resource the attachment should refer to
        :param str resource_id: the id of the resource the attachment should refer to
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AttachmentImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_attachment_with_http_info(**kwargs)  # noqa: E501

    def add_attachment_with_http_info(self, **kwargs):  # noqa: E501
        """Add attachment  # noqa: E501

        Adds new attachment.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_attachment_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file file: the file - attachment content
        :param str file_name: the display name of the file of this attachment
        :param str resource_type: the type of the resource the attachment should refer to
        :param str resource_id: the id of the resource the attachment should refer to
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AttachmentImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'file',
            'file_name',
            'resource_type',
            'resource_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_attachment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in local_var_params:
            local_var_files['file'] = local_var_params['file']  # noqa: E501
        if 'file_name' in local_var_params:
            form_params.append(('fileName', local_var_params['file_name']))  # noqa: E501
        if 'resource_type' in local_var_params:
            form_params.append(('resourceType', local_var_params['resource_type']))  # noqa: E501
        if 'resource_id' in local_var_params:
            form_params.append(('resourceId', local_var_params['resource_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/attachments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AttachmentImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_attachments(self, **kwargs):  # noqa: E501
        """Find attachments  # noqa: E501

        Returns attachments matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attachments satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attachments is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_attachments(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str file_name: The name of the file representing searched attachment.
        :param str file_content_type: The type of the content of the file representing searched attachment.
        :param int upload_date: The date of attachment upload. It is the timestamp (in UTC time standard).
        :param str user_id: The ID of the user who uploaded the attachment.
        :param str base_resource_id: The ID of the resource the attachment refers to.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AttachmentPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_attachments_with_http_info(**kwargs)  # noqa: E501

    def find_attachments_with_http_info(self, **kwargs):  # noqa: E501
        """Find attachments  # noqa: E501

        Returns attachments matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned attachments satisfy all constraints that are specified in this search criteria. By default a result containing 1000 attachments is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_attachments_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str file_name: The name of the file representing searched attachment.
        :param str file_content_type: The type of the content of the file representing searched attachment.
        :param int upload_date: The date of attachment upload. It is the timestamp (in UTC time standard).
        :param str user_id: The ID of the user who uploaded the attachment.
        :param str base_resource_id: The ID of the resource the attachment refers to.
        :param str sort_field: The field that should be used as reference for sorting.
        :param str sort_order: The order of sorting.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AttachmentPagedResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'file_name',
            'file_content_type',
            'upload_date',
            'user_id',
            'base_resource_id',
            'sort_field',
            'sort_order'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method find_attachments" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'offset' in local_var_params and local_var_params['offset'] is not None:  # noqa: E501
            query_params.append(('offset', local_var_params['offset']))  # noqa: E501
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'file_name' in local_var_params and local_var_params['file_name'] is not None:  # noqa: E501
            query_params.append(('fileName', local_var_params['file_name']))  # noqa: E501
        if 'file_content_type' in local_var_params and local_var_params['file_content_type'] is not None:  # noqa: E501
            query_params.append(('fileContentType', local_var_params['file_content_type']))  # noqa: E501
        if 'upload_date' in local_var_params and local_var_params['upload_date'] is not None:  # noqa: E501
            query_params.append(('uploadDate', local_var_params['upload_date']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('userId', local_var_params['user_id']))  # noqa: E501
        if 'base_resource_id' in local_var_params and local_var_params['base_resource_id'] is not None:  # noqa: E501
            query_params.append(('baseResourceId', local_var_params['base_resource_id']))  # noqa: E501
        if 'sort_field' in local_var_params and local_var_params['sort_field'] is not None:  # noqa: E501
            query_params.append(('sortField', local_var_params['sort_field']))  # noqa: E501
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/attachments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AttachmentPagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_attachment(self, attachment_id, **kwargs):  # noqa: E501
        """Get attachment  # noqa: E501

        Returns information about the attachment identified by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str attachment_id: the id of the attachment (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: AttachmentImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_attachment_with_http_info(attachment_id, **kwargs)  # noqa: E501

    def get_attachment_with_http_info(self, attachment_id, **kwargs):  # noqa: E501
        """Get attachment  # noqa: E501

        Returns information about the attachment identified by id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_with_http_info(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str attachment_id: the id of the attachment (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(AttachmentImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'attachment_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attachment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'attachment_id' is set
        if self.api_client.client_side_validation and ('attachment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['attachment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `attachment_id` when calling `get_attachment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'attachment_id' in local_var_params:
            path_params['attachmentId'] = local_var_params['attachment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/attachments/{attachmentId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AttachmentImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_attachment_content(self, attachment_id, **kwargs):  # noqa: E501
        """Get attachment content  # noqa: E501

        Returns content of the attachment identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_content(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str attachment_id: the id of the attachment (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_attachment_content_with_http_info(attachment_id, **kwargs)  # noqa: E501

    def get_attachment_content_with_http_info(self, attachment_id, **kwargs):  # noqa: E501
        """Get attachment content  # noqa: E501

        Returns content of the attachment identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_attachment_content_with_http_info(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str attachment_id: the id of the attachment (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'attachment_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_attachment_content" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'attachment_id' is set
        if self.api_client.client_side_validation and ('attachment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['attachment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `attachment_id` when calling `get_attachment_content`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'attachment_id' in local_var_params:
            path_params['attachmentId'] = local_var_params['attachment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/attachments/{attachmentId}/file', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_attachment(self, attachment_id, **kwargs):  # noqa: E501
        """Remove attachment  # noqa: E501

        Removes attachment identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_attachment(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str attachment_id: the id of the attachment (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.remove_attachment_with_http_info(attachment_id, **kwargs)  # noqa: E501

    def remove_attachment_with_http_info(self, attachment_id, **kwargs):  # noqa: E501
        """Remove attachment  # noqa: E501

        Removes attachment identified by given id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_attachment_with_http_info(attachment_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str attachment_id: the id of the attachment (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'attachment_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method remove_attachment" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'attachment_id' is set
        if self.api_client.client_side_validation and ('attachment_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['attachment_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `attachment_id` when calling `remove_attachment`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'attachment_id' in local_var_params:
            path_params['attachmentId'] = local_var_params['attachment_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/attachments/{attachmentId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)