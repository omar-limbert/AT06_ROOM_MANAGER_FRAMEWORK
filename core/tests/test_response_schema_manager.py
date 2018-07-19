import unittest

from core.modules.response_schema_manager import ResponseSchemaManager


class TestResponseSchemaManager(unittest.TestCase):
    """
    Test to ResponseSchemaManager class.
    """

    def setUp(self):
        self.response_manager = ResponseSchemaManager

    def test_is_valid_schema(self):
        response_json = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}
        self.assertTrue(self.response_manager.is_valid_schema(response_json, "server", "server"),
                        "is not valid schema")

    def test_is_not_valid_schema(self):
        response_json = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}
        self.assertFalse(self.response_manager.is_valid_schema(response_json, "meetings", "meeting"),
                         "is valid schema")
