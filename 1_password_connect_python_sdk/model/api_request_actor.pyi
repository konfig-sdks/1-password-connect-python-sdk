# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from 1_password_connect_python_sdk import schemas  # noqa: F401


class APIRequestActor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.UUIDSchema
            account = schemas.StrSchema
            jti = schemas.StrSchema
            userAgent = schemas.StrSchema
            requestIp = schemas.StrSchema
            __annotations__ = {
                "id": id,
                "account": account,
                "jti": jti,
                "userAgent": userAgent,
                "requestIp": requestIp,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account"]) -> MetaOapg.properties.account: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["jti"]) -> MetaOapg.properties.jti: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["userAgent"]) -> MetaOapg.properties.userAgent: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestIp"]) -> MetaOapg.properties.requestIp: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "account", "jti", "userAgent", "requestIp", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account"]) -> typing.Union[MetaOapg.properties.account, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["jti"]) -> typing.Union[MetaOapg.properties.jti, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["userAgent"]) -> typing.Union[MetaOapg.properties.userAgent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestIp"]) -> typing.Union[MetaOapg.properties.requestIp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "account", "jti", "userAgent", "requestIp", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, str, uuid.UUID, schemas.Unset] = schemas.unset,
        account: typing.Union[MetaOapg.properties.account, str, schemas.Unset] = schemas.unset,
        jti: typing.Union[MetaOapg.properties.jti, str, schemas.Unset] = schemas.unset,
        userAgent: typing.Union[MetaOapg.properties.userAgent, str, schemas.Unset] = schemas.unset,
        requestIp: typing.Union[MetaOapg.properties.requestIp, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIRequestActor':
        return super().__new__(
            cls,
            *args,
            id=id,
            account=account,
            jti=jti,
            userAgent=userAgent,
            requestIp=requestIp,
            _configuration=_configuration,
            **kwargs,
        )
