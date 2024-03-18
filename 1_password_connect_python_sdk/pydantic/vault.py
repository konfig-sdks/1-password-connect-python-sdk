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


class Vault(BaseModel):
    description: typing.Optional[str] = Field(None, alias='description')

    id: typing.Optional[str] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    # The vault version
    attribute_version: typing.Optional[int] = Field(None, alias='attributeVersion')

    # The version of the vault contents
    content_version: typing.Optional[int] = Field(None, alias='contentVersion')

    # Number of active items in the vault
    items: typing.Optional[int] = Field(None, alias='items')

    type: typing.Optional[Literal["USER_CREATED", "PERSONAL", "EVERYONE", "TRANSFER"]] = Field(None, alias='type')

    created_at: typing.Optional[datetime] = Field(None, alias='createdAt')

    updated_at: typing.Optional[datetime] = Field(None, alias='updatedAt')
    class Config:
        arbitrary_types_allowed = True
