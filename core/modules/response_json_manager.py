from core.utils.common_actions import CommonActions


class ResponseJsonManager:

    @staticmethod
    def is_json_list_contains(json_list, json):
        if json in json_list:
            return True
        else:
            return False

    @staticmethod
    def is_json_contains(json_to_compare, json_to_search):
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
        CommonActions.sort_json_by_key(json_response)
        CommonActions.sort_json_by_key(json_expected)
        if json_response == json_expected:
            return True
        elif type(json_expected) and type(json_response) is not dict:
            return False

    @staticmethod
    def extract_item(json_obj):
        if type(json_obj) is not dict:
            if type(json_obj) is list:
                if len(json_obj) != 0:
                    return json_obj[0]
                else:
                    return json_obj
        return json_obj

# if __name__ == "__main__":
#     is_equal = ResponseJsonManager.is_json_list_contains([{"4": "2"}, {"1": "2"}, {"5": "1", "6": "2"}],
#                                                          {"6": "2", "5": "1"})
#     print(is_equal)
#
#     is_equal = ResponseJsonManager.is_json_contains({"1": "1", "2": "2", "3": "3"}, {"1": "1", "2": "2"})
#     print(is_equal)
#
#     is_equal = ResponseJsonManager.is_json_equal_to({"1": "1", "2": "2"}, {"2": "2", "1": "1"})
#     print(is_equal)
