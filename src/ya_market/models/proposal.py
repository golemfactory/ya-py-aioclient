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


class Proposal(object):
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
        "properties": "object",
        "constraints": "str",
        "proposal_id": "str",
        "issuer_id": "str",
        "state": "str",
        "prev_proposal_id": "str",
    }

    attribute_map = {
        "properties": "properties",
        "constraints": "constraints",
        "proposal_id": "proposalId",
        "issuer_id": "issuerId",
        "state": "state",
        "prev_proposal_id": "prevProposalId",
    }

    def __init__(
        self,
        properties=None,
        constraints=None,
        proposal_id=None,
        issuer_id=None,
        state=None,
        prev_proposal_id=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Proposal - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._properties = None
        self._constraints = None
        self._proposal_id = None
        self._issuer_id = None
        self._state = None
        self._prev_proposal_id = None
        self.discriminator = None

        self.properties = properties
        self.constraints = constraints
        if proposal_id is not None:
            self.proposal_id = proposal_id
        if issuer_id is not None:
            self.issuer_id = issuer_id
        if state is not None:
            self.state = state
        if prev_proposal_id is not None:
            self.prev_proposal_id = prev_proposal_id

    @property
    def properties(self):
        """Gets the properties of this Proposal.  # noqa: E501


        :return: The properties of this Proposal.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this Proposal.


        :param properties: The properties of this Proposal.  # noqa: E501
        :type: object
        """
        if (
            self.local_vars_configuration.client_side_validation and properties is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `properties`, must not be `None`"
            )  # noqa: E501

        self._properties = properties

    @property
    def constraints(self):
        """Gets the constraints of this Proposal.  # noqa: E501


        :return: The constraints of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        """Sets the constraints of this Proposal.


        :param constraints: The constraints of this Proposal.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and constraints is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `constraints`, must not be `None`"
            )  # noqa: E501

        self._constraints = constraints

    @property
    def proposal_id(self):
        """Gets the proposal_id of this Proposal.  # noqa: E501


        :return: The proposal_id of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._proposal_id

    @proposal_id.setter
    def proposal_id(self, proposal_id):
        """Sets the proposal_id of this Proposal.


        :param proposal_id: The proposal_id of this Proposal.  # noqa: E501
        :type: str
        """

        self._proposal_id = proposal_id

    @property
    def issuer_id(self):
        """Gets the issuer_id of this Proposal.  # noqa: E501


        :return: The issuer_id of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._issuer_id

    @issuer_id.setter
    def issuer_id(self, issuer_id):
        """Sets the issuer_id of this Proposal.


        :param issuer_id: The issuer_id of this Proposal.  # noqa: E501
        :type: str
        """

        self._issuer_id = issuer_id

    @property
    def state(self):
        """Gets the state of this Proposal.  # noqa: E501

        * `Initial` - proposal arrived from the market as response to subscription * `Draft` - bespoke counter-proposal issued by one party directly to other party (negotiation phase) * `Rejected` by other party * `Accepted` - promoted into the Agreement draft * `Expired` - not accepted nor rejected before validity period   # noqa: E501

        :return: The state of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Proposal.

        * `Initial` - proposal arrived from the market as response to subscription * `Draft` - bespoke counter-proposal issued by one party directly to other party (negotiation phase) * `Rejected` by other party * `Accepted` - promoted into the Agreement draft * `Expired` - not accepted nor rejected before validity period   # noqa: E501

        :param state: The state of this Proposal.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "Initial",
            "Draft",
            "Rejected",
            "Accepted",
            "Expired",
        ]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and state not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}".format(  # noqa: E501
                    state, allowed_values
                )
            )

        self._state = state

    @property
    def prev_proposal_id(self):
        """Gets the prev_proposal_id of this Proposal.  # noqa: E501

        id of the proposal from other side which this proposal responds to   # noqa: E501

        :return: The prev_proposal_id of this Proposal.  # noqa: E501
        :rtype: str
        """
        return self._prev_proposal_id

    @prev_proposal_id.setter
    def prev_proposal_id(self, prev_proposal_id):
        """Sets the prev_proposal_id of this Proposal.

        id of the proposal from other side which this proposal responds to   # noqa: E501

        :param prev_proposal_id: The prev_proposal_id of this Proposal.  # noqa: E501
        :type: str
        """

        self._prev_proposal_id = prev_proposal_id

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
        if not isinstance(other, Proposal):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Proposal):
            return True

        return self.to_dict() != other.to_dict()
