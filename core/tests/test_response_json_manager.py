import unittest

from core.modules.response_json_manager import ResponseJsonManager


class TestResponseJsonManager(unittest.TestCase):
    """
    Test to ResponseJsonManager class.
    """

    def setUp(self):
        self.response_manager = ResponseJsonManager

    def test_is_json_equal_to(self):
        json_response = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}
        json_expected = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertTrue(self.response_manager.is_json_equal_to(json_expected, json_response),
                        "expected json is not equal to response json")

    def test_is_json_equal_when_data_is_not_sorted(self):
        json_response = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}
        json_expected = {'version': '1.0.504', 'name': 'server', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertTrue(self.response_manager.is_json_equal_to(json_expected, json_response),
                        "expected json is not equal to response json")

    def test_is_json_not_equal_to(self):
        json_response = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}
        json_expected = {'name': 'server1', 'version': '1', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertFalse(self.response_manager.is_json_equal_to(json_expected, json_response),
                         "expected json is equal to response json")

    def test_is_json_not_equal_when_data_is_not_sorted(self):
        json_response = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}
        json_expected = {'version': '1', 'name': 'server1', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertFalse(self.response_manager.is_json_equal_to(json_expected, json_response),
                         "expected json is equal to response json")

    def test_is_json_contains(self):
        json_response = {'version': '1.0.504'}
        json_expected = {'name': 'server', 'version': '1.0.504', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertTrue(self.response_manager.is_json_contains(json_expected, json_response),
                        "expected json is not on response json")

    def test_is_json_contains_when_data_is_not_sorted(self):
        json_response = {'version': '1.0.504'}
        json_expected = {'version': '1.0.504', 'name': 'server', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertTrue(self.response_manager.is_json_contains(json_expected, json_response),
                        "expected json is not on response json")

    def test_is_json_not_contains(self):
        json_response = {'version': '1.0.504'}
        json_expected = {'name': 'server1', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertFalse(self.response_manager.is_json_contains(json_expected, json_response),
                         "expected json is on response json")

    def test_is_json_not_contains_when_data_is_not_sorted(self):
        json_response = {'name': 'server'}
        json_expected = {'version': '1', 'description': 'Room Manager', 'license': 'MIT'}

        self.assertFalse(self.response_manager.is_json_contains(json_expected, json_response),
                         "expected json is on response json")

    def test_is_json_list_contains(self):
        json_to_find = {'version': '1.0.504'}
        json_list = [{'name': 'server'}, {'version': '1.0.504'}, {'description': 'Room Manager', 'license': 'MIT'}]

        self.assertTrue(self.response_manager.is_json_list_contains(json_list, json_to_find),
                        "json is not on response json list")

    def test_is_json_list_contains_when_data_is_not_sorted(self):
        json_to_find = {'version': '1.0.504'}
        json_list = [{'version': '1.0.504'}, {'name': 'server'}, {'description': 'Room Manager', 'license': 'MIT'}]

        self.assertTrue(self.response_manager.is_json_list_contains(json_list, json_to_find),
                        "json is not on response json list")

    def test_is_json_list_not_contains(self):
        json_to_find = {'version': '2'}
        json_list = [{'version': '1.0.504'}, {'name': 'server'}, {'description': 'Room Manager', 'license': 'MIT'}]

        self.assertFalse(self.response_manager.is_json_list_contains(json_list, json_to_find),
                         "json is on response json list")

    def test_is_json_list_not_contains_when_data_is_not_sorted(self):
        json_to_find = {'version': '2'}
        json_list = [{'description': 'Room Manager'}, {'version': '1.0.504'}, {'name': 'server'}, {'license': 'MIT'}]

        self.assertFalse(self.response_manager.is_json_list_contains(json_list, json_to_find),
                         "json is on response json list")
