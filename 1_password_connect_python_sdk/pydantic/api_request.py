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

from 1_password_connect_python_sdk.pydantic.api_request_actor import APIRequestActor
from 1_password_connect_python_sdk.pydantic.api_request_resource import APIRequestResource

class APIRequest(BaseModel):
    # The unique id used to identify a single request.
    request_id: typing.Optional[str] = Field(None, alias='requestId')

    # The time at which the request was processed by the server.
    timestamp: typing.Optional[datetime] = Field(None, alias='timestamp')

    action: typing.Optional[Literal["READ", "CREATE", "UPDATE", "DELETE"]] = Field(None, alias='action')

    result: typing.Optional[Literal["SUCCESS", "DENY"]] = Field(None, alias='result')

    actor: typing.Optional[APIRequestActor] = Field(None, alias='actor')

    resource: typing.Optional[APIRequestResource] = Field(None, alias='resource')
    class Config:
        arbitrary_types_allowed = True
