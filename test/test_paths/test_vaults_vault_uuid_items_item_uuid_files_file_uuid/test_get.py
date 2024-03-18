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
from 1_password_connect_python_sdk.paths.vaults_vault_uuid_items_item_uuid_files_file_uuid import get
from 1_password_connect_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestVaultsVaultUuidItemsItemUuidFilesFileUuid(ApiTestMixin, unittest.TestCase):
    """
    VaultsVaultUuidItemsItemUuidFilesFileUuid unit test stubs
        Get the details of a File
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
