import json
import os
from pathlib import Path

from cerberus import Validator, SchemaError


class ResponseSchemaManager:

    @staticmethod
    def is_valid_schema(json_schema_response, schema_folder, schema_name):
        """
        This method is to verify if a schema is valid.
        @:param json_schema_response: schema file to verify
        @:param schema_name: schema name on schemes folder.
        @:param True if json_schema_response is valid, False is not valid.
        """
        json_schema_expected = ResponseSchemaManager.get_schema(schema_folder, schema_name)
        schema_validator = Validator(json_schema_expected)
        try:
            return schema_validator.validate(json_schema_response)
        except SchemaError:

            return False

    @staticmethod
    def get_schema(schema_folder, schema_name):
        """
        This method is to get a scheme.
        @:param schema_name: schema name.
        @:return schema on json format.
        """
        schema_path = "{}{}test{}schemes{}{}{}{}.json".format(str(Path().absolute()),
                                                              os.path.sep,
                                                              os.path.sep,
                                                              os.path.sep,
                                                              schema_folder,
                                                              os.path.sep,
                                                              schema_name
                                                              )

        return json.loads(open(schema_path).read())
