# coding: utf-8
"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

import typing
import inspect
from datetime import date, datetime
from 1_password_connect_python_sdk.client_custom import ClientCustom
from 1_password_connect_python_sdk.configuration import Configuration
from 1_password_connect_python_sdk.api_client import ApiClient
from 1_password_connect_python_sdk.type_util import copy_signature
from 1_password_connect_python_sdk.apis.tags.activity_api import ActivityApi
from 1_password_connect_python_sdk.apis.tags.files_api import FilesApi
from 1_password_connect_python_sdk.apis.tags.health_api import HealthApi
from 1_password_connect_python_sdk.apis.tags.items_api import ItemsApi
from 1_password_connect_python_sdk.apis.tags.metrics_api import MetricsApi
from 1_password_connect_python_sdk.apis.tags.vaults_api import VaultsApi



class OnePasswordConnect(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.activity: ActivityApi = ActivityApi(api_client)
        self.files: FilesApi = FilesApi(api_client)
        self.health: HealthApi = HealthApi(api_client)
        self.items: ItemsApi = ItemsApi(api_client)
        self.metrics: MetricsApi = MetricsApi(api_client)
        self.vaults: VaultsApi = VaultsApi(api_client)
