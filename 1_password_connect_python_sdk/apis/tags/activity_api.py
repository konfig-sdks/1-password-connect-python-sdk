# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

from 1_password_connect_python_sdk.paths.activity.get import GetApiRequests
from 1_password_connect_python_sdk.apis.tags.activity_api_raw import ActivityApiRaw


class ActivityApi(
    GetApiRequests,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ActivityApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ActivityApiRaw(api_client)