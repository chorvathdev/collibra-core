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


class Mapping(object):
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
        'external_system_id': 'str',
        'external_entity_id': 'str',
        'external_entity_url': 'str',
        'description': 'str',
        'mapped_resource': 'NamedResourceReferenceImpl',
        'last_sync_date': 'int',
        'sync_action': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'external_system_id': 'externalSystemId',
        'external_entity_id': 'externalEntityId',
        'external_entity_url': 'externalEntityUrl',
        'description': 'description',
        'mapped_resource': 'mappedResource',
        'last_sync_date': 'lastSyncDate',
        'sync_action': 'syncAction'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, external_system_id=None, external_entity_id=None, external_entity_url=None, description=None, mapped_resource=None, last_sync_date=None, sync_action=None, local_vars_configuration=None):  # noqa: E501
        """Mapping - a model defined in OpenAPI"""  # noqa: E501
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
        self._external_system_id = None
        self._external_entity_id = None
        self._external_entity_url = None
        self._description = None
        self._mapped_resource = None
        self._last_sync_date = None
        self._sync_action = None
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
        if external_system_id is not None:
            self.external_system_id = external_system_id
        if external_entity_id is not None:
            self.external_entity_id = external_entity_id
        if external_entity_url is not None:
            self.external_entity_url = external_entity_url
        if description is not None:
            self.description = description
        if mapped_resource is not None:
            self.mapped_resource = mapped_resource
        if last_sync_date is not None:
            self.last_sync_date = last_sync_date
        if sync_action is not None:
            self.sync_action = sync_action

    @property
    def id(self):
        """Gets the id of this Mapping.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Mapping.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this Mapping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this Mapping.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Mapping.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this Mapping.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this Mapping.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this Mapping.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Mapping.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this Mapping.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this Mapping.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this Mapping.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this Mapping.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this Mapping.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this Mapping.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this Mapping.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this Mapping.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this Mapping.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this Mapping.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Mapping.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this Mapping.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this Mapping.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this Mapping.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this Mapping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def external_system_id(self):
        """Gets the external_system_id of this Mapping.  # noqa: E501

        The id of the external system that the mapped resource belongs to.  # noqa: E501

        :return: The external_system_id of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._external_system_id

    @external_system_id.setter
    def external_system_id(self, external_system_id):
        """Sets the external_system_id of this Mapping.

        The id of the external system that the mapped resource belongs to.  # noqa: E501

        :param external_system_id: The external_system_id of this Mapping.  # noqa: E501
        :type: str
        """

        self._external_system_id = external_system_id

    @property
    def external_entity_id(self):
        """Gets the external_entity_id of this Mapping.  # noqa: E501

        The external id of the mapped resource.  # noqa: E501

        :return: The external_entity_id of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._external_entity_id

    @external_entity_id.setter
    def external_entity_id(self, external_entity_id):
        """Sets the external_entity_id of this Mapping.

        The external id of the mapped resource.  # noqa: E501

        :param external_entity_id: The external_entity_id of this Mapping.  # noqa: E501
        :type: str
        """

        self._external_entity_id = external_entity_id

    @property
    def external_entity_url(self):
        """Gets the external_entity_url of this Mapping.  # noqa: E501

        The external URL of the mapped resource.  # noqa: E501

        :return: The external_entity_url of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._external_entity_url

    @external_entity_url.setter
    def external_entity_url(self, external_entity_url):
        """Sets the external_entity_url of this Mapping.

        The external URL of the mapped resource.  # noqa: E501

        :param external_entity_url: The external_entity_url of this Mapping.  # noqa: E501
        :type: str
        """

        self._external_entity_url = external_entity_url

    @property
    def description(self):
        """Gets the description of this Mapping.  # noqa: E501

        The description of the mapped resource.  # noqa: E501

        :return: The description of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Mapping.

        The description of the mapped resource.  # noqa: E501

        :param description: The description of this Mapping.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mapped_resource(self):
        """Gets the mapped_resource of this Mapping.  # noqa: E501


        :return: The mapped_resource of this Mapping.  # noqa: E501
        :rtype: NamedResourceReferenceImpl
        """
        return self._mapped_resource

    @mapped_resource.setter
    def mapped_resource(self, mapped_resource):
        """Sets the mapped_resource of this Mapping.


        :param mapped_resource: The mapped_resource of this Mapping.  # noqa: E501
        :type: NamedResourceReferenceImpl
        """

        self._mapped_resource = mapped_resource

    @property
    def last_sync_date(self):
        """Gets the last_sync_date of this Mapping.  # noqa: E501

        The timestamp (in UTC time standard) of the last synchronization of mapped resource.  # noqa: E501

        :return: The last_sync_date of this Mapping.  # noqa: E501
        :rtype: int
        """
        return self._last_sync_date

    @last_sync_date.setter
    def last_sync_date(self, last_sync_date):
        """Sets the last_sync_date of this Mapping.

        The timestamp (in UTC time standard) of the last synchronization of mapped resource.  # noqa: E501

        :param last_sync_date: The last_sync_date of this Mapping.  # noqa: E501
        :type: int
        """

        self._last_sync_date = last_sync_date

    @property
    def sync_action(self):
        """Gets the sync_action of this Mapping.  # noqa: E501

        Represents the type of the action performed during last successful synchronization  # noqa: E501

        :return: The sync_action of this Mapping.  # noqa: E501
        :rtype: str
        """
        return self._sync_action

    @sync_action.setter
    def sync_action(self, sync_action):
        """Sets the sync_action of this Mapping.

        Represents the type of the action performed during last successful synchronization  # noqa: E501

        :param sync_action: The sync_action of this Mapping.  # noqa: E501
        :type: str
        """
        allowed_values = ["ADD", "UPDATE", "REMOVE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and sync_action not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `sync_action` ({0}), must be one of {1}"  # noqa: E501
                .format(sync_action, allowed_values)
            )

        self._sync_action = sync_action

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
        if not isinstance(other, Mapping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Mapping):
            return True

        return self.to_dict() != other.to_dict()
