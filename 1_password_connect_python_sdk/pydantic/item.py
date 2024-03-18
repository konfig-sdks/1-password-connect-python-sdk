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

from 1_password_connect_python_sdk.pydantic.item_tags import ItemTags
from 1_password_connect_python_sdk.pydantic.item_urls import ItemUrls
from 1_password_connect_python_sdk.pydantic.item_vault import ItemVault

class Item(BaseModel):
    vault: ItemVault = Field(alias='vault')

    category: Literal["LOGIN", "PASSWORD", "API_CREDENTIAL", "SERVER", "DATABASE", "CREDIT_CARD", "MEMBERSHIP", "PASSPORT", "SOFTWARE_LICENSE", "OUTDOOR_LICENSE", "SECURE_NOTE", "WIRELESS_ROUTER", "BANK_ACCOUNT", "DRIVER_LICENSE", "IDENTITY", "REWARD_PROGRAM", "DOCUMENT", "EMAIL_ACCOUNT", "SOCIAL_SECURITY_NUMBER", "MEDICAL_RECORD", "SSH_KEY", "CUSTOM"] = Field(alias='category')

    tags: typing.Optional[ItemTags] = Field(None, alias='tags')

    title: typing.Optional[str] = Field(None, alias='title')

    version: typing.Optional[int] = Field(None, alias='version')

    id: typing.Optional[str] = Field(None, alias='id')

    urls: typing.Optional[ItemUrls] = Field(None, alias='urls')

    favorite: typing.Optional[bool] = Field(None, alias='favorite')

    state: typing.Optional[Literal["ARCHIVED", "DELETED"]] = Field(None, alias='state')

    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    updated_at: typing.Optional[datetime] = Field(None, alias='updatedAt')

    last_edited_by: typing.Optional[str] = Field(None, alias='lastEditedBy')
    class Config:
        arbitrary_types_allowed = True
