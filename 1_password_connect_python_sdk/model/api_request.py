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


class APIRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Represents a request that was made to the API. Including what Token was used and what resource was accessed.
    """


    class MetaOapg:
        
        class properties:
            requestId = schemas.UUIDSchema
            timestamp = schemas.DateTimeSchema
            
            
            class action(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "READ": "READ",
                        "CREATE": "CREATE",
                        "UPDATE": "UPDATE",
                        "DELETE": "DELETE",
                    }
                
                @schemas.classproperty
                def READ(cls):
                    return cls("READ")
                
                @schemas.classproperty
                def CREATE(cls):
                    return cls("CREATE")
                
                @schemas.classproperty
                def UPDATE(cls):
                    return cls("UPDATE")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("DELETE")
            
            
            class result(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "SUCCESS": "SUCCESS",
                        "DENY": "DENY",
                    }
                
                @schemas.classproperty
                def SUCCESS(cls):
                    return cls("SUCCESS")
                
                @schemas.classproperty
                def DENY(cls):
                    return cls("DENY")
        
            @staticmethod
            def actor() -> typing.Type['APIRequestActor']:
                return APIRequestActor
        
            @staticmethod
            def resource() -> typing.Type['APIRequestResource']:
                return APIRequestResource
            __annotations__ = {
                "requestId": requestId,
                "timestamp": timestamp,
                "action": action,
                "result": result,
                "actor": actor,
                "resource": resource,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requestId"]) -> MetaOapg.properties.requestId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["timestamp"]) -> MetaOapg.properties.timestamp: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["result"]) -> MetaOapg.properties.result: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["actor"]) -> 'APIRequestActor': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource"]) -> 'APIRequestResource': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["requestId", "timestamp", "action", "result", "actor", "resource", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requestId"]) -> typing.Union[MetaOapg.properties.requestId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["timestamp"]) -> typing.Union[MetaOapg.properties.timestamp, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["result"]) -> typing.Union[MetaOapg.properties.result, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["actor"]) -> typing.Union['APIRequestActor', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource"]) -> typing.Union['APIRequestResource', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["requestId", "timestamp", "action", "result", "actor", "resource", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        requestId: typing.Union[MetaOapg.properties.requestId, str, uuid.UUID, schemas.Unset] = schemas.unset,
        timestamp: typing.Union[MetaOapg.properties.timestamp, str, datetime, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, str, schemas.Unset] = schemas.unset,
        result: typing.Union[MetaOapg.properties.result, str, schemas.Unset] = schemas.unset,
        actor: typing.Union['APIRequestActor', schemas.Unset] = schemas.unset,
        resource: typing.Union['APIRequestResource', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'APIRequest':
        return super().__new__(
            cls,
            *args,
            requestId=requestId,
            timestamp=timestamp,
            action=action,
            result=result,
            actor=actor,
            resource=resource,
            _configuration=_configuration,
            **kwargs,
        )

from 1_password_connect_python_sdk.model.api_request_actor import APIRequestActor
from 1_password_connect_python_sdk.model.api_request_resource import APIRequestResource
