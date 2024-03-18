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

from 1_password_connect_python_sdk.type.api_request_actor import APIRequestActor
from 1_password_connect_python_sdk.type.api_request_resource import APIRequestResource

class RequiredAPIRequest(TypedDict):
    pass

class OptionalAPIRequest(TypedDict, total=False):
    # The unique id used to identify a single request.
    requestId: str

    # The time at which the request was processed by the server.
    timestamp: datetime

    action: str

    result: str

    actor: APIRequestActor

    resource: APIRequestResource

class APIRequest(RequiredAPIRequest, OptionalAPIRequest):
    pass
