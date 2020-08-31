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
from collibra_core.models.related_asset_id import RelatedAssetId  # noqa: E501
from collibra_core.rest import ApiException

class TestRelatedAssetId(unittest.TestCase):
    """RelatedAssetId unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RelatedAssetId
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.related_asset_id.RelatedAssetId()  # noqa: E501
        if include_optional :
            return RelatedAssetId(
                id = '0'
            )
        else :
            return RelatedAssetId(
                id = '0',
        )

    def testRelatedAssetId(self):
        """Test RelatedAssetId"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
