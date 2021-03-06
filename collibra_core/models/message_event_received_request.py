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


class MessageEventReceivedRequest(object):
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
        'message_name': 'str',
        'process_instance_id': 'str',
        'variables': 'dict(str, object)'
    }

    attribute_map = {
        'message_name': 'messageName',
        'process_instance_id': 'processInstanceId',
        'variables': 'variables'
    }

    def __init__(self, message_name=None, process_instance_id=None, variables=None, local_vars_configuration=None):  # noqa: E501
        """MessageEventReceivedRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._message_name = None
        self._process_instance_id = None
        self._variables = None
        self.discriminator = None

        self.message_name = message_name
        self.process_instance_id = process_instance_id
        if variables is not None:
            self.variables = variables

    @property
    def message_name(self):
        """Gets the message_name of this MessageEventReceivedRequest.  # noqa: E501

        The name of the message event.  # noqa: E501

        :return: The message_name of this MessageEventReceivedRequest.  # noqa: E501
        :rtype: str
        """
        return self._message_name

    @message_name.setter
    def message_name(self, message_name):
        """Sets the message_name of this MessageEventReceivedRequest.

        The name of the message event.  # noqa: E501

        :param message_name: The message_name of this MessageEventReceivedRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and message_name is None:  # noqa: E501
            raise ValueError("Invalid value for `message_name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message_name is not None and len(message_name) > 2147483647):
            raise ValueError("Invalid value for `message_name`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                message_name is not None and len(message_name) < 1):
            raise ValueError("Invalid value for `message_name`, length must be greater than or equal to `1`")  # noqa: E501

        self._message_name = message_name

    @property
    def process_instance_id(self):
        """Gets the process_instance_id of this MessageEventReceivedRequest.  # noqa: E501

        The ID of the workflow execution.  # noqa: E501

        :return: The process_instance_id of this MessageEventReceivedRequest.  # noqa: E501
        :rtype: str
        """
        return self._process_instance_id

    @process_instance_id.setter
    def process_instance_id(self, process_instance_id):
        """Sets the process_instance_id of this MessageEventReceivedRequest.

        The ID of the workflow execution.  # noqa: E501

        :param process_instance_id: The process_instance_id of this MessageEventReceivedRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and process_instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `process_instance_id`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                process_instance_id is not None and len(process_instance_id) > 2147483647):
            raise ValueError("Invalid value for `process_instance_id`, length must be less than or equal to `2147483647`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                process_instance_id is not None and len(process_instance_id) < 1):
            raise ValueError("Invalid value for `process_instance_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._process_instance_id = process_instance_id

    @property
    def variables(self):
        """Gets the variables of this MessageEventReceivedRequest.  # noqa: E501

        The variables of the message event. They will be injected as variables in the running workflow.  # noqa: E501

        :return: The variables of this MessageEventReceivedRequest.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._variables

    @variables.setter
    def variables(self, variables):
        """Sets the variables of this MessageEventReceivedRequest.

        The variables of the message event. They will be injected as variables in the running workflow.  # noqa: E501

        :param variables: The variables of this MessageEventReceivedRequest.  # noqa: E501
        :type: dict(str, object)
        """

        self._variables = variables

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
        if not isinstance(other, MessageEventReceivedRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MessageEventReceivedRequest):
            return True

        return self.to_dict() != other.to_dict()
