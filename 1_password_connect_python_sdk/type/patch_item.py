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


class RequiredPatchItem(TypedDict):
    op: str

    # An RFC6901 JSON Pointer pointing to the Item document, an Item Attribute, and Item Field by Field ID, or an Item Field Attribute
    path: str

class OptionalPatchItem(TypedDict, total=False):
    value: typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]

class PatchItem(RequiredPatchItem, OptionalPatchItem):
    pass
