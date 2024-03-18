import typing_extensions

from 1_password_connect_python_sdk.paths import PathValues
from 1_password_connect_python_sdk.apis.paths.activity import Activity
from 1_password_connect_python_sdk.apis.paths.vaults import Vaults
from 1_password_connect_python_sdk.apis.paths.vaults_vault_uuid import VaultsVaultUuid
from 1_password_connect_python_sdk.apis.paths.vaults_vault_uuid_items import VaultsVaultUuidItems
from 1_password_connect_python_sdk.apis.paths.vaults_vault_uuid_items_item_uuid import VaultsVaultUuidItemsItemUuid
from 1_password_connect_python_sdk.apis.paths.vaults_vault_uuid_items_item_uuid_files import VaultsVaultUuidItemsItemUuidFiles
from 1_password_connect_python_sdk.apis.paths.vaults_vault_uuid_items_item_uuid_files_file_uuid import VaultsVaultUuidItemsItemUuidFilesFileUuid
from 1_password_connect_python_sdk.apis.paths.vaults_vault_uuid_items_item_uuid_files_file_uuid_content import VaultsVaultUuidItemsItemUuidFilesFileUuidContent
from 1_password_connect_python_sdk.apis.paths.heartbeat import Heartbeat
from 1_password_connect_python_sdk.apis.paths.health import Health
from 1_password_connect_python_sdk.apis.paths.metrics import Metrics

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ACTIVITY: Activity,
        PathValues.VAULTS: Vaults,
        PathValues.VAULTS_VAULT_UUID: VaultsVaultUuid,
        PathValues.VAULTS_VAULT_UUID_ITEMS: VaultsVaultUuidItems,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID: VaultsVaultUuidItemsItemUuid,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES: VaultsVaultUuidItemsItemUuidFiles,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES_FILE_UUID: VaultsVaultUuidItemsItemUuidFilesFileUuid,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES_FILE_UUID_CONTENT: VaultsVaultUuidItemsItemUuidFilesFileUuidContent,
        PathValues.HEARTBEAT: Heartbeat,
        PathValues.HEALTH: Health,
        PathValues.METRICS: Metrics,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ACTIVITY: Activity,
        PathValues.VAULTS: Vaults,
        PathValues.VAULTS_VAULT_UUID: VaultsVaultUuid,
        PathValues.VAULTS_VAULT_UUID_ITEMS: VaultsVaultUuidItems,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID: VaultsVaultUuidItemsItemUuid,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES: VaultsVaultUuidItemsItemUuidFiles,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES_FILE_UUID: VaultsVaultUuidItemsItemUuidFilesFileUuid,
        PathValues.VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES_FILE_UUID_CONTENT: VaultsVaultUuidItemsItemUuidFilesFileUuidContent,
        PathValues.HEARTBEAT: Heartbeat,
        PathValues.HEALTH: Health,
        PathValues.METRICS: Metrics,
    }
)
