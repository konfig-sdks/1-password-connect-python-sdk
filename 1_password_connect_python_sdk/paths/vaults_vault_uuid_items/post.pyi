# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from 1_password_connect_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from 1_password_connect_python_sdk.api_response import AsyncGeneratorResponse
from 1_password_connect_python_sdk import api_client, exceptions
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

from 1_password_connect_python_sdk.model.item_urls import ItemUrls as ItemUrlsSchema
from 1_password_connect_python_sdk.model.file import File as FileSchema
from 1_password_connect_python_sdk.model.full_item import FullItem as FullItemSchema
from 1_password_connect_python_sdk.model.field import Field as FieldSchema
from 1_password_connect_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema
from 1_password_connect_python_sdk.model.item_tags import ItemTags as ItemTagsSchema
from 1_password_connect_python_sdk.model.item_vault import ItemVault as ItemVaultSchema

from 1_password_connect_python_sdk.type.item_tags import ItemTags
from 1_password_connect_python_sdk.type.item_vault import ItemVault
from 1_password_connect_python_sdk.type.file import File
from 1_password_connect_python_sdk.type.error_response import ErrorResponse
from 1_password_connect_python_sdk.type.item_urls import ItemUrls
from 1_password_connect_python_sdk.type.full_item import FullItem
from 1_password_connect_python_sdk.type.field import Field

from ...api_client import Dictionary
from 1_password_connect_python_sdk.pydantic.item_urls import ItemUrls as ItemUrlsPydantic
from 1_password_connect_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic
from 1_password_connect_python_sdk.pydantic.full_item import FullItem as FullItemPydantic
from 1_password_connect_python_sdk.pydantic.item_tags import ItemTags as ItemTagsPydantic
from 1_password_connect_python_sdk.pydantic.file import File as FilePydantic
from 1_password_connect_python_sdk.pydantic.item_vault import ItemVault as ItemVaultPydantic
from 1_password_connect_python_sdk.pydantic.field import Field as FieldPydantic

# Path params


class VaultUuidSchema(
    schemas.StrSchema
):
    pass
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'vaultUuid': typing.Union[VaultUuidSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_vault_uuid = api_client.PathParameter(
    name="vaultUuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=VaultUuidSchema,
    required=True,
)
# body param
SchemaForRequestBodyApplicationJson = FullItemSchema


request_body_full_item = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = FullItemSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FullItem


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FullItem


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor403Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    response_cls_async=ApiResponseFor403Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _create_new_item_mapped_args(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        _body = {}
        if tags is not None:
            _body["tags"] = tags
        if title is not None:
            _body["title"] = title
        if version is not None:
            _body["version"] = version
        if id is not None:
            _body["id"] = id
        if vault is not None:
            _body["vault"] = vault
        if category is not None:
            _body["category"] = category
        if urls is not None:
            _body["urls"] = urls
        if favorite is not None:
            _body["favorite"] = favorite
        if state is not None:
            _body["state"] = state
        if created_at is not None:
            _body["createdAt"] = created_at
        if updated_at is not None:
            _body["updatedAt"] = updated_at
        if last_edited_by is not None:
            _body["lastEditedBy"] = last_edited_by
        if sections is not None:
            _body["sections"] = sections
        if fields is not None:
            _body["fields"] = fields
        if files is not None:
            _body["files"] = files
        args.body = _body
        if vault_uuid is not None:
            _path_params["vaultUuid"] = vault_uuid
        args.path = _path_params
        return args

    async def _acreate_new_item_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create a new Item
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vault_uuid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vaults/{vaultUuid}/items',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_full_item.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_new_item_oapg(
        self,
        body: typing.Any = None,
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create a new Item
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vault_uuid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vaults/{vaultUuid}/items',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_full_item.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateNewItemRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_new_item(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_item_mapped_args(
            body=body,
            vault_uuid=vault_uuid,
            tags=tags,
            title=title,
            version=version,
            id=id,
            vault=vault,
            category=category,
            urls=urls,
            favorite=favorite,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            last_edited_by=last_edited_by,
            sections=sections,
            fields=fields,
            files=files,
        )
        return await self._acreate_new_item_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def create_new_item(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_item_mapped_args(
            body=body,
            vault_uuid=vault_uuid,
            tags=tags,
            title=title,
            version=version,
            id=id,
            vault=vault,
            category=category,
            urls=urls,
            favorite=favorite,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            last_edited_by=last_edited_by,
            sections=sections,
            fields=fields,
            files=files,
        )
        return self._create_new_item_oapg(
            body=args.body,
            path_params=args.path,
        )

class CreateNewItem(BaseApi):

    async def acreate_new_item(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
        validate: bool = False,
        **kwargs,
    ) -> FullItemPydantic:
        raw_response = await self.raw.acreate_new_item(
            body=body,
            vault_uuid=vault_uuid,
            tags=tags,
            title=title,
            version=version,
            id=id,
            vault=vault,
            category=category,
            urls=urls,
            favorite=favorite,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            last_edited_by=last_edited_by,
            sections=sections,
            fields=fields,
            files=files,
            **kwargs,
        )
        if validate:
            return RootModel[FullItemPydantic](raw_response.body).root
        return api_client.construct_model_instance(FullItemPydantic, raw_response.body)
    
    
    def create_new_item(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
        validate: bool = False,
    ) -> FullItemPydantic:
        raw_response = self.raw.create_new_item(
            body=body,
            vault_uuid=vault_uuid,
            tags=tags,
            title=title,
            version=version,
            id=id,
            vault=vault,
            category=category,
            urls=urls,
            favorite=favorite,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            last_edited_by=last_edited_by,
            sections=sections,
            fields=fields,
            files=files,
        )
        if validate:
            return RootModel[FullItemPydantic](raw_response.body).root
        return api_client.construct_model_instance(FullItemPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_new_item_mapped_args(
            body=body,
            vault_uuid=vault_uuid,
            tags=tags,
            title=title,
            version=version,
            id=id,
            vault=vault,
            category=category,
            urls=urls,
            favorite=favorite,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            last_edited_by=last_edited_by,
            sections=sections,
            fields=fields,
            files=files,
        )
        return await self._acreate_new_item_oapg(
            body=args.body,
            path_params=args.path,
            **kwargs,
        )
    
    def post(
        self,
        vault_uuid: str,
        tags: typing.Optional[ItemTags] = None,
        title: typing.Optional[str] = None,
        version: typing.Optional[int] = None,
        id: typing.Optional[str] = None,
        vault: typing.Optional[ItemVault] = None,
        category: typing.Optional[str] = None,
        urls: typing.Optional[ItemUrls] = None,
        favorite: typing.Optional[bool] = None,
        state: typing.Optional[str] = None,
        created_at: typing.Optional[datetime] = None,
        updated_at: typing.Optional[datetime] = None,
        last_edited_by: typing.Optional[str] = None,
        sections: typing.Optional[typing.List[typing.Dict[str, typing.Union[bool, date, datetime, dict, float, int, list, str, None]]]] = None,
        fields: typing.Optional[typing.List[Field]] = None,
        files: typing.Optional[typing.List[File]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_new_item_mapped_args(
            body=body,
            vault_uuid=vault_uuid,
            tags=tags,
            title=title,
            version=version,
            id=id,
            vault=vault,
            category=category,
            urls=urls,
            favorite=favorite,
            state=state,
            created_at=created_at,
            updated_at=updated_at,
            last_edited_by=last_edited_by,
            sections=sections,
            fields=fields,
            files=files,
        )
        return self._create_new_item_oapg(
            body=args.body,
            path_params=args.path,
        )

