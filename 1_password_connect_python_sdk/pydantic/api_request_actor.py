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


class APIRequestActor(BaseModel):
    id: typing.Optional[str] = Field(None, alias='id')

    account: typing.Optional[str] = Field(None, alias='account')

    jti: typing.Optional[str] = Field(None, alias='jti')

    user_agent: typing.Optional[str] = Field(None, alias='userAgent')

    request_ip: typing.Optional[str] = Field(None, alias='requestIp')
    class Config:
        arbitrary_types_allowed = True
