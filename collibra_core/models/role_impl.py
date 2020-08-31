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


class RoleImpl(object):
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
        'name': 'str',
        'description': 'str',
        'permissions': 'list[str]',
        '_global': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'name': 'name',
        'description': 'description',
        'permissions': 'permissions',
        '_global': 'global'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, name=None, description=None, permissions=None, _global=None, local_vars_configuration=None):  # noqa: E501
        """RoleImpl - a model defined in OpenAPI"""  # noqa: E501
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
        self._name = None
        self._description = None
        self._permissions = None
        self.__global = None
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
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if permissions is not None:
            self.permissions = permissions
        if _global is not None:
            self._global = _global

    @property
    def id(self):
        """Gets the id of this RoleImpl.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this RoleImpl.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RoleImpl.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this RoleImpl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this RoleImpl.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this RoleImpl.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this RoleImpl.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this RoleImpl.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this RoleImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this RoleImpl.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this RoleImpl.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this RoleImpl.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this RoleImpl.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this RoleImpl.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this RoleImpl.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this RoleImpl.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this RoleImpl.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this RoleImpl.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this RoleImpl.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this RoleImpl.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this RoleImpl.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this RoleImpl.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this RoleImpl.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this RoleImpl.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this RoleImpl.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this RoleImpl.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this RoleImpl.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this RoleImpl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def name(self):
        """Gets the name of this RoleImpl.  # noqa: E501

        The name of the resource.  # noqa: E501

        :return: The name of this RoleImpl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RoleImpl.

        The name of the resource.  # noqa: E501

        :param name: The name of this RoleImpl.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this RoleImpl.  # noqa: E501

        The description of the resource.  # noqa: E501

        :return: The description of this RoleImpl.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleImpl.

        The description of the resource.  # noqa: E501

        :param description: The description of this RoleImpl.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def permissions(self):
        """Gets the permissions of this RoleImpl.  # noqa: E501

        The list of permissions this role will provide to the user.  # noqa: E501

        :return: The permissions of this RoleImpl.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this RoleImpl.

        The list of permissions this role will provide to the user.  # noqa: E501

        :param permissions: The permissions of this RoleImpl.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ATTACHMENT_ADD", "ATTACHMENT_CHANGE", "ATTACHMENT_REMOVE", "COMMENT_ADD", "COMMENT_CHANGE", "COMMENT_REMOVE", "RATING_ADD", "RATING_CHANGE", "RATING_REMOVE", "COMMUNITY_ADD", "COMMUNITY_CHANGE", "COMMUNITY_REMOVE", "COMMUNITY_CONFIGURE_EXTERNAL_SYSTEM", "COMMUNITY_RESPONSIBILITY_ADD", "COMMUNITY_RESPONSIBILITY_CHANGE", "COMMUNITY_RESPONSIBILITY_REMOVE", "DOMAIN_ADD", "DOMAIN_CHANGE", "DOMAIN_REMOVE", "DOMAIN_RESPONSIBILITY_ADD", "DOMAIN_RESPONSIBILITY_CHANGE", "DOMAIN_RESPONSIBILITY_REMOVE", "WORKFLOW_MANAGE", "ASSET_ADD", "ASSET_CHANGE", "ASSET_REMOVE", "ASSET_STATUS_CHANGE", "ASSET_TYPE_CHANGE", "ASSET_TAG_CHANGE", "ASSET_ATTRIBUTE_ADD", "ASSET_ATTRIBUTE_CHANGE", "ASSET_ATTRIBUTE_REMOVE", "ASSET_RESPONSIBILITY_ADD", "ASSET_RESPONSIBILITY_CHANGE", "ASSET_RESPONSIBILITY_REMOVE", "VIEW_PERMISSIONS_CHANGE", "BUSINESS_SEMANTICS_GLOSSARY", "REFERENCE_DATA_MANAGER", "DATA_STEWARDSHIP_MANAGER", "SYSTEM_ADMINISTRATION", "USER_ADMINISTRATION", "WORKFLOW_ADMINISTRATION", "DATA_HELPDESK", "POLICY_MANAGER", "DATA_DICTIONARY", "CATALOG", "WORKFLOW_MANAGE_ALL", "WORKFLOW_MESSAGE_EVENTS_USE", "VIEW_PERMISSIONS_VIEW_ALL", "VIEW_MANAGE", "VIEW_SHARE", "VIEW_MANAGE_ALL", "ADVANCED_DATA_TYPE_ADD", "ADVANCED_DATA_TYPE_EDIT", "ADVANCED_DATA_TYPE_REMOVE", "TAGS_VIEW", "TAGS_MANAGE", "VALIDATION_EXECUTION", "ACCESS_DATA", "VIEW_SAMPLES", "RELATION_TYPE_ADD", "RELATION_TYPE_REMOVE", "RELATION_TYPE_CHANGE", "REGISTER_PROFILING_INFORMATION", "REPORTING_DOWNLOAD_INSIGHTS_DATA", "REPORTING_VIEW_INSIGHTS_REPORTS", "TECHNICAL_LINEAGE"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(permissions).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `permissions` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(permissions) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._permissions = permissions

    @property
    def _global(self):
        """Gets the _global of this RoleImpl.  # noqa: E501

        Whether the role is global.  # noqa: E501

        :return: The _global of this RoleImpl.  # noqa: E501
        :rtype: bool
        """
        return self.__global

    @_global.setter
    def _global(self, _global):
        """Sets the _global of this RoleImpl.

        Whether the role is global.  # noqa: E501

        :param _global: The _global of this RoleImpl.  # noqa: E501
        :type: bool
        """

        self.__global = _global

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
        if not isinstance(other, RoleImpl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RoleImpl):
            return True

        return self.to_dict() != other.to_dict()