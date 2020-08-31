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
from collibra_core.models.body_part import BodyPart  # noqa: E501
from collibra_core.rest import ApiException

class TestBodyPart(unittest.TestCase):
    """BodyPart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BodyPart
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = collibra_core.models.body_part.BodyPart()  # noqa: E501
        if include_optional :
            return BodyPart(
                content_disposition = collibra_core.models.content_disposition.ContentDisposition(
                    type = '0', 
                    parameters = {
                        'key' : '0'
                        }, 
                    file_name = '0', 
                    creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    read_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    size = 56, ), 
                entity = None, 
                headers = {
                    'key' : [
                        '0'
                        ]
                    }, 
                media_type = collibra_core.models.body_part_media_type.BodyPart_mediaType(
                    type = '0', 
                    subtype = '0', 
                    parameters = {
                        'key' : '0'
                        }, 
                    wildcard_type = True, 
                    wildcard_subtype = True, ), 
                message_body_workers = None, 
                parent = collibra_core.models.multi_part.MultiPart(
                    content_disposition = collibra_core.models.content_disposition.ContentDisposition(
                        type = '0', 
                        parameters = {
                            'key' : '0'
                            }, 
                        file_name = '0', 
                        creation_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        modification_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        read_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        size = 56, ), 
                    entity = collibra_core.models.entity.entity(), 
                    headers = {
                        'key' : [
                            '0'
                            ]
                        }, 
                    media_type = collibra_core.models.body_part_media_type.BodyPart_mediaType(
                        type = '0', 
                        subtype = '0', 
                        wildcard_type = True, 
                        wildcard_subtype = True, ), 
                    message_body_workers = collibra_core.models.message_body_workers.MessageBodyWorkers(), 
                    parent = collibra_core.models.multi_part.MultiPart(
                        entity = collibra_core.models.entity.entity(), 
                        providers = collibra_core.models.providers.providers(), 
                        body_parts = [
                            collibra_core.models.body_part.BodyPart(
                                entity = collibra_core.models.entity.entity(), 
                                providers = collibra_core.models.providers.providers(), 
                                parameterized_headers = {
                                    'key' : [
                                        collibra_core.models.parameterized_header.ParameterizedHeader(
                                            value = '0', )
                                        ]
                                    }, )
                            ], 
                        parameterized_headers = {
                            'key' : [
                                collibra_core.models.parameterized_header.ParameterizedHeader(
                                    value = '0', )
                                ]
                            }, ), 
                    providers = collibra_core.models.providers.providers(), 
                    body_parts = [
                        collibra_core.models.body_part.BodyPart(
                            entity = collibra_core.models.entity.entity(), 
                            providers = collibra_core.models.providers.providers(), )
                        ], 
                    parameterized_headers = {
                        'key' : [
                            collibra_core.models.parameterized_header.ParameterizedHeader(
                                value = '0', )
                            ]
                        }, ), 
                providers = collibra_core.models.providers.providers(), 
                parameterized_headers = {
                    'key' : [
                        collibra_core.models.parameterized_header.ParameterizedHeader(
                            value = '0', 
                            parameters = {
                                'key' : '0'
                                }, )
                        ]
                    }
            )
        else :
            return BodyPart(
        )

    def testBodyPart(self):
        """Test BodyPart"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
