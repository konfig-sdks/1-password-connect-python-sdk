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

from 1_password_connect_python_sdk.model.error_response import ErrorResponse as ErrorResponseSchema

from 1_password_connect_python_sdk.type.error_response import ErrorResponse

from ...api_client import Dictionary
from 1_password_connect_python_sdk.pydantic.error_response import ErrorResponse as ErrorResponsePydantic

# Path params
VaultUuidSchema = schemas.UUIDSchema
ItemUuidSchema = schemas.UUIDSchema
FileUuidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'vaultUuid': typing.Union[VaultUuidSchema, str, uuid.UUID, ],
        'itemUuid': typing.Union[ItemUuidSchema, str, uuid.UUID, ],
        'fileUuid': typing.Union[FileUuidSchema, str, ],
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
request_path_file_uuid = api_client.PathParameter(
    name="fileUuid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=FileUuidSchema,
    required=True,
)
ContentDispositionSchema = schemas.StrSchema
ContentLengthSchema = schemas.StrSchema
SchemaFor200ResponseBodyApplicationOctetStream = schemas.BinarySchema
ResponseHeadersFor200 = typing_extensions.TypedDict(
    'ResponseHeadersFor200',
    {
        'Content-Disposition': ContentDispositionSchema,
        'Content-Length': ContentLengthSchema,
    }
)


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: typing.IO


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: typing.IO


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/octet-stream': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationOctetStream),
    },
    headers=[
        content_disposition_parameter,
        content_length_parameter,
    ]
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
_all_accept_content_types = (
    'application/octet-stream',
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_content_mapped_args(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _path_params = {}
        if vault_uuid is not None:
            _path_params["vaultUuid"] = vault_uuid
        if item_uuid is not None:
            _path_params["itemUuid"] = item_uuid
        if file_uuid is not None:
            _path_params["fileUuid"] = file_uuid
        args.path = _path_params
        return args

    async def _aget_content_oapg(
        self,
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
        Get the content of a File
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vault_uuid,
            request_path_item_uuid,
            request_path_file_uuid,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}/content',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _get_content_oapg(
        self,
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
        Get the content of a File
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value
    
        _path_params = {}
        for parameter in (
            request_path_vault_uuid,
            request_path_item_uuid,
            request_path_file_uuid,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}/content',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class GetContentRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_content(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_content_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            file_uuid=file_uuid,
        )
        return await self._aget_content_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get_content(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_content_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            file_uuid=file_uuid,
        )
        return self._get_content_oapg(
            path_params=args.path,
        )

class GetContent(BaseApi):

    async def aget_content(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
        validate: bool = False,
        **kwargs,
    ) -> typing.IO:
        raw_response = await self.raw.aget_content(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            file_uuid=file_uuid,
            **kwargs,
        )
        if validate:
            return RootModel[typing.IO](raw_response.body).root
        return raw_response.body
    
    
    def get_content(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
        validate: bool = False,
    ) -> typing.IO:
        raw_response = self.raw.get_content(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            file_uuid=file_uuid,
        )
        if validate:
            return RootModel[typing.IO](raw_response.body).root
        return raw_response.body


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_content_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            file_uuid=file_uuid,
        )
        return await self._aget_content_oapg(
            path_params=args.path,
            **kwargs,
        )
    
    def get(
        self,
        vault_uuid: str,
        item_uuid: str,
        file_uuid: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_content_mapped_args(
            vault_uuid=vault_uuid,
            item_uuid=item_uuid,
            file_uuid=file_uuid,
        )
        return self._get_content_oapg(
            path_params=args.path,
        )

