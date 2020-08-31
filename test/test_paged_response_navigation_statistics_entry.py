# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import collibra_core
from collibra_core.models.paged_response_navigation_statistics_entry import PagedResponseNavigationStatisticsEntry  # noqa: E501
from collibra_core.rest import ApiException

class TestPagedResponseNavigationStatisticsEntry(unittest.TestCase):
    """PagedResponseNavigationStatisticsEntry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResponseNavigationStatisticsEntry
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.paged_response_navigation_statistics_entry.PagedResponseNavigationStatisticsEntry()  # noqa: E501
        if include_optional :
            return PagedResponseNavigationStatisticsEntry(
                total = 1000, 
                offset = 10, 
                limit = 100, 
                results = [
                    collibra_core.models.navigation_statistics_entry.NavigationStatisticsEntry(
                        asset_id = '6b1e48c3-0d90-42ad-a0e3-bfb6644c8cf9', 
                        name = '0', 
                        number_of_views = 56, 
                        last_viewed_date = 1475904011120, )
                    ]
            )
        else :
            return PagedResponseNavigationStatisticsEntry(
        )

    def testPagedResponseNavigationStatisticsEntry(self):
        """Test PagedResponseNavigationStatisticsEntry"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
