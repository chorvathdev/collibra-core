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
from collibra_core.api.activities_api import ActivitiesApi  # noqa: E501
from collibra_core.rest import ApiException


class TestActivitiesApi(unittest.TestCase):
    """ActivitiesApi unit test stubs"""

    def setUp(self):
        self.api = collibra_core.api.activities_api.ActivitiesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_activities(self):
        """Test case for get_activities

        Returns activities matching the given search criteria.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
