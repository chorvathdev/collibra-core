# coding: utf-8

"""
    Collibra Data Governance Center Core API

    <p>The Core REST API allows you to create your own integrations with Collibra Data Governance Center.</p><p><i>Create custom applications to help users get access to the right data.</i></p>  # noqa: E501

    The version of the OpenAPI document: 2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from collibra_core.configuration import Configuration


class ValidateInJobRequest(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'asset_ids': 'list[str]',
        'send_notification': 'bool'
    }

    attribute_map = {
        'asset_ids': 'assetIds',
        'send_notification': 'sendNotification'
    }

    def __init__(self, asset_ids=None, send_notification=None, local_vars_configuration=None):  # noqa: E501
        """ValidateInJobRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._asset_ids = None
        self._send_notification = None
        self.discriminator = None

        if asset_ids is not None:
            self.asset_ids = asset_ids
        if send_notification is not None:
            self.send_notification = send_notification

    @property
    def asset_ids(self):
        """Gets the asset_ids of this ValidateInJobRequest.  # noqa: E501


        :return: The asset_ids of this ValidateInJobRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this ValidateInJobRequest.


        :param asset_ids: The asset_ids of this ValidateInJobRequest.  # noqa: E501
        :type: list[str]
        """

        self._asset_ids = asset_ids

    @property
    def send_notification(self):
        """Gets the send_notification of this ValidateInJobRequest.  # noqa: E501


        :return: The send_notification of this ValidateInJobRequest.  # noqa: E501
        :rtype: bool
        """
        return self._send_notification

    @send_notification.setter
    def send_notification(self, send_notification):
        """Sets the send_notification of this ValidateInJobRequest.


        :param send_notification: The send_notification of this ValidateInJobRequest.  # noqa: E501
        :type: bool
        """

        self._send_notification = send_notification

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ValidateInJobRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ValidateInJobRequest):
            return True

        return self.to_dict() != other.to_dict()
