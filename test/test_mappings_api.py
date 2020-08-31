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
from collibra_core.api.mappings_api import MappingsApi  # noqa: E501
from collibra_core.rest import ApiException


class TestMappingsApi(unittest.TestCase):
    """MappingsApi unit test stubs"""

    def setUp(self):
        self.api = collibra_core.api.mappings_api.MappingsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_mapping(self):
        """Test case for add_mapping

        Adds a new mapping.  # noqa: E501
        """
        pass

    def test_add_mappings(self):
        """Test case for add_mappings

        Adds new mappings.  # noqa: E501
        """
        pass

    def test_change_mapping(self):
        """Test case for change_mapping

        Changes the mapping identified by its id.  # noqa: E501
        """
        pass

    def test_change_mapping_by_external_entity(self):
        """Test case for change_mapping_by_external_entity

        Changes the mapping identified by its external ids.  # noqa: E501
        """
        pass

    def test_change_mapping_by_mapped_resource(self):
        """Test case for change_mapping_by_mapped_resource

        Changes the mapping identified by its external system id and mapped resource id.  # noqa: E501
        """
        pass

    def test_change_mappings(self):
        """Test case for change_mappings

        Changes multiple mappings identified by their ids.  # noqa: E501
        """
        pass

    def test_change_mappings_by_external_entities(self):
        """Test case for change_mappings_by_external_entities

        Changes the mappings identified by their external ids.  # noqa: E501
        """
        pass

    def test_change_mappings_by_mapped_resources(self):
        """Test case for change_mappings_by_mapped_resources

        Changes the mapping identified by their external system ids and mapped resource ids.  # noqa: E501
        """
        pass

    def test_find_mappings(self):
        """Test case for find_mappings

        Returns mappings matching the given search criteria.  # noqa: E501
        """
        pass

    def test_get_mapping(self):
        """Test case for get_mapping

        Returns a mapping identified by given id.  # noqa: E501
        """
        pass

    def test_get_mapping_by_external_entity(self):
        """Test case for get_mapping_by_external_entity

        Returns a mapping identified by its external ids.  # noqa: E501
        """
        pass

    def test_get_mapping_by_mapped_resource(self):
        """Test case for get_mapping_by_mapped_resource

        Returns a mapping identified by its external system id and mapped resource id.  # noqa: E501
        """
        pass

    def test_remove_mapping(self):
        """Test case for remove_mapping

        Removes the mapping identified by its id.  # noqa: E501
        """
        pass

    def test_remove_mapping_by_external_entity(self):
        """Test case for remove_mapping_by_external_entity

        Removes the mapping identified by its external ids.  # noqa: E501
        """
        pass

    def test_remove_mapping_by_mapped_resource(self):
        """Test case for remove_mapping_by_mapped_resource

        Removes the mapping identified by its external system id and mapped resource id.  # noqa: E501
        """
        pass

    def test_remove_mappings_by_external_system_in_job(self):
        """Test case for remove_mappings_by_external_system_in_job

        Removes all the mappings identified by given external system id.  # noqa: E501
        """
        pass

    def test_remove_mappings_in_job(self):
        """Test case for remove_mappings_in_job

        Removes multiple mappings in job.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
