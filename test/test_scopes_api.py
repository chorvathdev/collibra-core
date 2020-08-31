# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import collibra_core
from collibra_core.api.scopes_api import ScopesApi  # noqa: E501
from collibra_core.rest import ApiException


class TestScopesApi(unittest.TestCase):
    """ScopesApi unit test stubs"""

    def setUp(self):
        self.api = collibra_core.api.scopes_api.ScopesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_scope(self):
        """Test case for add_scope

        Add scope  # noqa: E501
        """
        pass

    def test_change_scope(self):
        """Test case for change_scope

        Change scope  # noqa: E501
        """
        pass

    def test_get_all_scopes(self):
        """Test case for get_all_scopes

        Find scopes  # noqa: E501
        """
        pass

    def test_get_scope(self):
        """Test case for get_scope

        Get scope  # noqa: E501
        """
        pass

    def test_remove_scope(self):
        """Test case for remove_scope

        Remove scope  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
