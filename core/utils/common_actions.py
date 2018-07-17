import base64
import json
import random
import string


class CommonActions:

    @staticmethod
    def encode_base64(string_to_encode):
        """
        This method encode a String to Base64.
        @:param string_to_encode: String.
        @:return String encode with base64.
        """
        result = str(base64.b64encode(bytes(string_to_encode, "utf-8")))
        return result[2:len(result)-1]

    @staticmethod
    def sort_json_by_key(json_schema):
        """
        This method is to sort a json.
        @:param json_schema: json to sort.
        @:return json sorted.
        """
        json_schema = CommonActions.sort_inside_json_collection(json_schema)
        return json.dumps(json_schema, sort_keys=True)

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
    def get_random_key():
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))