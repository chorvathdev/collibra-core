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


class Comment(object):
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
        'created_by': 'str',
        'created_on': 'int',
        'last_modified_by': 'str',
        'last_modified_on': 'int',
        'system': 'bool',
        'resource_type': 'str',
        'content': 'str',
        'mentioned_users': 'User',
        'base_resource': 'ResourceReference',
        'parent': 'ResourceReference'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'content': 'content',
        'mentioned_users': 'mentionedUsers',
        'base_resource': 'baseResource',
        'parent': 'parent'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, content=None, mentioned_users=None, base_resource=None, parent=None, local_vars_configuration=None):  # noqa: E501
        """Comment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_by = None
        self._created_on = None
        self._last_modified_by = None
        self._last_modified_on = None
        self._system = None
        self._resource_type = None
        self._content = None
        self._mentioned_users = None
        self._base_resource = None
        self._parent = None
        self.discriminator = None

        self.id = id
        if created_by is not None:
            self.created_by = created_by
        if created_on is not None:
            self.created_on = created_on
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_on is not None:
            self.last_modified_on = last_modified_on
        if system is not None:
            self.system = system
        self.resource_type = resource_type
        if content is not None:
            self.content = content
        if mentioned_users is not None:
            self.mentioned_users = mentioned_users
        self.base_resource = base_resource
        if parent is not None:
            self.parent = parent

    @property
    def id(self):
        """Gets the id of this Comment.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Comment.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this Comment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this Comment.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Comment.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this Comment.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this Comment.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Comment.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this Comment.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this Comment.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this Comment.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this Comment.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this Comment.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this Comment.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this Comment.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this Comment.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this Comment.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this Comment.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Comment.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this Comment.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this Comment.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Comment.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this Comment.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def content(self):
        """Gets the content of this Comment.  # noqa: E501

        The content of the comment.  # noqa: E501

        :return: The content of this Comment.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Comment.

        The content of the comment.  # noqa: E501

        :param content: The content of this Comment.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def mentioned_users(self):
        """Gets the mentioned_users of this Comment.  # noqa: E501


        :return: The mentioned_users of this Comment.  # noqa: E501
        :rtype: User
        """
        return self._mentioned_users

    @mentioned_users.setter
    def mentioned_users(self, mentioned_users):
        """Sets the mentioned_users of this Comment.


        :param mentioned_users: The mentioned_users of this Comment.  # noqa: E501
        :type: User
        """

        self._mentioned_users = mentioned_users

    @property
    def base_resource(self):
        """Gets the base_resource of this Comment.  # noqa: E501


        :return: The base_resource of this Comment.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._base_resource

    @base_resource.setter
    def base_resource(self, base_resource):
        """Sets the base_resource of this Comment.


        :param base_resource: The base_resource of this Comment.  # noqa: E501
        :type: ResourceReference
        """
        if self.local_vars_configuration.client_side_validation and base_resource is None:  # noqa: E501
            raise ValueError("Invalid value for `base_resource`, must not be `None`")  # noqa: E501

        self._base_resource = base_resource

    @property
    def parent(self):
        """Gets the parent of this Comment.  # noqa: E501


        :return: The parent of this Comment.  # noqa: E501
        :rtype: ResourceReference
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this Comment.


        :param parent: The parent of this Comment.  # noqa: E501
        :type: ResourceReference
        """

        self._parent = parent

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
        if not isinstance(other, Comment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Comment):
            return True

        return self.to_dict() != other.to_dict()
