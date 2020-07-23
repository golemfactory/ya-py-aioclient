# coding: utf-8

"""
    Yagna Activity API

    It conforms with capability level 1 of the [Activity API specification](https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401


from ya_activity.configuration import Configuration


class ExeScriptCommandResult(object):
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
        "index": "int",
        "result": "str",
        "message": "str",
        "is_batch_finished": "bool",
    }

    attribute_map = {
        "index": "index",
        "result": "result",
        "message": "message",
        "is_batch_finished": "isBatchFinished",
    }

    def __init__(
        self,
        index=None,
        result=None,
        message=None,
        is_batch_finished=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """ExeScriptCommandResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._index = None
        self._result = None
        self._message = None
        self._is_batch_finished = None
        self.discriminator = None

        self.index = index
        self.result = result
        if message is not None:
            self.message = message
        if is_batch_finished is not None:
            self.is_batch_finished = is_batch_finished

    @property
    def index(self):
        """Gets the index of this ExeScriptCommandResult.  # noqa: E501


        :return: The index of this ExeScriptCommandResult.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ExeScriptCommandResult.


        :param index: The index of this ExeScriptCommandResult.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and index is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `index`, must not be `None`"
            )  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and index is not None
            and index < 0
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `index`, must be a value greater than or equal to `0`"
            )  # noqa: E501

        self._index = index

    @property
    def result(self):
        """Gets the result of this ExeScriptCommandResult.  # noqa: E501


        :return: The result of this ExeScriptCommandResult.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ExeScriptCommandResult.


        :param result: The result of this ExeScriptCommandResult.  # noqa: E501
        :type: str
        """
        if (
            self.local_vars_configuration.client_side_validation and result is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result`, must not be `None`"
            )  # noqa: E501
        allowed_values = ["Ok", "Error"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and result not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `result` ({0}), must be one of {1}".format(  # noqa: E501
                    result, allowed_values
                )
            )

        self._result = result

    @property
    def message(self):
        """Gets the message of this ExeScriptCommandResult.  # noqa: E501


        :return: The message of this ExeScriptCommandResult.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ExeScriptCommandResult.


        :param message: The message of this ExeScriptCommandResult.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def is_batch_finished(self):
        """Gets the is_batch_finished of this ExeScriptCommandResult.  # noqa: E501


        :return: The is_batch_finished of this ExeScriptCommandResult.  # noqa: E501
        :rtype: bool
        """
        return self._is_batch_finished

    @is_batch_finished.setter
    def is_batch_finished(self, is_batch_finished):
        """Sets the is_batch_finished of this ExeScriptCommandResult.


        :param is_batch_finished: The is_batch_finished of this ExeScriptCommandResult.  # noqa: E501
        :type: bool
        """

        self._is_batch_finished = is_batch_finished

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
        if not isinstance(other, ExeScriptCommandResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ExeScriptCommandResult):
            return True

        return self.to_dict() != other.to_dict()
