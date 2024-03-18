import typing_extensions

from 1_password_connect_python_sdk.apis.tags import TagValues
from 1_password_connect_python_sdk.apis.tags.items_api import ItemsApi
from 1_password_connect_python_sdk.apis.tags.files_api import FilesApi
from 1_password_connect_python_sdk.apis.tags.vaults_api import VaultsApi
from 1_password_connect_python_sdk.apis.tags.health_api import HealthApi
from 1_password_connect_python_sdk.apis.tags.activity_api import ActivityApi
from 1_password_connect_python_sdk.apis.tags.metrics_api import MetricsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ITEMS: ItemsApi,
        TagValues.FILES: FilesApi,
        TagValues.VAULTS: VaultsApi,
        TagValues.HEALTH: HealthApi,
        TagValues.ACTIVITY: ActivityApi,
        TagValues.METRICS: MetricsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ITEMS: ItemsApi,
        TagValues.FILES: FilesApi,
        TagValues.VAULTS: VaultsApi,
        TagValues.HEALTH: HealthApi,
        TagValues.ACTIVITY: ActivityApi,
        TagValues.METRICS: MetricsApi,
    }
)
