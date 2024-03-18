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

from 1_password_connect_python_sdk.model.files_get_all_files_inside_item_response import FilesGetAllFilesInsideItemResponse as FilesGetAllFilesInsideItemResponseSchema
from 1_password_connect_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from 1_password_connect_python_sdk.type.error_response import ErrorResponse
from 1_password_connect_python_sdk.type.files_get_all_files_inside_item_response import FilesGetAllFilesInsideItemResponse

from ...api_client import Dictionary
from 1_password_connect_python_sdk.pydantic.files_get_all_files_inside_item_response import FilesGetAllFilesInsideItemResponse as FilesGetAllFilesInsideItemResponsePydantic
from 1_password_connect_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic

# Query params
InlineFilesSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'inline_files': typing.Union[InlineFilesSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_inline_files = api_client.QueryParameter(
    name="inline_files",
    style=api_client.ParameterStyle.FORM,
    schema=InlineFilesSchema,
    explode=True,
)
# Path params
VaultUuidSchema = schemas.UUIDSchema
ItemUuidSchema = schemas.UUIDSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'vaultUuid': typing.Union[VaultUuidSchema, str, uuid.UUID, ],
        'itemUuid': typing.Union[ItemUuidSchema, str, uuid.UUID, ],
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
request_path_item_uuid = api_client.PathParameter(
    name="itemUuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=ItemUuidSchema,
    required=True,
)
SchemaFor200ResponseBodyApplicationJson = FilesGetAllFilesInsideItemResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: FilesGetAllFilesInsideItemResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: FilesGetAllFilesInsideItemResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
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
SchemaFor413ResponseBodyApplicationJson = ErrorResponseSchema


@dataclass
class ApiResponseFor413(api_client.ApiResponse):
    body: ErrorResponse


@dataclass
class ApiResponseFor413Async(api_client.AsyncApiResponse):
    body: ErrorResponse


_response_for_413 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor413,
    response_cls_async=ApiResponseFor413Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor413ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_all_files_inside_item_mapped_args(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _path_params = {}
        if inline_files is not None:
            _query_params["inline_files"] = inline_files
        if vault_uuid is not None:
            _path_params["vaultUuid"] = vault_uuid
        if item_uuid is not None:
            _path_params["itemUuid"] = item_uuid
        args.query = _query_params
        args.path = _path_params
        return args

    async def _aget_all_files_inside_item_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get all the files inside an Item
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vault_uuid,
            request_path_item_uuid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_inline_files,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vaults/{vaultUuid}/items/{itemUuid}/files',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


    def _get_all_files_inside_item_oapg(
        self,
            query_params: typing.Optional[dict] = {},
            path_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get all the files inside an Item
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vault_uuid,
            request_path_item_uuid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)
    
        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_inline_files,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vaults/{vaultUuid}/items/{itemUuid}/files',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
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


class GetAllFilesInsideItemRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_all_files_inside_item(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_files_inside_item_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            inline_files=inline_files,
        )
        return await self._aget_all_files_inside_item_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get_all_files_inside_item(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_files_inside_item_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            inline_files=inline_files,
        )
        return self._get_all_files_inside_item_oapg(
            query_params=args.query,
            path_params=args.path,
        )

class GetAllFilesInsideItem(BaseApi):

    async def aget_all_files_inside_item(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
        validate: bool = False,
        **kwargs,
    ) -> FilesGetAllFilesInsideItemResponsePydantic:
        raw_response = await self.raw.aget_all_files_inside_item(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            inline_files=inline_files,
            **kwargs,
        )
        if validate:
            return RootModel[FilesGetAllFilesInsideItemResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(FilesGetAllFilesInsideItemResponsePydantic, raw_response.body)
    
    
    def get_all_files_inside_item(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
        validate: bool = False,
    ) -> FilesGetAllFilesInsideItemResponsePydantic:
        raw_response = self.raw.get_all_files_inside_item(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            inline_files=inline_files,
        )
        if validate:
            return RootModel[FilesGetAllFilesInsideItemResponsePydantic](raw_response.body).root
        return api_client.construct_model_instance(FilesGetAllFilesInsideItemResponsePydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_all_files_inside_item_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            inline_files=inline_files,
        )
        return await self._aget_all_files_inside_item_oapg(
            query_params=args.query,
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        vault_uuid: str,
        item_uuid: str,
        inline_files: typing.Optional[bool] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_all_files_inside_item_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            inline_files=inline_files,
        )
        return self._get_all_files_inside_item_oapg(
            query_params=args.query,
            path_params=args.path,
        )

