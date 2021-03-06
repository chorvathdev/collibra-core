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


class AddRelationTypeRequest(object):
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
        'id': 'str',
        'source_type_id': 'str',
        'role': 'str',
        'target_type_id': 'str',
        'co_role': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'source_type_id': 'sourceTypeId',
        'role': 'role',
        'target_type_id': 'targetTypeId',
        'co_role': 'coRole',
        'description': 'description'
    }

    def __init__(self, id=None, source_type_id=None, role=None, target_type_id=None, co_role=None, description=None, local_vars_configuration=None):  # noqa: E501
        """AddRelationTypeRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._source_type_id = None
        self._role = None
        self._target_type_id = None
        self._co_role = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.source_type_id = source_type_id
        self.role = role
        self.target_type_id = target_type_id
        self.co_role = co_role
        if description is not None:
            self.description = description

    @property
    def id(self):
        """Gets the id of this AddRelationTypeRequest.  # noqa: E501

        The ID of the new relation type. Should be unique within all relation types.<br/>It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :return: The id of this AddRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AddRelationTypeRequest.

        The ID of the new relation type. Should be unique within all relation types.<br/>It should have a format of universally unique identifier (UUID) and should not start with <code>00000000-0000-0000-</code> which is a reserved prefix.  # noqa: E501

        :param id: The id of this AddRelationTypeRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source_type_id(self):
        """Gets the source_type_id of this AddRelationTypeRequest.  # noqa: E501

        The ID of the source type for new relation type.  # noqa: E501

        :return: The source_type_id of this AddRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_type_id

    @source_type_id.setter
    def source_type_id(self, source_type_id):
        """Sets the source_type_id of this AddRelationTypeRequest.

        The ID of the source type for new relation type.  # noqa: E501

        :param source_type_id: The source_type_id of this AddRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and source_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `source_type_id`, must not be `None`")  # noqa: E501

        self._source_type_id = source_type_id

    @property
    def role(self):
        """Gets the role of this AddRelationTypeRequest.  # noqa: E501

        The name of the role that the source plays.  # noqa: E501

        :return: The role of this AddRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AddRelationTypeRequest.

        The name of the role that the source plays.  # noqa: E501

        :param role: The role of this AddRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and role is None:  # noqa: E501
            raise ValueError("Invalid value for `role`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                role is not None and len(role) > 255):
            raise ValueError("Invalid value for `role`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                role is not None and len(role) < 1):
            raise ValueError("Invalid value for `role`, length must be greater than or equal to `1`")  # noqa: E501

        self._role = role

    @property
    def target_type_id(self):
        """Gets the target_type_id of this AddRelationTypeRequest.  # noqa: E501

        The ID of the source type for new relation type.  # noqa: E501

        :return: The target_type_id of this AddRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._target_type_id

    @target_type_id.setter
    def target_type_id(self, target_type_id):
        """Sets the target_type_id of this AddRelationTypeRequest.

        The ID of the source type for new relation type.  # noqa: E501

        :param target_type_id: The target_type_id of this AddRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and target_type_id is None:  # noqa: E501
            raise ValueError("Invalid value for `target_type_id`, must not be `None`")  # noqa: E501

        self._target_type_id = target_type_id

    @property
    def co_role(self):
        """Gets the co_role of this AddRelationTypeRequest.  # noqa: E501

        The name of the role that the target plays.  # noqa: E501

        :return: The co_role of this AddRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._co_role

    @co_role.setter
    def co_role(self, co_role):
        """Sets the co_role of this AddRelationTypeRequest.

        The name of the role that the target plays.  # noqa: E501

        :param co_role: The co_role of this AddRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and co_role is None:  # noqa: E501
            raise ValueError("Invalid value for `co_role`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                co_role is not None and len(co_role) > 255):
            raise ValueError("Invalid value for `co_role`, length must be less than or equal to `255`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                co_role is not None and len(co_role) < 1):
            raise ValueError("Invalid value for `co_role`, length must be greater than or equal to `1`")  # noqa: E501

        self._co_role = co_role

    @property
    def description(self):
        """Gets the description of this AddRelationTypeRequest.  # noqa: E501

        The description of the relation type.  # noqa: E501

        :return: The description of this AddRelationTypeRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AddRelationTypeRequest.

        The description of the relation type.  # noqa: E501

        :param description: The description of this AddRelationTypeRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 4000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `4000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

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
        if not isinstance(other, AddRelationTypeRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AddRelationTypeRequest):
            return True

        return self.to_dict() != other.to_dict()
