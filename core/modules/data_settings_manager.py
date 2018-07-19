import json
import os
from pathlib import Path

import yaml

from core.utils.common_actions import CommonActions


class DataSettingsManager:

    @staticmethod
    def fill_json_list_with_data_on_settings(json_list):
        result = []
        for json in json_list:
            json = str(json).replace("'", "\"")
            result.append(DataSettingsManager.fill_json_with_data_on_settings(json))
        return result

    @staticmethod
    def fill_json_with_data_on_settings(json_to_fill):
        """
        This method is to get data of setting file in a dictionary.
        @:param file_data_name: This is a name of file to read on settings folder.
        @:return dictionary with all data.
        """
        json_to_fill = json.loads(json_to_fill)
        data_on_settings = DataSettingsManager.get_data_of_room_manager("data")
        for key in json_to_fill:

            key_to_find = str(json_to_fill[key])

            if type(json_to_fill[key]) is list:
                json_to_fill[key] = DataSettingsManager.fill_list_with_data_on_settings(json_to_fill[key],
                                                                                        data_on_settings)

            if key_to_find in data_on_settings.keys():
                json_to_fill[key] = data_on_settings[key_to_find]
        return json_to_fill

    @staticmethod
    def fill_list_with_data_on_settings(list_to_fill, data_on_settings):
        """
        This method is to fill list with data on settings.
        @:param list_to_fill: This is a list to fill.
        @:param data_on_settings: data on settings.
        """
        result = []
        for data in list_to_fill:
            if data in data_on_settings.keys():
                result.append(data_on_settings[data])
            else:
                result.append(data)
        return result

    @staticmethod
    def get_data_of_room_manager(file_data_name):
        """
        This method is to get data of setting file in a dictionary.
        @:param file_data_name: This is a name of file to read on settings folder.
        @:return dictionary with all data.
        """
        file_data = CommonActions.get_config_file_path(file_data_name, "yml")
        file_data["__ADMINISTRATOR_CREDENTIALS"] = DataSettingsManager.get_credentials(file_data["__DOMAIN"],
                                                                                       file_data["__ADMINISTRATOR_ACC"],
                                                                                       file_data["__ADMINISTRATOR_PWD"])

        file_data["__USER1_CREDENTIALS"] = DataSettingsManager.get_credentials(file_data["__DOMAIN"],
                                                                               file_data["__USER1_ACC"],
                                                                               file_data["__USER2_PWD"])

        file_data["__USER2_CREDENTIALS"] = DataSettingsManager.get_credentials(file_data["__DOMAIN"],
                                                                               file_data["__USER2_ACC"],
                                                                               file_data["__USER2_PWD"])
        return file_data

    @staticmethod
    def get_credentials(domain, user, password):
        """
        This method is to get credentials.
        @:param domain: Domain of roommanager.
        @:param user: User to get credentials.
        @:param password: Password of user.
        @:return String credentials encode with base64.
        """
        return CommonActions.encode_base64("{}\{}:{}".format(domain,
                                                             user,
                                                             password))


if __name__ == "__main__":
    print(DataSettingsManager.get_data_of_room_manager("data"))
