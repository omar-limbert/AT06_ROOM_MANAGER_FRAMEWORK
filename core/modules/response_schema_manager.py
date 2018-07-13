import json
import os
from pathlib import Path

from cerberus import Validator, SchemaError


class ResponseSchemaManager:

    @staticmethod
    def is_valid_schema(json_schema_response, schema_name):
        json_schema_expected = ResponseSchemaManager.get_schema(schema_name)
        schema_validator = Validator(json_schema_expected)
        try:
            return schema_validator.validate(json_schema_response)
        except SchemaError:
            return False

    @staticmethod
    def get_schema(schema_name):
        schema_path = "{}{}test{}schemes{}{}.json".format(str(Path().absolute().parent.parent),
                                                          os.path.sep,
                                                          os.path.sep,
                                                          os.path.sep,
                                                          schema_name)

        print("ON => " + schema_path)

        return json.loads(open(schema_path).read())

# if __name__ == "__main__":
#     schema = requests.get(url='http://10.37.129.3:7070/api/v1/info').json()
#     response = ResponseSchemaManager.is_valid_schema(schema, "server")
#     print(ResponseSchemaManager.get_schema("server"))
#     print(response)
