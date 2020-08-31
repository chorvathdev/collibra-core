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
from collibra_core.models.role_impl import RoleImpl  # noqa: E501
from collibra_core.rest import ApiException

class TestRoleImpl(unittest.TestCase):
    """RoleImpl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RoleImpl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.role_impl.RoleImpl()  # noqa: E501
        if include_optional :
            return RoleImpl(
                id = '0', 
                created_by = '4d250cc5-e583-4640-9874-b93d82c7a6cb', 
                created_on = 1475503010320, 
                last_modified_by = 'a073ff90-e7bc-4b35-ba90-c4d475f642fe', 
                last_modified_on = 1476703764163, 
                system = True, 
                resource_type = 'Job', 
                name = 'Test name', 
                description = 'Sample descripion of the resource.', 
                permissions = [
                    'ATTACHMENT_ADD'
                    ], 
                _global = True
            )
        else :
            return RoleImpl(
                id = '0',
                resource_type = 'Job',
        )

    def testRoleImpl(self):
        """Test RoleImpl"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
