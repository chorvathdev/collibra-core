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


class ChangeWorkflowDefinitionRequest(object):
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
        'name': 'str',
        'description': 'str',
        'configuration_variables': 'dict(str, str)',
        'start_events': 'list[str]',
        'business_item_resource_type': 'str',
        'exclusivity': 'str',
        'guest_user_accessible': 'bool',
        'registered_user_accessible': 'bool',
        'candidate_user_check_disabled': 'bool',
        'global_create': 'bool',
        'enable': 'bool',
        'start_label': 'str',
        'start_role_ids': 'list[str]',
        'stop_role_ids': 'list[str]',
        'reassign_role_ids': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'configuration_variables': 'configurationVariables',
        'start_events': 'startEvents',
        'business_item_resource_type': 'businessItemResourceType',
        'exclusivity': 'exclusivity',
        'guest_user_accessible': 'guestUserAccessible',
        'registered_user_accessible': 'registeredUserAccessible',
        'candidate_user_check_disabled': 'candidateUserCheckDisabled',
        'global_create': 'globalCreate',
        'enable': 'enable',
        'start_label': 'startLabel',
        'start_role_ids': 'startRoleIds',
        'stop_role_ids': 'stopRoleIds',
        'reassign_role_ids': 'reassignRoleIds'
    }

    def __init__(self, name=None, description=None, configuration_variables=None, start_events=None, business_item_resource_type=None, exclusivity=None, guest_user_accessible=None, registered_user_accessible=None, candidate_user_check_disabled=None, global_create=None, enable=None, start_label=None, start_role_ids=None, stop_role_ids=None, reassign_role_ids=None, local_vars_configuration=None):  # noqa: E501
        """ChangeWorkflowDefinitionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._configuration_variables = None
        self._start_events = None
        self._business_item_resource_type = None
        self._exclusivity = None
        self._guest_user_accessible = None
        self._registered_user_accessible = None
        self._candidate_user_check_disabled = None
        self._global_create = None
        self._enable = None
        self._start_label = None
        self._start_role_ids = None
        self._stop_role_ids = None
        self._reassign_role_ids = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if configuration_variables is not None:
            self.configuration_variables = configuration_variables
        if start_events is not None:
            self.start_events = start_events
        if business_item_resource_type is not None:
            self.business_item_resource_type = business_item_resource_type
        if exclusivity is not None:
            self.exclusivity = exclusivity
        if guest_user_accessible is not None:
            self.guest_user_accessible = guest_user_accessible
        if registered_user_accessible is not None:
            self.registered_user_accessible = registered_user_accessible
        if candidate_user_check_disabled is not None:
            self.candidate_user_check_disabled = candidate_user_check_disabled
        if global_create is not None:
            self.global_create = global_create
        if enable is not None:
            self.enable = enable
        if start_label is not None:
            self.start_label = start_label
        if start_role_ids is not None:
            self.start_role_ids = start_role_ids
        if stop_role_ids is not None:
            self.stop_role_ids = stop_role_ids
        if reassign_role_ids is not None:
            self.reassign_role_ids = reassign_role_ids

    @property
    def name(self):
        """Gets the name of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The name of the workflow definition.  # noqa: E501

        :return: The name of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChangeWorkflowDefinitionRequest.

        The name of the workflow definition.  # noqa: E501

        :param name: The name of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 2000):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `2000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The new description for the workflow definition.  # noqa: E501

        :return: The description of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ChangeWorkflowDefinitionRequest.

        The new description for the workflow definition.  # noqa: E501

        :param description: The description of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def configuration_variables(self):
        """Gets the configuration_variables of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The configuration variables.  # noqa: E501

        :return: The configuration_variables of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._configuration_variables

    @configuration_variables.setter
    def configuration_variables(self, configuration_variables):
        """Sets the configuration_variables of this ChangeWorkflowDefinitionRequest.

        The configuration variables.  # noqa: E501

        :param configuration_variables: The configuration_variables of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._configuration_variables = configuration_variables

    @property
    def start_events(self):
        """Gets the start_events of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The list of workflow start event types.  # noqa: E501

        :return: The start_events of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_events

    @start_events.setter
    def start_events(self, start_events):
        """Sets the start_events of this ChangeWorkflowDefinitionRequest.

        The list of workflow start event types.  # noqa: E501

        :param start_events: The start_events of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["ASSET_ADDED", "ASSET_REMOVED", "ASSET_STATUS_CHANGED", "ASSET_DOMAIN_CHANGED", "ASSET_TYPE_CHANGED", "ASSET_ATTRIBUTE_CHANGED", "ASSET_NAME_CHANGED", "ASSET_DISPLAY_NAME_CHANGED", "ASSET_ATTRIBUTE_ADDED", "ASSET_ATTRIBUTE_REMOVED", "DOMAIN_ADDED", "DOMAIN_REMOVED", "ROLE_GRANTED", "ROLE_REVOKED", "WORKFLOW_STARTED", "WORKFLOW_CANCELED", "WORKLFLOW_ESCALATION", "WORKFLOW_TASK_COMPLETED", "USER_ADDED", "USER_REMOVED", "USER_DISABLED", "COMMENT_ADDED", "COMMENT_REMOVED", "COMMENT_CHANGED", "RELATION_ADDED_AND_ASSET_IS_SOURCE", "RELATION_REMOVED_AND_ASSET_WAS_SOURCE", "RELATION_ADDED_AND_ASSET_IS_TARGET", "RELATION_REMOVED_AND_ASSET_WAS_TARGET", "TAG_ASSIGN_CHANGED", "CLASSIFICATION_MATCH_ACCEPTED", "CLASSIFICATION_MATCH_REJECTED", "CLASSIFICATION_MATCH_ADDED", "CLASSIFICATION_MATCH_REMOVED", "CLASSIFICATION_MATCH_UPDATED"]  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                not set(start_events).issubset(set(allowed_values))):  # noqa: E501
            raise ValueError(
                "Invalid values for `start_events` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(start_events) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._start_events = start_events

    @property
    def business_item_resource_type(self):
        """Gets the business_item_resource_type of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The type of the business item corresponding to the workflow.  # noqa: E501

        :return: The business_item_resource_type of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._business_item_resource_type

    @business_item_resource_type.setter
    def business_item_resource_type(self, business_item_resource_type):
        """Sets the business_item_resource_type of this ChangeWorkflowDefinitionRequest.

        The type of the business item corresponding to the workflow.  # noqa: E501

        :param business_item_resource_type: The business_item_resource_type of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["ASSET", "DOMAIN", "COMMUNITY", "GLOBAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and business_item_resource_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `business_item_resource_type` ({0}), must be one of {1}"  # noqa: E501
                .format(business_item_resource_type, allowed_values)
            )

        self._business_item_resource_type = business_item_resource_type

    @property
    def exclusivity(self):
        """Gets the exclusivity of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        Defines the number of times a resource workflow is able to be start.  # noqa: E501

        :return: The exclusivity of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._exclusivity

    @exclusivity.setter
    def exclusivity(self, exclusivity):
        """Sets the exclusivity of this ChangeWorkflowDefinitionRequest.

        Defines the number of times a resource workflow is able to be start.  # noqa: E501

        :param exclusivity: The exclusivity of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["RESOURCE_EXCLUSIVITY", "DEFINITION_EXCLUSIVITY", "UNCONSTRAINED"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and exclusivity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `exclusivity` ({0}), must be one of {1}"  # noqa: E501
                .format(exclusivity, allowed_values)
            )

        self._exclusivity = exclusivity

    @property
    def guest_user_accessible(self):
        """Gets the guest_user_accessible of this ChangeWorkflowDefinitionRequest.  # noqa: E501


        :return: The guest_user_accessible of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._guest_user_accessible

    @guest_user_accessible.setter
    def guest_user_accessible(self, guest_user_accessible):
        """Sets the guest_user_accessible of this ChangeWorkflowDefinitionRequest.


        :param guest_user_accessible: The guest_user_accessible of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._guest_user_accessible = guest_user_accessible

    @property
    def registered_user_accessible(self):
        """Gets the registered_user_accessible of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        Whether the workflow should be accessible by the registered user.  # noqa: E501

        :return: The registered_user_accessible of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._registered_user_accessible

    @registered_user_accessible.setter
    def registered_user_accessible(self, registered_user_accessible):
        """Sets the registered_user_accessible of this ChangeWorkflowDefinitionRequest.

        Whether the workflow should be accessible by the registered user.  # noqa: E501

        :param registered_user_accessible: The registered_user_accessible of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._registered_user_accessible = registered_user_accessible

    @property
    def candidate_user_check_disabled(self):
        """Gets the candidate_user_check_disabled of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        Whether the candidate user check for the workflow should be disabled.  # noqa: E501

        :return: The candidate_user_check_disabled of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._candidate_user_check_disabled

    @candidate_user_check_disabled.setter
    def candidate_user_check_disabled(self, candidate_user_check_disabled):
        """Sets the candidate_user_check_disabled of this ChangeWorkflowDefinitionRequest.

        Whether the candidate user check for the workflow should be disabled.  # noqa: E501

        :param candidate_user_check_disabled: The candidate_user_check_disabled of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._candidate_user_check_disabled = candidate_user_check_disabled

    @property
    def global_create(self):
        """Gets the global_create of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        Whether the workflow is accessible from the global create menu.  # noqa: E501

        :return: The global_create of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._global_create

    @global_create.setter
    def global_create(self, global_create):
        """Sets the global_create of this ChangeWorkflowDefinitionRequest.

        Whether the workflow is accessible from the global create menu.  # noqa: E501

        :param global_create: The global_create of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._global_create = global_create

    @property
    def enable(self):
        """Gets the enable of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        Whether the workflow definition should be enabled.  # noqa: E501

        :return: The enable of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this ChangeWorkflowDefinitionRequest.

        Whether the workflow definition should be enabled.  # noqa: E501

        :param enable: The enable of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def start_label(self):
        """Gets the start_label of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The start label of the workflow.  # noqa: E501

        :return: The start_label of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: str
        """
        return self._start_label

    @start_label.setter
    def start_label(self, start_label):
        """Sets the start_label of this ChangeWorkflowDefinitionRequest.

        The start label of the workflow.  # noqa: E501

        :param start_label: The start_label of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: str
        """

        self._start_label = start_label

    @property
    def start_role_ids(self):
        """Gets the start_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The list of IDs identifying the roles allowing to start the workflow.  # noqa: E501

        :return: The start_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._start_role_ids

    @start_role_ids.setter
    def start_role_ids(self, start_role_ids):
        """Sets the start_role_ids of this ChangeWorkflowDefinitionRequest.

        The list of IDs identifying the roles allowing to start the workflow.  # noqa: E501

        :param start_role_ids: The start_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: list[str]
        """

        self._start_role_ids = start_role_ids

    @property
    def stop_role_ids(self):
        """Gets the stop_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The list of IDs identifying the roles allowing to stop the workflow.  # noqa: E501

        :return: The stop_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._stop_role_ids

    @stop_role_ids.setter
    def stop_role_ids(self, stop_role_ids):
        """Sets the stop_role_ids of this ChangeWorkflowDefinitionRequest.

        The list of IDs identifying the roles allowing to stop the workflow.  # noqa: E501

        :param stop_role_ids: The stop_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: list[str]
        """

        self._stop_role_ids = stop_role_ids

    @property
    def reassign_role_ids(self):
        """Gets the reassign_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501

        The list of IDs identifying the roles allowing to reassign the workflow.  # noqa: E501

        :return: The reassign_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._reassign_role_ids

    @reassign_role_ids.setter
    def reassign_role_ids(self, reassign_role_ids):
        """Sets the reassign_role_ids of this ChangeWorkflowDefinitionRequest.

        The list of IDs identifying the roles allowing to reassign the workflow.  # noqa: E501

        :param reassign_role_ids: The reassign_role_ids of this ChangeWorkflowDefinitionRequest.  # noqa: E501
        :type: list[str]
        """

        self._reassign_role_ids = reassign_role_ids

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
        if not isinstance(other, ChangeWorkflowDefinitionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ChangeWorkflowDefinitionRequest):
            return True

        return self.to_dict() != other.to_dict()