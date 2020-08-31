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


class RatingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_rating(self, **kwargs):  # noqa: E501
        """Add rating.  # noqa: E501

        Adds a new rating.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_rating(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddRatingRequest add_rating_request: The properties of the rating to be added.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Rating
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.add_rating_with_http_info(**kwargs)  # noqa: E501

    def add_rating_with_http_info(self, **kwargs):  # noqa: E501
        """Add rating.  # noqa: E501

        Adds a new rating.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_rating_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param AddRatingRequest add_rating_request: The properties of the rating to be added.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Rating, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'add_rating_request'
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
                    " to method add_rating" % key
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
        if 'add_rating_request' in local_var_params:
            body_params = local_var_params['add_rating_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/ratings', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rating',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def change_rating(self, rating_id, **kwargs):  # noqa: E501
        """Change rating.  # noqa: E501

        Modifies the rating with the specified ID.<p>Only properties that are specified in these requests and have not <code>null</code> values are updated. All other properties are ignored.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_rating(rating_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rating_id: The ID of the rating to be changed. (required)
        :param ChangeRatingRequest change_rating_request: The properties of the rating to be changed.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Rating
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.change_rating_with_http_info(rating_id, **kwargs)  # noqa: E501

    def change_rating_with_http_info(self, rating_id, **kwargs):  # noqa: E501
        """Change rating.  # noqa: E501

        Modifies the rating with the specified ID.<p>Only properties that are specified in these requests and have not <code>null</code> values are updated. All other properties are ignored.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.change_rating_with_http_info(rating_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rating_id: The ID of the rating to be changed. (required)
        :param ChangeRatingRequest change_rating_request: The properties of the rating to be changed.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Rating, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rating_id',
            'change_rating_request'
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
                    " to method change_rating" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rating_id' is set
        if self.api_client.client_side_validation and ('rating_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rating_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rating_id` when calling `change_rating`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rating_id' in local_var_params:
            path_params['ratingId'] = local_var_params['rating_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'change_rating_request' in local_var_params:
            body_params = local_var_params['change_rating_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/ratings/{ratingId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rating',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def find_ratings(self, **kwargs):  # noqa: E501
        """Find ratings.  # noqa: E501

        Returns ratings matching the given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p><p>The returned ratings satisfy all constraints that are specified in this search criteria. By default, the result contains up to 1000 ratings.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_ratings(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str sort_order: The order of sorting (on creation date) the found ratings.
        :param str asset_id: The ID of the asset the rating belongs to.
        :param str user_id: The ID of the rating author.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: RatingsPagedResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.find_ratings_with_http_info(**kwargs)  # noqa: E501

    def find_ratings_with_http_info(self, **kwargs):  # noqa: E501
        """Find ratings.  # noqa: E501

        Returns ratings matching the given search criteria.<p>Only parameters that are specified in this request and have not <code>null</code> values are used for filtering. All other parameters are ignored.</p><p>The returned ratings satisfy all constraints that are specified in this search criteria. By default, the result contains up to 1000 ratings.</p>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.find_ratings_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int offset: The first result to retrieve. If not set (offset = <code>0</code>), results will be retrieved starting from row <code>0</code>.
        :param int limit: The maximum number of results to retrieve. If not set (limit = <code>0</code>), the default limit will be used.
        :param str sort_order: The order of sorting (on creation date) the found ratings.
        :param str asset_id: The ID of the asset the rating belongs to.
        :param str user_id: The ID of the rating author.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(RatingsPagedResponse, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'offset',
            'limit',
            'sort_order',
            'asset_id',
            'user_id'
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
                    " to method find_ratings" % key
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
        if 'sort_order' in local_var_params and local_var_params['sort_order'] is not None:  # noqa: E501
            query_params.append(('sortOrder', local_var_params['sort_order']))  # noqa: E501
        if 'asset_id' in local_var_params and local_var_params['asset_id'] is not None:  # noqa: E501
            query_params.append(('assetId', local_var_params['asset_id']))  # noqa: E501
        if 'user_id' in local_var_params and local_var_params['user_id'] is not None:  # noqa: E501
            query_params.append(('userId', local_var_params['user_id']))  # noqa: E501

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
            '/ratings', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RatingsPagedResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_rating(self, rating_id, **kwargs):  # noqa: E501
        """Get rating.  # noqa: E501

        Returns the rating with the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rating(rating_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rating_id: The ID of the rating. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Rating
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_rating_with_http_info(rating_id, **kwargs)  # noqa: E501

    def get_rating_with_http_info(self, rating_id, **kwargs):  # noqa: E501
        """Get rating.  # noqa: E501

        Returns the rating with the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_rating_with_http_info(rating_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rating_id: The ID of the rating. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Rating, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'rating_id'
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
                    " to method get_rating" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rating_id' is set
        if self.api_client.client_side_validation and ('rating_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rating_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rating_id` when calling `get_rating`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rating_id' in local_var_params:
            path_params['ratingId'] = local_var_params['rating_id']  # noqa: E501

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
            '/ratings/{ratingId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Rating',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_rating(self, rating_id, **kwargs):  # noqa: E501
        """Remove rating.  # noqa: E501

        Removes the rating with the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_rating(rating_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rating_id: The ID of the rating to be removed. (required)
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
        return self.remove_rating_with_http_info(rating_id, **kwargs)  # noqa: E501

    def remove_rating_with_http_info(self, rating_id, **kwargs):  # noqa: E501
        """Remove rating.  # noqa: E501

        Removes the rating with the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_rating_with_http_info(rating_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str rating_id: The ID of the rating to be removed. (required)
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
            'rating_id'
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
                    " to method remove_rating" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'rating_id' is set
        if self.api_client.client_side_validation and ('rating_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['rating_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `rating_id` when calling `remove_rating`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'rating_id' in local_var_params:
            path_params['ratingId'] = local_var_params['rating_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['basicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/ratings/{ratingId}', 'DELETE',
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
