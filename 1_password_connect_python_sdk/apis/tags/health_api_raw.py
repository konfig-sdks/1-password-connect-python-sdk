# coding: utf-8

"""
    1Password Connect

    REST API interface for 1Password Connect.

    The version of the OpenAPI document: 1.5.7
    Contact: support@1password.com
    Created by: https://support.1password.com/
"""

from 1_password_connect_python_sdk.paths.heartbeat.get import CheckLivenessRaw
from 1_password_connect_python_sdk.paths.health.get import ServerStateCheckRaw


class HealthApiRaw(
    CheckLivenessRaw,
    ServerStateCheckRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass