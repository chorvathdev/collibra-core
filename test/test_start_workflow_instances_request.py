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
from collibra_core.models.start_workflow_instances_request import StartWorkflowInstancesRequest  # noqa: E501
from collibra_core.rest import ApiException

class TestStartWorkflowInstancesRequest(unittest.TestCase):
    """StartWorkflowInstancesRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StartWorkflowInstancesRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.start_workflow_instances_request.StartWorkflowInstancesRequest()  # noqa: E501
        if include_optional :
            return StartWorkflowInstancesRequest(
                workflow_definition_id = '0', 
                business_item_ids = [
                    '0'
                    ], 
                business_item_type = 'ASSET', 
                form_properties = {
                    'key' : '0'
                    }, 
                guest_user_id = '0', 
                send_notification = True
            )
        else :
            return StartWorkflowInstancesRequest(
                workflow_definition_id = '0',
        )

    def testStartWorkflowInstancesRequest(self):
        """Test StartWorkflowInstancesRequest"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()