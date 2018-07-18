# -*- coding: utf-8 -*-
import os

import yaml

from core.modules.data_settings_manager import DataSettingsManager
from core.utils.singleton_logger import SingletonLogger

global generic_data
logger_agent = SingletonLogger().get_logger()
current_file_path = os.path.dirname(os.path.abspath(__file__))
config_path = str(os.path.dirname(current_file_path) + os.path.sep + 'settings' + os.path.sep + 'config.yml')
generic_data = yaml.load(open(config_path))


def before_all(context):
    """
    This method is to initialize all context variables before tests.
    """
    context.accounts = DataSettingsManager.get_data_of_room_manager("data")
    context.headers = {}
    context.body = {}


def before_scenario(context, scenario):
    if "create_meeting" in scenario.tags:
        print("I will create a meeting")


def before_feature(context, feature):
    if "room_manager_server" in feature.tags:
        logger_agent.info("Executing with Room Manager Server")
        set_to_room_manager_server(context)
    if "exchange_server" in feature.tags:
        logger_agent.info("Executing with Room Manager Server")
        set_to_exchange_manager_server(context)


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
