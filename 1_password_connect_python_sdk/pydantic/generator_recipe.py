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

from 1_password_connect_python_sdk.pydantic.generator_recipe_character_sets import GeneratorRecipeCharacterSets

class GeneratorRecipe(BaseModel):
    # Length of the generated value
    length: typing.Optional[int] = Field(None, alias='length')

    character_sets: typing.Optional[GeneratorRecipeCharacterSets] = Field(None, alias='characterSets')

    # List of all characters that should be excluded from generated passwords.
    exclude_characters: typing.Optional[str] = Field(None, alias='excludeCharacters')
    class Config:
        arbitrary_types_allowed = True
