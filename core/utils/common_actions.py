import base64
import json
import os
import random
import string
from pathlib import Path


class CommonActions:

    @staticmethod
    def encode_base64(string_to_encode):
        """
        This method encode a String to Base64.
        @:param string_to_encode: String.
        @:return String encode with base64.
        """
        result = str(base64.b64encode(bytes(string_to_encode, "utf-8")))
        return result[2:len(result) - 1]

    @staticmethod
    def sort_json_by_key(json_to_sort):
        """
        This method is to sort a json.
        @:param json_schema: json to sort.
        @:return json sorted.
        """
        json_to_sort = CommonActions.sort_inside_json_collection(json_to_sort)
        return json.dumps(json_to_sort, sort_keys=True)

    @staticmethod
    def sort_inside_json_collection(json_to_sort):
        """
        This method is to sort a json inside other json.
        @:param json_schema: json to sort.
        @:return json sorted.
        """

        for key in json_to_sort:
            if type(json_to_sort[key]) is list:
                json_to_sort[key] = sorted(json_to_sort[key])

        return json_to_sort

    @staticmethod
    def parameter_validator(context, param):
        """
        Method to validate parameter sent in the feature.
        :param context: is the context param.
        :param param: is the parameter received from the feature.
        :return: the parameter validated.
        """
        if param[0] == '_' and param[1] == '_':
            return context.accounts[param]
        return param

    @staticmethod
    def get_random_key():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))

    @staticmethod
    def convert_array_to_json(insert_array):
        """
        This method is to convert an array to json.
        @:param insert_array: array to json.
        @:return json.
        """
        result = {}
        for doc in insert_array:
            print(doc)
            result.update(doc)
        return result

    @staticmethod
    def convert_json_to_array(insert_json):
        """
        This method is to convert a json to array.
        @:param insert_json: json to array.
        @:return array.
        """
        result = []
        for doc in insert_json:
            result.append(doc)
        return result

    @staticmethod
    def get_json_sample(schema_name):
        """
        This method is to get a scheme.
        @:param schema_name: schema name.
        @:return schema on json format.
        """
        schema_path = "{}{}test{}samples{}{}.json".format(str(Path().absolute()),
                                                          os.path.sep,
                                                          os.path.sep,
                                                          os.path.sep,
                                                          schema_name
                                                          )

        return json.loads(open(schema_path).read())
