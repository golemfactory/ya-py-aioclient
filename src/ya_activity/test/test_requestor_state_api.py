# coding: utf-8

"""
    Yagna Activity API

     The Activity API can be perceived as controls which a Requestor-side application has to steer the execution of an Activity as specified in an Agreement which has been negotiated via the Market API/Protocol. This defines possible interactions between the Requestor application (via Activity API) and the generic components running on the Provider node, which host the Provider-side application code. The possible interactions imply a logical “execution environment” component, which is the host/container for the “payload” code. The “execution environment” is specified as an ExeUnit, with a generic interface via which a Provider node’s Activity Controller can operate the hosted code. It conforms with capability level 1 of the [Activity API specification] (https://docs.google.com/document/d/1BXaN32ediXdBHljEApmznSfbuudTU8TmvOmHKl0gmQM).   # noqa: E501

    The version of the OpenAPI document: 1.6.1
    Generated by: https://openapi-generator.tech
"""

import unittest

import ya_activity
from ya_activity.api.requestor_state_api import RequestorStateApi  # noqa: E501
from ya_activity.rest import ApiException


class TestRequestorStateApi(unittest.TestCase):
    """RequestorStateApi unit test stubs"""

    def setUp(self):
        self.api = ya_activity.api.requestor_state_api.RequestorStateApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_activity_state(self):
        """Test case for get_activity_state

        Get state of specified Activity.  # noqa: E501
        """
        pass

    def test_get_activity_usage(self):
        """Test case for get_activity_usage

        Get usage of specified Activity.  # noqa: E501
        """
        pass

    def test_get_running_command(self):
        """Test case for get_running_command

        Get running commands for a specified Activity.  # noqa: E501
        """
        pass


if __name__ == "__main__":
    unittest.main()
