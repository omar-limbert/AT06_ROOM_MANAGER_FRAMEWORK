import os
from pathlib import Path

import yaml

from core.utils.common_actions import CommonActions


class DataSettingsManager:

    @staticmethod
    def get_data_of_room_manager(file_data_name):
        """
        This method is to get data of setting file in a dictionary.
        @:param file_data_name: This is a name of file to read on settings folder.
        @:return dictionary with all data.
        """
        file_data_path = "{}{}test{}settings{}{}.yml".format(str(Path().absolute()),
                                                             os.path.sep,
                                                             os.path.sep,
                                                             os.path.sep,
                                                             file_data_name)
        file_data = yaml.load(open(file_data_path))
        file_data["__ADMINISTRATOR_CREDENTIALS"] = DataSettingsManager.get_credentials(file_data["__DOMAIN"],
                                                                                       file_data["__ADMINISTRATOR_ACC"],
                                                                                       file_data["__ADMINISTRATOR_PWD"])

        file_data["__USER_CREDENTIALS"] = DataSettingsManager.get_credentials(file_data["__DOMAIN"],
                                                                              file_data["__USER_ACC"],
                                                                              file_data["__USER_PWD"])
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
        return CommonActions.encode_base64("{}\{}:{}".format(domain[0:len(domain) - 4],
                                                             user,
                                                             password))


if __name__ == "__main__":
    print(DataSettingsManager.get_data_of_room_manager("data"))
