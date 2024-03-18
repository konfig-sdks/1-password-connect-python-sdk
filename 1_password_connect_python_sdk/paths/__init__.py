# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 1_password_connect_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    ACTIVITY = "/activity"
    VAULTS = "/vaults"
    VAULTS_VAULT_UUID = "/vaults/{vaultUuid}"
    VAULTS_VAULT_UUID_ITEMS = "/vaults/{vaultUuid}/items"
    VAULTS_VAULT_UUID_ITEMS_ITEM_UUID = "/vaults/{vaultUuid}/items/{itemUuid}"
    VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES = "/vaults/{vaultUuid}/items/{itemUuid}/files"
    VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES_FILE_UUID = "/vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}"
    VAULTS_VAULT_UUID_ITEMS_ITEM_UUID_FILES_FILE_UUID_CONTENT = "/vaults/{vaultUuid}/items/{itemUuid}/files/{fileUuid}/content"
    HEARTBEAT = "/heartbeat"
    HEALTH = "/health"
    METRICS = "/metrics"
