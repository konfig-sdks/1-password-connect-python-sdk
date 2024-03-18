# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

import unittest
from unittest.mock import patch

import urllib3

import 1_password_connect_python_sdk
from 1_password_connect_python_sdk.paths.activity import get
from 1_password_connect_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestActivity(ApiTestMixin, unittest.TestCase):
    """
    Activity unit test stubs
        Retrieve a list of API Requests that have been made.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
