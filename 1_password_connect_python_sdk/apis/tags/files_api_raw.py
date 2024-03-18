# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

from 1_password_connect_python_sdk.paths.vaults_vault_uuid_items_item_uuid_files.get import GetAllFilesInsideItemRaw
from 1_password_connect_python_sdk.paths.vaults_vault_uuid_items_item_uuid_files_file_uuid_content.get import GetContentRaw
from 1_password_connect_python_sdk.paths.vaults_vault_uuid_items_item_uuid_files_file_uuid.get import GetFileDetailsRaw


class FilesApiRaw(
    GetAllFilesInsideItemRaw,
    GetContentRaw,
    GetFileDetailsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
