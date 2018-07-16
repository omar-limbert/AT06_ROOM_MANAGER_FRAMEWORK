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

    logger_agent.info("Execute Before all")
    context.room_manager_host = generic_data['room_manager']['host']
    context.room_manager_port = generic_data['room_manager']['port']

    context.protocol = generic_data['root_path']['protocol']
    context.path = generic_data['root_path']['path']
    context.version = generic_data['root_path']['version']

    context.base_url = '{}://{}:{}/{}/{}'.format(context.protocol,
                                                 context.room_manager_host,
                                                 context.room_manager_port,
                                                 context.path,
                                                 context.version)

    context.accounts = DataSettingsManager.get_data_of_room_manager("data")

    print(context.accounts)
