# coding: utf-8

"""
    Yagna Payment API

     Invoicing and Payments is a fundamental area of Yagna Ecosystem functionality. It includes aspects of communication between Requestor, Provider and a selected Payment Platform, which becomes crucial when Activities are executed in the context of negotiated Agreements. Yagna applications must be able to exercise various payment models, and the Invoicing/Payment-related communication is happening in parallel to Activity control communication. To define functional patterns of Requestor/Provider interaction in this area, Payment API is specified.  An important principle of the Yagna Payment API is that the actual payment transactions are hidden behind the Invoice flow. In other words, a Yagna Application on Requestor side isn’t expected to trigger actual payment transactions. Instead it is expected to receive and accept Invoices raised by the Provider - based on Application’s Invoice Accept notifications, the Payment API implementation orchestrates the payment via a configured Payment platform.  **NOTE:** This specification is work-in-progress.   # noqa: E501

    The version of the OpenAPI document: 1.6.3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from ya_payment.configuration import Configuration


class Payment(object):
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
        "payment_id": "str",
        "payer_id": "str",
        "payee_id": "str",
        "payer_addr": "str",
        "payee_addr": "str",
        "payment_platform": "str",
        "amount": "str",
        "timestamp": "datetime",
        "agreement_payments": "list[AgreementPayment]",
        "activity_payments": "list[ActivityPayment]",
        "details": "str",
    }

    attribute_map = {
        "payment_id": "paymentId",
        "payer_id": "payerId",
        "payee_id": "payeeId",
        "payer_addr": "payerAddr",
        "payee_addr": "payeeAddr",
        "payment_platform": "paymentPlatform",
        "amount": "amount",
        "timestamp": "timestamp",
        "agreement_payments": "agreementPayments",
        "activity_payments": "activityPayments",
        "details": "details",
    }

    def __init__(
        self,
        payment_id=None,
        payer_id=None,
        payee_id=None,
        payer_addr=None,
        payee_addr=None,
        payment_platform=None,
        amount=None,
        timestamp=None,
        agreement_payments=None,
        activity_payments=None,
        details=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """Payment - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._payment_id = None
        self._payer_id = None
        self._payee_id = None
        self._payer_addr = None
        self._payee_addr = None
        self._payment_platform = None
        self._amount = None
        self._timestamp = None
        self._agreement_payments = None
        self._activity_payments = None
        self._details = None
        self.discriminator = None

        self.payment_id = payment_id
        self.payer_id = payer_id
        self.payee_id = payee_id
        self.payer_addr = payer_addr
        self.payee_addr = payee_addr
        self.payment_platform = payment_platform
        self.amount = amount
        self.timestamp = timestamp
        self.agreement_payments = agreement_payments
        self.activity_payments = activity_payments
        self.details = details

    @property
    def payment_id(self):
        """Gets the payment_id of this Payment.  # noqa: E501


        :return: The payment_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_id

    @payment_id.setter
    def payment_id(self, payment_id):
        """Sets the payment_id of this Payment.


        :param payment_id: The payment_id of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and payment_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_id`, must not be `None`"
            )  # noqa: E501

        self._payment_id = payment_id

    @property
    def payer_id(self):
        """Gets the payer_id of this Payment.  # noqa: E501


        :return: The payer_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payer_id

    @payer_id.setter
    def payer_id(self, payer_id):
        """Sets the payer_id of this Payment.


        :param payer_id: The payer_id of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and payer_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payer_id`, must not be `None`"
            )  # noqa: E501

        self._payer_id = payer_id

    @property
    def payee_id(self):
        """Gets the payee_id of this Payment.  # noqa: E501


        :return: The payee_id of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payee_id

    @payee_id.setter
    def payee_id(self, payee_id):
        """Sets the payee_id of this Payment.


        :param payee_id: The payee_id of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and payee_id is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payee_id`, must not be `None`"
            )  # noqa: E501

        self._payee_id = payee_id

    @property
    def payer_addr(self):
        """Gets the payer_addr of this Payment.  # noqa: E501


        :return: The payer_addr of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payer_addr

    @payer_addr.setter
    def payer_addr(self, payer_addr):
        """Sets the payer_addr of this Payment.


        :param payer_addr: The payer_addr of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and payer_addr is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payer_addr`, must not be `None`"
            )  # noqa: E501

        self._payer_addr = payer_addr

    @property
    def payee_addr(self):
        """Gets the payee_addr of this Payment.  # noqa: E501


        :return: The payee_addr of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payee_addr

    @payee_addr.setter
    def payee_addr(self, payee_addr):
        """Sets the payee_addr of this Payment.


        :param payee_addr: The payee_addr of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and payee_addr is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payee_addr`, must not be `None`"
            )  # noqa: E501

        self._payee_addr = payee_addr

    @property
    def payment_platform(self):
        """Gets the payment_platform of this Payment.  # noqa: E501


        :return: The payment_platform of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._payment_platform

    @payment_platform.setter
    def payment_platform(self, payment_platform):
        """Sets the payment_platform of this Payment.


        :param payment_platform: The payment_platform of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation
            and payment_platform is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `payment_platform`, must not be `None`"
            )  # noqa: E501

        self._payment_platform = payment_platform

    @property
    def amount(self):
        """Gets the amount of this Payment.  # noqa: E501


        :return: The amount of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Payment.


        :param amount: The amount of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and amount is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `amount`, must not be `None`"
            )  # noqa: E501

        self._amount = amount

    @property
    def timestamp(self):
        """Gets the timestamp of this Payment.  # noqa: E501


        :return: The timestamp of this Payment.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Payment.


        :param timestamp: The timestamp of this Payment.  # noqa: E501
        :type: datetime
        """
        if (
            self.local_vars_configuration.client_side_validation and timestamp is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `timestamp`, must not be `None`"
            )  # noqa: E501

        self._timestamp = timestamp

    @property
    def agreement_payments(self):
        """Gets the agreement_payments of this Payment.  # noqa: E501


        :return: The agreement_payments of this Payment.  # noqa: E501
        :rtype: list[AgreementPayment]
        """
        return self._agreement_payments

    @agreement_payments.setter
    def agreement_payments(self, agreement_payments):
        """Sets the agreement_payments of this Payment.


        :param agreement_payments: The agreement_payments of this Payment.  # noqa: E501
        :type: list[AgreementPayment]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and agreement_payments is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `agreement_payments`, must not be `None`"
            )  # noqa: E501

        self._agreement_payments = agreement_payments

    @property
    def activity_payments(self):
        """Gets the activity_payments of this Payment.  # noqa: E501


        :return: The activity_payments of this Payment.  # noqa: E501
        :rtype: list[ActivityPayment]
        """
        return self._activity_payments

    @activity_payments.setter
    def activity_payments(self, activity_payments):
        """Sets the activity_payments of this Payment.


        :param activity_payments: The activity_payments of this Payment.  # noqa: E501
        :type: list[ActivityPayment]
        """
        if (
            self.local_vars_configuration.client_side_validation
            and activity_payments is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `activity_payments`, must not be `None`"
            )  # noqa: E501

        self._activity_payments = activity_payments

    @property
    def details(self):
        """Gets the details of this Payment.  # noqa: E501


        :return: The details of this Payment.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this Payment.


        :param details: The details of this Payment.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and details is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `details`, must not be `None`"
            )  # noqa: E501

        self._details = details

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
        if not isinstance(other, Payment):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Payment):
            return True

        return self.to_dict() != other.to_dict()
