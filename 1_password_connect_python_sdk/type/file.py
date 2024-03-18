# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING

from 1_password_connect_python_sdk.type.file_section import FileSection

class RequiredFile(TypedDict):
    pass

class OptionalFile(TypedDict, total=False):
    # ID of the file
    id: str

    # Name of the file
    name: str

    # Size in bytes of the file
    size: int

    # Path of the Connect API that can be used to download the contents of this file.
    content_path: str

    section: FileSection

    # Base64-encoded contents of the file. Only set if size <= OP_MAX_INLINE_FILE_SIZE_KB kb and `inline_files` is set to `true`.
    content: str

class File(RequiredFile, OptionalFile):
    pass
