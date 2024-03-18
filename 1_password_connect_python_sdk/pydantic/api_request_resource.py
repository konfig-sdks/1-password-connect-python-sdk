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

from 1_password_connect_python_sdk.pydantic.api_request_resource_item import APIRequestResourceItem
from 1_password_connect_python_sdk.pydantic.api_request_resource_vault import APIRequestResourceVault

class APIRequestResource(BaseModel):
    type: typing.Optional[Literal["ITEM", "VAULT"]] = Field(None, alias='type')

    vault: typing.Optional[APIRequestResourceVault] = Field(None, alias='vault')

    item: typing.Optional[APIRequestResourceItem] = Field(None, alias='item')

    item_version: typing.Optional[int] = Field(None, alias='itemVersion')
    class Config:
        arbitrary_types_allowed = True
