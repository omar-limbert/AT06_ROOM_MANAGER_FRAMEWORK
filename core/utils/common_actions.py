import base64
import json


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
        return json.dumps(json_schema, sort_keys=True)

    @staticmethod
    def sort_json_collection_by_key(json_schema):
        """
        This method is to sort a json inside other json.
        @:param json_schema: json to sort.
        @:return json sorted.
        """
        for key in json_schema:
            json.dumps(json_schema[key], sort_keys=True)
        return json_schema

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
