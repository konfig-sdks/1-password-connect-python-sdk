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
from pydantic import BaseModel, Field, RootModel

from 1_password_connect_python_sdk.pydantic.file_section import FileSection

class File(BaseModel):
    # ID of the file
    id: typing.Optional[str] = Field(None, alias='id')

    # Name of the file
    name: typing.Optional[str] = Field(None, alias='name')

    # Size in bytes of the file
    size: typing.Optional[int] = Field(None, alias='size')

    # Path of the Connect API that can be used to download the contents of this file.
    content_path: typing.Optional[str] = Field(None, alias='content_path')

    section: typing.Optional[FileSection] = Field(None, alias='section')

    # Base64-encoded contents of the file. Only set if size <= OP_MAX_INLINE_FILE_SIZE_KB kb and `inline_files` is set to `true`.
    content: typing.Optional[str] = Field(None, alias='content')
    class Config:
        arbitrary_types_allowed = True
