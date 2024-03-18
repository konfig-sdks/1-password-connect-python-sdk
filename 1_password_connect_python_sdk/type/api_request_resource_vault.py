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


class RequiredAPIRequestResourceVault(TypedDict):
    pass

class OptionalAPIRequestResourceVault(TypedDict, total=False):
    id: str

class APIRequestResourceVault(RequiredAPIRequestResourceVault, OptionalAPIRequestResourceVault):
    pass
