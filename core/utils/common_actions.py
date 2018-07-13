import base64
import json


class CommonActions:

    @staticmethod
    def encode_base64(string_to_encode):  # In Progress
        return base64.b64encode(b"test")

    @staticmethod
    def sort_json_by_key(json_schema):
        return json.dumps(json_schema, sort_keys=True)

    @staticmethod
    def sort_json_collection_by_key(json_schema):
        for key in json_schema:
            json.dumps(json_schema[key], sort_keys=True)
        return json_schema


if __name__ == "__main__":
    print(CommonActions.sort_json_by_key({"version": "1", "name": "2"}))
    print(CommonActions.encode_base64("sdf"))
    print(CommonActions.sort_json_by_key([{"1": "1"}, {"1": "1", "3": "3", "2": "2"}]))
