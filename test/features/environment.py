# -*- coding: utf-8 -*-
import os

import yaml

global generic_data

current_file_path = os.path.dirname(os.path.abspath(__file__))
config_path = str(os.path.dirname(current_file_path) + os.path.sep + 'settings' + os.path.sep + 'config.yml')
generic_data = yaml.load(open(config_path))


def before_all(context):
    """
    This method is to initialize all context variables before tests.
    """
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
