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
from collibra_core.models.start_form_data_impl import StartFormDataImpl  # noqa: E501
from collibra_core.rest import ApiException

class TestStartFormDataImpl(unittest.TestCase):
    """StartFormDataImpl unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StartFormDataImpl
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.start_form_data_impl.StartFormDataImpl()  # noqa: E501
        if include_optional :
            return StartFormDataImpl(
                form_key = '0', 
                form_properties = [
                    collibra_core.models.form_property.FormProperty(
                        id = '0', 
                        name = '0', 
                        type = '0', 
                        value = '0', 
                        writable = True, 
                        required = True, 
                        enum_values = [
                            collibra_core.models.dropdown_value.DropdownValue(
                                parents = [
                                    '0'
                                    ], 
                                id_as_string = '0', 
                                text = '0', 
                                id = '0', )
                            ], 
                        check_buttons = [
                            collibra_core.models.option_value.OptionValue(
                                label = '0', 
                                value = '0', )
                            ], 
                        radio_buttons = [
                            collibra_core.models.option_value.OptionValue(
                                label = '0', 
                                value = '0', )
                            ], 
                        default_dropdown_values = [
                            collibra_core.models.dropdown_value.DropdownValue(
                                id_as_string = '0', 
                                text = '0', 
                                id = '0', )
                            ], 
                        proposed_dropdown_values = [
                            collibra_core.models.dropdown_value.DropdownValue(
                                id_as_string = '0', 
                                text = '0', 
                                id = '0', )
                            ], 
                        date_time_type = '0', 
                        multi_value = True, 
                        proposed_fixed = True, 
                        default_from_resource = True, 
                        multi_default_dropdown_values = {
                            'key' : [
                                collibra_core.models.dropdown_value.DropdownValue(
                                    id_as_string = '0', 
                                    text = '0', 
                                    id = '0', )
                                ]
                            }, 
                        multi_proposed_dropdown_values = {
                            'key' : [
                                collibra_core.models.dropdown_value.DropdownValue(
                                    id_as_string = '0', 
                                    text = '0', 
                                    id = '0', )
                                ]
                            }, 
                        asset_type = collibra_core.models.resource_reference.ResourceReference(
                            id = '2b7f3a1a-4e50-4077-96f0-a58a395c860d', 
                            resource_type = 'Asset', ), )
                    ], 
                process_id = '0'
            )
        else :
            return StartFormDataImpl(
        )

    def testStartFormDataImpl(self):
        """Test StartFormDataImpl"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
