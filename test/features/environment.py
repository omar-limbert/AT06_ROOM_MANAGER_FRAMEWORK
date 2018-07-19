# -*- coding: utf-8 -*-
import json
import os

import yaml

from core.modules.data_settings_manager import DataSettingsManager
from core.modules.request_manager import RequestManager
from core.utils.common_actions import CommonActions
from core.utils.singleton_logger import SingletonLogger

global generic_data
logger_agent = SingletonLogger().get_logger()
current_file_path = os.path.dirname(os.path.abspath(__file__))
generic_data = CommonActions.get_config_file_path("config", "yml")


def before_all(context):
    """
    This method is to initialize all context variables before tests.
    """
    context.request = RequestManager()
    context.item_id = ""
    context.accounts = DataSettingsManager.get_data_of_room_manager("data")
    print(context.accounts["__ADMINISTRATOR_CREDENTIALS"])


def before_scenario(context, scenario):
    context.request.set_initial_values()
    context.request.set_base_url(context.base_url)

    if "create_meeting" in scenario.tags:
        headers = {"Credentials": context.accounts["__ADMINISTRATOR_CREDENTIALS"],
                   "ServiceName": "ExchangeServer"}
        create_feature_request(context, "meetings", headers)

    if "create_equipment" in scenario.tags:
        headers = {"Credentials": context.accounts["__ADMINISTRATOR_CREDENTIALS"],
                   "ServiceName": "ExchangeServer"}
        create_feature_request(context, "equipments", headers)

    if "create_service" in scenario.tags:
        headers = {"Credentials": context.accounts["__ADMINISTRATOR_CREDENTIALS"]}
        create_feature_request(context, "services", headers)


def before_feature(context, feature):
    if "room_manager_server" in feature.tags:
        set_to_room_manager_server(context)
    if "exchange_server" in feature.tags:
        set_to_exchange_manager_server(context)


def after_scenario(context, scenario):
    if "delete_meeting" in scenario.tags:
        headers = {"Credentials": context.accounts["__ADMINISTRATOR_CREDENTIALS"],
                   "ServiceName": "ExchangeServer"}
        delete_feature_request(context, headers)
    if "delete_equipment" in scenario.tags:
        headers = {"Credentials": context.accounts["__ADMINISTRATOR_CREDENTIALS"]}
        delete_feature_request(context, headers)
    if "delete_service" in scenario.tags:
        headers = {"Credentials": context.accounts["__ADMINISTRATOR_CREDENTIALS"]}
        delete_feature_request(context, headers)


def set_to_room_manager_server(context):
    context.server_host = generic_data['room_manager_server']['host']
    context.server_port = generic_data['room_manager_server']['port']
    context.server_protocol = generic_data['room_manager_server']['protocol']
    context.server_path = generic_data['room_manager_server']['path']
    context.server_version = generic_data['room_manager_server']['version']
    set_base_url(context)


def set_to_exchange_manager_server(context):
    context.server_host = generic_data['exchange_manager_server']['host']
    context.server_port = generic_data['exchange_manager_server']['port']
    context.server_protocol = generic_data['exchange_manager_server']['protocol']
    context.server_path = generic_data['exchange_manager_server']['path']
    context.server_version = generic_data['exchange_manager_server']['version']
    set_base_url(context)


def set_base_url(context):
    context.base_url = '{}://{}:{}/{}/{}'.format(context.server_protocol,
                                                 context.server_host,
                                                 context.server_port,
                                                 context.server_path,
                                                 context.server_version)


def create_feature_request(context, feature, headers=None):
    if headers is None:
        headers = {}

    json_sample = CommonActions.get_json_sample(feature)
    context.request.set_body(
        DataSettingsManager.fill_json_with_data_on_settings(str(json_sample).replace("'", "\"")))
    context.request.set_headers(headers)
    context.response = context.request.execute_request("POST",
                                                       "/{}".format(feature))
    print(context.response.json())
    context.item_id = context.response.json()["_id"]


def delete_feature_request(context, headers=None):
    if headers is None:
        headers = {}
    context.request.set_item_id(context.item_id)
    context.request.set_headers(headers)
    print(context.item_id, headers, context.end_point)
    context.response = context.request.execute_request("DELETE",
                                                       context.end_point)
    print(context.response.status_code)
