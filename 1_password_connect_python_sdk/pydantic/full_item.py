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

from 1_password_connect_python_sdk.pydantic.field import Field
from 1_password_connect_python_sdk.pydantic.file import File
from 1_password_connect_python_sdk.pydantic.item import Item

FullItem = typing.Union[Item,typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]
