# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from 1_password_connect_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ITEMS = "Items"
    FILES = "Files"
    VAULTS = "Vaults"
    HEALTH = "Health"
    ACTIVITY = "Activity"
    METRICS = "Metrics"
