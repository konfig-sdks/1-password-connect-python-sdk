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

from 1_password_connect_python_sdk.type.field_section import FieldSection
from 1_password_connect_python_sdk.type.generator_recipe import GeneratorRecipe

class RequiredField(TypedDict):
    id: str

    type: str

class OptionalField(TypedDict, total=False):
    section: FieldSection

    # Some item types, Login and Password, have fields used for autofill. This property indicates that purpose and is required for some item types.
    purpose: str

    label: str

    value: str

    # If value is not present then a new value should be generated for this field
    generate: bool

    recipe: GeneratorRecipe

    # For fields with a purpose of `PASSWORD` this is the entropy of the value
    entropy: typing.Union[int, float]

class Field(RequiredField, OptionalField):
    pass
