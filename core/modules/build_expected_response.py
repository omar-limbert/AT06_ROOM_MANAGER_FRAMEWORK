from bson import ObjectId


# Class to build the expected response.
class BuildResponse:

    @staticmethod
    def build_expected_response(json_request, json_response):
        """
        Function that is going to build the expected response.

        :param json_request: is the json parameter that is sent in the request.
        :param json_response: is the json response received after doing the request.
        :return: the json built with the keys of the response and the values of the request.
        """
        try:
            res_dict_build = {}
            for key_response in json_response:
                for key_expected in json_request:
                    if key_response.__contains__(key_expected):
                        res_dict_build[str(key_response)] = json_request[key_expected]
                    elif key_response not in res_dict_build:
                        res_dict_build[str(key_response)] = json_response[key_response]
            print(res_dict_build)
            return res_dict_build
        except KeyError:
            print("Build expected response: Key error")

    @staticmethod
    def is_json_request_equal_to_json_response(json_request, json_response):
        """
        Function to compare whether two json files are equals or not;
        if not returns which ones are not equals.

        :param json_request: is the json parameter that is sent in the request.
        :param json_response: is the json response received after doing the request.
        :return: a boolean value depending whether the json data are equals or not
        """
        if type(json_request) and type(json_response) is not dict:
            return None
        result = True
        for key in json_request:
            if key in json_response:
                if type(json_request[key]) is ObjectId:
                    if str(json_request[key]) == str(json_response[key]):
                        continue
                    else:
                        result = False
                        print("JSON_request: {} >>> ObjId({}) not equals to JSON_response: {} >>> ObjId({})"
                              .format(key, json_request[key], key, json_response[key]))
                else:
                    if json_request[key] == json_response[key]:
                        # print("JSON_request: {} >>> ObjId({}) is equals to JSON_response: {} >>> ObjId({})"
                        #       .format(key, json_request[key], key, json_response[key]))
                        continue
                    else:
                        print("JSON_request: {} >>> ObjId({}) not equals to JSON_response: {} >>> ObjId({})".
                              format(key, json_request[key], key, json_response[key]))
                        result = False
        return result
