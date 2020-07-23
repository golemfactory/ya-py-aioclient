# coding: utf-8

"""
    Yagna Market API

     ## Yagna Market The Yagna Market is a core component of the Yagna Network, which enables computational Offers and Demands circulation. The Market is open for all entities willing to buy computations (Demands) or monetize computational resources (Offers). ## Yagna Market API The Yagna Market API is the entry to the Yagna Market through which Requestors and Providers can publish their Demands and Offers respectively, find matching counterparty, conduct negotiations and make an agreement.  This version of Market API conforms with capability level 1 of the <a href=\"https://docs.google.com/document/d/1Zny_vfgWV-hcsKS7P-Kdr3Fb0dwfl-6T_cYKVQ9mkNg\"> Market API specification</a>.  Market API contains two roles: Requestors and Providers which are symmetrical most of the time (excluding agreement phase).   # noqa: E501

    The version of the OpenAPI document: 1.6.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from ya_market.configuration import Configuration


class Event(object):
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
    openapi_types = {"event_type": "str", "event_date": "datetime"}

    attribute_map = {"event_type": "eventType", "event_date": "eventDate"}

    discriminator_value_class_map = {
        "AgreementEvent": "AgreementEvent",
        "PropertyQueryEvent": "PropertyQueryEvent",
        "ProposalEvent": "ProposalEvent",
    }

    def __init__(
        self, event_type=None, event_date=None, local_vars_configuration=None
    ):  # noqa: E501
        """Event - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._event_type = None
        self._event_date = None
        self.discriminator = "event_type"

        self.event_type = event_type
        self.event_date = event_date

    @property
    def event_type(self):
        """Gets the event_type of this Event.  # noqa: E501


        :return: The event_type of this Event.  # noqa: E501
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this Event.


        :param event_type: The event_type of this Event.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and event_type is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event_type`, must not be `None`"
            )  # noqa: E501

        self._event_type = event_type

    @property
    def event_date(self):
        """Gets the event_date of this Event.  # noqa: E501


        :return: The event_date of this Event.  # noqa: E501
        :rtype: datetime
        """
        return self._event_date

    @event_date.setter
    def event_date(self, event_date):
        """Sets the event_date of this Event.


        :param event_date: The event_date of this Event.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and event_date is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `event_date`, must not be `None`"
            )  # noqa: E501

        self._event_date = event_date

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, Event):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Event):
            return True

        return self.to_dict() != other.to_dict()
