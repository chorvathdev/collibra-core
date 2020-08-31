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


class ComplexRelationTypesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_complex_relation_type(self, **kwargs):  # noqa: E501
        """Adds a new complex relation type.  # noqa: E501

        Adds a new complex relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_complex_relation_type(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddComplexRelationTypeRequest add_complex_relation_type_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ComplexRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_complex_relation_type_with_http_info(**kwargs)  # noqa: E501

    def add_complex_relation_type_with_http_info(self, **kwargs):  # noqa: E501
        """Adds a new complex relation type.  # noqa: E501

        Adds a new complex relation type.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_complex_relation_type_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddComplexRelationTypeRequest add_complex_relation_type_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ComplexRelationTypeImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'add_complex_relation_type_request'
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
                    " to method add_complex_relation_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add_complex_relation_type_request' in local_var_params:
            body_params = local_var_params['add_complex_relation_type_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/complexRelationTypes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComplexRelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_complex_relation_type(self, complex_relation_type_id, **kwargs):  # noqa: E501
        """Changes the complex relation type.  # noqa: E501

        Changes the complex relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_complex_relation_type(complex_relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str complex_relation_type_id: the unique identifier of the complex relation type (required)
        :param ChangeComplexRelationTypeRequest change_complex_relation_type_request:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ComplexRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.change_complex_relation_type_with_http_info(complex_relation_type_id, **kwargs)  # noqa: E501

    def change_complex_relation_type_with_http_info(self, complex_relation_type_id, **kwargs):  # noqa: E501
        """Changes the complex relation type.  # noqa: E501

        Changes the complex relation type with the information that is present in the request. Only properties that are specified in this request and have not <code>null</code> values are updated. All other properties are ignored.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_complex_relation_type_with_http_info(complex_relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str complex_relation_type_id: the unique identifier of the complex relation type (required)
        :param ChangeComplexRelationTypeRequest change_complex_relation_type_request:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ComplexRelationTypeImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'complex_relation_type_id',
            'change_complex_relation_type_request'
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
                    " to method change_complex_relation_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'complex_relation_type_id' is set
        if self.api_client.client_side_validation and ('complex_relation_type_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['complex_relation_type_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `complex_relation_type_id` when calling `change_complex_relation_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'complex_relation_type_id' in local_var_params:
            path_params['complexRelationTypeId'] = local_var_params['complex_relation_type_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'change_complex_relation_type_request' in local_var_params:
            body_params = local_var_params['change_complex_relation_type_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/complexRelationTypes/{complexRelationTypeId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComplexRelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_complex_relation_types(self, **kwargs):  # noqa: E501
        """Returns complex relation types matching the given search criteria.  # noqa: E501

        Returns complex relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned complex relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 complex relation types is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_complex_relation_types(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str name: The name of the complex relation type to search for.
        :param str name_match_mode: The match mode used to compare <code>name</code>.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ComplexRelationTypePagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_complex_relation_types_with_http_info(**kwargs)  # noqa: E501

    def find_complex_relation_types_with_http_info(self, **kwargs):  # noqa: E501
        """Returns complex relation types matching the given search criteria.  # noqa: E501

        Returns complex relation types matching the given search criteria. Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored. The returned complex relation types satisfy all constraints that are specified in this search criteria. By default a result containing 1000 complex relation types is returned.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_complex_relation_types_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str name: The name of the complex relation type to search for.
        :param str name_match_mode: The match mode used to compare <code>name</code>.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ComplexRelationTypePagedResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'name',
            'name_match_mode'
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
                    " to method find_complex_relation_types" % key
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
        if 'name' in local_var_params and local_var_params['name'] is not None:  # noqa: E501
            query_params.append(('name', local_var_params['name']))  # noqa: E501
        if 'name_match_mode' in local_var_params and local_var_params['name_match_mode'] is not None:  # noqa: E501
            query_params.append(('nameMatchMode', local_var_params['name_match_mode']))  # noqa: E501

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
            '/complexRelationTypes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComplexRelationTypePagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_complex_relation_type(self, complex_relation_type_id, **kwargs):  # noqa: E501
        """Returns complex relation type identified by given UUID.  # noqa: E501

        Returns complex relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_complex_relation_type(complex_relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str complex_relation_type_id: the unique identifier of the complex relation type (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ComplexRelationTypeImpl
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_complex_relation_type_with_http_info(complex_relation_type_id, **kwargs)  # noqa: E501

    def get_complex_relation_type_with_http_info(self, complex_relation_type_id, **kwargs):  # noqa: E501
        """Returns complex relation type identified by given UUID.  # noqa: E501

        Returns complex relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_complex_relation_type_with_http_info(complex_relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str complex_relation_type_id: the unique identifier of the complex relation type (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ComplexRelationTypeImpl, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'complex_relation_type_id'
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
                    " to method get_complex_relation_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'complex_relation_type_id' is set
        if self.api_client.client_side_validation and ('complex_relation_type_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['complex_relation_type_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `complex_relation_type_id` when calling `get_complex_relation_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'complex_relation_type_id' in local_var_params:
            path_params['complexRelationTypeId'] = local_var_params['complex_relation_type_id']  # noqa: E501

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
            '/complexRelationTypes/{complexRelationTypeId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ComplexRelationTypeImpl',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_complex_relation_type(self, complex_relation_type_id, **kwargs):  # noqa: E501
        """Removes complex relation type identified by given UUID.  # noqa: E501

        Removes complex relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_complex_relation_type(complex_relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str complex_relation_type_id: the unique identifier of the complex relation type (required)
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
        return self.remove_complex_relation_type_with_http_info(complex_relation_type_id, **kwargs)  # noqa: E501

    def remove_complex_relation_type_with_http_info(self, complex_relation_type_id, **kwargs):  # noqa: E501
        """Removes complex relation type identified by given UUID.  # noqa: E501

        Removes complex relation type identified by given UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_complex_relation_type_with_http_info(complex_relation_type_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str complex_relation_type_id: the unique identifier of the complex relation type (required)
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
            'complex_relation_type_id'
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
                    " to method remove_complex_relation_type" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'complex_relation_type_id' is set
        if self.api_client.client_side_validation and ('complex_relation_type_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['complex_relation_type_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `complex_relation_type_id` when calling `remove_complex_relation_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'complex_relation_type_id' in local_var_params:
            path_params['complexRelationTypeId'] = local_var_params['complex_relation_type_id']  # noqa: E501

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
            '/complexRelationTypes/{complexRelationTypeId}', 'DELETE',
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
