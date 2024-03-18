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

from 1_password_connect_python_sdk.pydantic.field_section import FieldSection
from 1_password_connect_python_sdk.pydantic.generator_recipe import GeneratorRecipe

class Field(BaseModel):
    id: str = Field(alias='id')

    type: Literal["STRING", "EMAIL", "CONCEALED", "URL", "TOTP", "DATE", "MONTH_YEAR", "MENU"] = Field(alias='type')

    section: typing.Optional[FieldSection] = Field(None, alias='section')

    # Some item types, Login and Password, have fields used for autofill. This property indicates that purpose and is required for some item types.
    purpose: typing.Optional[Literal["", "USERNAME", "PASSWORD", "NOTES"]] = Field(None, alias='purpose')

    label: typing.Optional[str] = Field(None, alias='label')

    value: typing.Optional[str] = Field(None, alias='value')

    # If value is not present then a new value should be generated for this field
    generate: typing.Optional[bool] = Field(None, alias='generate')

    recipe: typing.Optional[GeneratorRecipe] = Field(None, alias='recipe')

    # For fields with a purpose of `PASSWORD` this is the entropy of the value
    entropy: typing.Optional[typing.Union[int, float]] = Field(None, alias='entropy')
    class Config:
        arbitrary_types_allowed = True
