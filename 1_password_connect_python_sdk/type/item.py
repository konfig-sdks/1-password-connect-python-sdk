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

from 1_password_connect_python_sdk.type.item_tags import ItemTags
from 1_password_connect_python_sdk.type.item_urls import ItemUrls
from 1_password_connect_python_sdk.type.item_vault import ItemVault

class RequiredItem(TypedDict):
    vault: ItemVault

    category: str

class OptionalItem(TypedDict, total=False):
    tags: ItemTags

    title: str

    version: int

    id: str

    urls: ItemUrls

    favorite: bool

    state: str

    createdAt: datetime

    updatedAt: datetime

    lastEditedBy: str

class Item(RequiredItem, OptionalItem):
    pass
