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
from collibra_core.models.paged_response_rating import PagedResponseRating  # noqa: E501
from collibra_core.rest import ApiException

class TestPagedResponseRating(unittest.TestCase):
    """PagedResponseRating unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PagedResponseRating
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.paged_response_rating.PagedResponseRating()  # noqa: E501
        if include_optional :
            return PagedResponseRating(
                total = 1000, 
                offset = 10, 
                limit = 100, 
                results = [
                    collibra_core.models.rating.Rating(
                        id = '0', 
                        created_by = '4d250cc5-e583-4640-9874-b93d82c7a6cb', 
                        created_on = 1475503010320, 
                        last_modified_by = 'a073ff90-e7bc-4b35-ba90-c4d475f642fe', 
                        last_modified_on = 1476703764163, 
                        system = True, 
                        resource_type = 'Job', 
                        rating = 0.2, 
                        review = '0', 
                        asset = collibra_core.models.named_resource_reference_impl.NamedResourceReferenceImpl(
                            id = '2b7f3a1a-4e50-4077-96f0-a58a395c860d', 
                            resource_type = 'Asset', 
                            name = '0', ), )
                    ]
            )
        else :
            return PagedResponseRating(
        )

    def testPagedResponseRating(self):
        """Test PagedResponseRating"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()