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

from 1_password_connect_python_sdk.type.generator_recipe_character_sets import GeneratorRecipeCharacterSets

class RequiredGeneratorRecipe(TypedDict):
    pass

class OptionalGeneratorRecipe(TypedDict, total=False):
    # Length of the generated value
    length: int

    characterSets: GeneratorRecipeCharacterSets

    # List of all characters that should be excluded from generated passwords.
    excludeCharacters: str

class GeneratorRecipe(RequiredGeneratorRecipe, OptionalGeneratorRecipe):
    pass
