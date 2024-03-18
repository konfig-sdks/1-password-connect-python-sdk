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


class RequiredVault(TypedDict):
    pass

class OptionalVault(TypedDict, total=False):
    description: str

    id: str

    name: str

    # The vault version
    attributeVersion: int

    # The version of the vault contents
    contentVersion: int

    # Number of active items in the vault
    items: int

    type: str

    createdAt: datetime

    updatedAt: datetime

class Vault(RequiredVault, OptionalVault):
    pass
