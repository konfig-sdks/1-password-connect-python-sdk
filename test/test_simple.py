# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

import unittest

import os
from pprint import pprint
from 1_password_connect_python_sdk import OnePasswordConnect

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        onepasswordconnect = OnePasswordConnect(
        
            access_token = 'YOUR_BEARER_TOKEN'
        )
        self.assertIsNotNone(onepasswordconnect)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
