from core.utils.common_actions import CommonActions


class ResponseJsonManager:

    @staticmethod
    def is_json_list_contains(json_list, json):
        """
        This method is to find a json inside one json list.
        @:param json_list: Json list to eval.
        @:param json: Json to find on list before.
        @:param True if json exist on list, False is not exist on list.
        """
        if json in json_list:
            return True
        else:
            return False

    @staticmethod
    def is_json_contains(json_to_compare, json_to_search):
        """
        This method is to verify if a json data is on other json.
        @:param json_to_compare: Json to find.
        @:param json_to_search: Json to eval.
        @:param True if json_to_search data is on json_to_compare, False is not on json_to_compare.
        """
        CommonActions.sort_json_by_key(json_to_search)
        CommonActions.sort_json_by_key(json_to_compare)
        try:
            for key in json_to_search:
                if not (str(json_to_search[key]) in str(json_to_compare[key]) or str(json_to_compare[key]) in str(
                        json_to_search[key])):
                    print(str(json_to_compare[key]) + "is not equal to" + str(json_to_search[key]))
                    return False
            return True
        except KeyError:
            return False

    @staticmethod
    def is_json_equal_to(json_response, json_expected):
        """
        This method is to verify is a one json is equal to other json.
        @:param json_response: Json to compare.
        @:param json_expected: Json to compare.
        @:param True if json_response is equal to json_expected, False is not equal to json_expected.
        """
        CommonActions.sort_json_by_key(json_response)
        CommonActions.sort_json_by_key(json_expected)
        if json_response == json_expected:
            return True
        elif type(json_expected) and type(json_response) is not dict:
            return False
        else:
            return False
