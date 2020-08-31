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


class User(object):
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
        'user_name': 'str',
        'first_name': 'str',
        'last_name': 'str',
        'email_address': 'str',
        'gender': 'str',
        'language': 'str',
        'additional_email_addresses': 'list[Email]',
        'phone_numbers': 'list[PhoneNumber]',
        'instant_messaging_accounts': 'list[InstantMessagingAccount]',
        'websites': 'list[Website]',
        'addresses': 'list[Address]',
        'activated': 'bool',
        'enabled': 'bool',
        'ldap_user': 'bool',
        'guest_user': 'bool',
        'api_user': 'bool',
        'license_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_by': 'createdBy',
        'created_on': 'createdOn',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_on': 'lastModifiedOn',
        'system': 'system',
        'resource_type': 'resourceType',
        'user_name': 'userName',
        'first_name': 'firstName',
        'last_name': 'lastName',
        'email_address': 'emailAddress',
        'gender': 'gender',
        'language': 'language',
        'additional_email_addresses': 'additionalEmailAddresses',
        'phone_numbers': 'phoneNumbers',
        'instant_messaging_accounts': 'instantMessagingAccounts',
        'websites': 'websites',
        'addresses': 'addresses',
        'activated': 'activated',
        'enabled': 'enabled',
        'ldap_user': 'ldapUser',
        'guest_user': 'guestUser',
        'api_user': 'apiUser',
        'license_type': 'licenseType'
    }

    def __init__(self, id=None, created_by=None, created_on=None, last_modified_by=None, last_modified_on=None, system=None, resource_type=None, user_name=None, first_name=None, last_name=None, email_address=None, gender=None, language=None, additional_email_addresses=None, phone_numbers=None, instant_messaging_accounts=None, websites=None, addresses=None, activated=None, enabled=None, ldap_user=None, guest_user=None, api_user=None, license_type=None, local_vars_configuration=None):  # noqa: E501
        """User - a model defined in OpenAPI"""  # noqa: E501
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
        self._user_name = None
        self._first_name = None
        self._last_name = None
        self._email_address = None
        self._gender = None
        self._language = None
        self._additional_email_addresses = None
        self._phone_numbers = None
        self._instant_messaging_accounts = None
        self._websites = None
        self._addresses = None
        self._activated = None
        self._enabled = None
        self._ldap_user = None
        self._guest_user = None
        self._api_user = None
        self._license_type = None
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
        if user_name is not None:
            self.user_name = user_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if email_address is not None:
            self.email_address = email_address
        if gender is not None:
            self.gender = gender
        if language is not None:
            self.language = language
        if additional_email_addresses is not None:
            self.additional_email_addresses = additional_email_addresses
        if phone_numbers is not None:
            self.phone_numbers = phone_numbers
        if instant_messaging_accounts is not None:
            self.instant_messaging_accounts = instant_messaging_accounts
        if websites is not None:
            self.websites = websites
        if addresses is not None:
            self.addresses = addresses
        if activated is not None:
            self.activated = activated
        if enabled is not None:
            self.enabled = enabled
        if ldap_user is not None:
            self.ldap_user = ldap_user
        if guest_user is not None:
            self.guest_user = guest_user
        if api_user is not None:
            self.api_user = api_user
        if license_type is not None:
            self.license_type = license_type

    @property
    def id(self):
        """Gets the id of this User.  # noqa: E501

        The id of the represented object (entity).  # noqa: E501

        :return: The id of this User.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

        The id of the represented object (entity).  # noqa: E501

        :param id: The id of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def created_by(self):
        """Gets the created_by of this User.  # noqa: E501

        The id of the user that created this resource.  # noqa: E501

        :return: The created_by of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this User.

        The id of the user that created this resource.  # noqa: E501

        :param created_by: The created_by of this User.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_on(self):
        """Gets the created_on of this User.  # noqa: E501

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :return: The created_on of this User.  # noqa: E501
        :rtype: int
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this User.

        The timestamp (in UTC time standard) of the creation of this resource.  # noqa: E501

        :param created_on: The created_on of this User.  # noqa: E501
        :type: int
        """

        self._created_on = created_on

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this User.  # noqa: E501

        The id of the user who modified this resource the last time.  # noqa: E501

        :return: The last_modified_by of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this User.

        The id of the user who modified this resource the last time.  # noqa: E501

        :param last_modified_by: The last_modified_by of this User.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_on(self):
        """Gets the last_modified_on of this User.  # noqa: E501

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :return: The last_modified_on of this User.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_on

    @last_modified_on.setter
    def last_modified_on(self, last_modified_on):
        """Sets the last_modified_on of this User.

        The timestamp (in UTC time standard) of the last modification of this resource.  # noqa: E501

        :param last_modified_on: The last_modified_on of this User.  # noqa: E501
        :type: int
        """

        self._last_modified_on = last_modified_on

    @property
    def system(self):
        """Gets the system of this User.  # noqa: E501

        Whether this is a system resource or not.  # noqa: E501

        :return: The system of this User.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this User.

        Whether this is a system resource or not.  # noqa: E501

        :param system: The system of this User.  # noqa: E501
        :type: bool
        """

        self._system = system

    @property
    def resource_type(self):
        """Gets the resource_type of this User.  # noqa: E501

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :return: The resource_type of this User.  # noqa: E501
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this User.

        The type of this resource, i.e. [Community, Asset, Domain, Attribute, Relation, WorkflowInstance].  # noqa: E501

        :param resource_type: The resource_type of this User.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and resource_type is None:  # noqa: E501
            raise ValueError("Invalid value for `resource_type`, must not be `None`")  # noqa: E501

        self._resource_type = resource_type

    @property
    def user_name(self):
        """Gets the user_name of this User.  # noqa: E501

        The user name.  # noqa: E501

        :return: The user_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this User.

        The user name.  # noqa: E501

        :param user_name: The user_name of this User.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def first_name(self):
        """Gets the first_name of this User.  # noqa: E501

        The first name of the user.  # noqa: E501

        :return: The first_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this User.

        The first name of the user.  # noqa: E501

        :param first_name: The first_name of this User.  # noqa: E501
        :type: str
        """

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this User.  # noqa: E501

        The last name of the user.  # noqa: E501

        :return: The last_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this User.

        The last name of the user.  # noqa: E501

        :param last_name: The last_name of this User.  # noqa: E501
        :type: str
        """

        self._last_name = last_name

    @property
    def email_address(self):
        """Gets the email_address of this User.  # noqa: E501

        The main email address.  # noqa: E501

        :return: The email_address of this User.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this User.

        The main email address.  # noqa: E501

        :param email_address: The email_address of this User.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def gender(self):
        """Gets the gender of this User.  # noqa: E501

        The gender of the user.  # noqa: E501

        :return: The gender of this User.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this User.

        The gender of the user.  # noqa: E501

        :param gender: The gender of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["MALE", "FEMALE", "UNKNOWN"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and gender not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `gender` ({0}), must be one of {1}"  # noqa: E501
                .format(gender, allowed_values)
            )

        self._gender = gender

    @property
    def language(self):
        """Gets the language of this User.  # noqa: E501

        The current language preference for this user.  # noqa: E501

        :return: The language of this User.  # noqa: E501
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this User.

        The current language preference for this user.  # noqa: E501

        :param language: The language of this User.  # noqa: E501
        :type: str
        """

        self._language = language

    @property
    def additional_email_addresses(self):
        """Gets the additional_email_addresses of this User.  # noqa: E501

        The list of additional email addresses.  # noqa: E501

        :return: The additional_email_addresses of this User.  # noqa: E501
        :rtype: list[Email]
        """
        return self._additional_email_addresses

    @additional_email_addresses.setter
    def additional_email_addresses(self, additional_email_addresses):
        """Sets the additional_email_addresses of this User.

        The list of additional email addresses.  # noqa: E501

        :param additional_email_addresses: The additional_email_addresses of this User.  # noqa: E501
        :type: list[Email]
        """

        self._additional_email_addresses = additional_email_addresses

    @property
    def phone_numbers(self):
        """Gets the phone_numbers of this User.  # noqa: E501

        The list of phone numbers.  # noqa: E501

        :return: The phone_numbers of this User.  # noqa: E501
        :rtype: list[PhoneNumber]
        """
        return self._phone_numbers

    @phone_numbers.setter
    def phone_numbers(self, phone_numbers):
        """Sets the phone_numbers of this User.

        The list of phone numbers.  # noqa: E501

        :param phone_numbers: The phone_numbers of this User.  # noqa: E501
        :type: list[PhoneNumber]
        """

        self._phone_numbers = phone_numbers

    @property
    def instant_messaging_accounts(self):
        """Gets the instant_messaging_accounts of this User.  # noqa: E501

        The list of instant messaging accounts.  # noqa: E501

        :return: The instant_messaging_accounts of this User.  # noqa: E501
        :rtype: list[InstantMessagingAccount]
        """
        return self._instant_messaging_accounts

    @instant_messaging_accounts.setter
    def instant_messaging_accounts(self, instant_messaging_accounts):
        """Sets the instant_messaging_accounts of this User.

        The list of instant messaging accounts.  # noqa: E501

        :param instant_messaging_accounts: The instant_messaging_accounts of this User.  # noqa: E501
        :type: list[InstantMessagingAccount]
        """

        self._instant_messaging_accounts = instant_messaging_accounts

    @property
    def websites(self):
        """Gets the websites of this User.  # noqa: E501

        The list of websites.  # noqa: E501

        :return: The websites of this User.  # noqa: E501
        :rtype: list[Website]
        """
        return self._websites

    @websites.setter
    def websites(self, websites):
        """Sets the websites of this User.

        The list of websites.  # noqa: E501

        :param websites: The websites of this User.  # noqa: E501
        :type: list[Website]
        """

        self._websites = websites

    @property
    def addresses(self):
        """Gets the addresses of this User.  # noqa: E501

        The list of addresses.  # noqa: E501

        :return: The addresses of this User.  # noqa: E501
        :rtype: list[Address]
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this User.

        The list of addresses.  # noqa: E501

        :param addresses: The addresses of this User.  # noqa: E501
        :type: list[Address]
        """

        self._addresses = addresses

    @property
    def activated(self):
        """Gets the activated of this User.  # noqa: E501

        Whether this user account is already activated or not.  # noqa: E501

        :return: The activated of this User.  # noqa: E501
        :rtype: bool
        """
        return self._activated

    @activated.setter
    def activated(self, activated):
        """Sets the activated of this User.

        Whether this user account is already activated or not.  # noqa: E501

        :param activated: The activated of this User.  # noqa: E501
        :type: bool
        """

        self._activated = activated

    @property
    def enabled(self):
        """Gets the enabled of this User.  # noqa: E501

        Whether this user account is already enabled or not.  # noqa: E501

        :return: The enabled of this User.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this User.

        Whether this user account is already enabled or not.  # noqa: E501

        :param enabled: The enabled of this User.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def ldap_user(self):
        """Gets the ldap_user of this User.  # noqa: E501

        Whether this is an LDAP user or not.  # noqa: E501

        :return: The ldap_user of this User.  # noqa: E501
        :rtype: bool
        """
        return self._ldap_user

    @ldap_user.setter
    def ldap_user(self, ldap_user):
        """Sets the ldap_user of this User.

        Whether this is an LDAP user or not.  # noqa: E501

        :param ldap_user: The ldap_user of this User.  # noqa: E501
        :type: bool
        """

        self._ldap_user = ldap_user

    @property
    def guest_user(self):
        """Gets the guest_user of this User.  # noqa: E501

        Whether this is a guest user or not.  # noqa: E501

        :return: The guest_user of this User.  # noqa: E501
        :rtype: bool
        """
        return self._guest_user

    @guest_user.setter
    def guest_user(self, guest_user):
        """Sets the guest_user of this User.

        Whether this is a guest user or not.  # noqa: E501

        :param guest_user: The guest_user of this User.  # noqa: E501
        :type: bool
        """

        self._guest_user = guest_user

    @property
    def api_user(self):
        """Gets the api_user of this User.  # noqa: E501

        Whether this is API user or not.  # noqa: E501

        :return: The api_user of this User.  # noqa: E501
        :rtype: bool
        """
        return self._api_user

    @api_user.setter
    def api_user(self, api_user):
        """Sets the api_user of this User.

        Whether this is API user or not.  # noqa: E501

        :param api_user: The api_user of this User.  # noqa: E501
        :type: bool
        """

        self._api_user = api_user

    @property
    def license_type(self):
        """Gets the license_type of this User.  # noqa: E501

        The licence type of the user.  # noqa: E501

        :return: The license_type of this User.  # noqa: E501
        :rtype: str
        """
        return self._license_type

    @license_type.setter
    def license_type(self, license_type):
        """Sets the license_type of this User.

        The licence type of the user.  # noqa: E501

        :param license_type: The license_type of this User.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSUMER", "AUTHOR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and license_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `license_type` ({0}), must be one of {1}"  # noqa: E501
                .format(license_type, allowed_values)
            )

        self._license_type = license_type

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
        if not isinstance(other, User):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, User):
            return True

        return self.to_dict() != other.to_dict()
