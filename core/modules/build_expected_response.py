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
                    if key_response == "body" and json_response[key_expected].__contains__(json_request[key_expected]):
                        res_dict_build[str(key_response)] = json_response[key_expected]
                    elif key_response not in res_dict_build:
                        res_dict_build[str(key_response)] = json_response[key_response]
            print(res_dict_build)
            return res_dict_build
        except KeyError:
            print("Build expected response: Key error")

    @staticmethod
    def response_get_vs_post(response_get_parameter, response_post_parameter):
        """
        Function that is going print the values that are not equal.

        :param response_get_parameter: is the response after doing GET request
        :param response_post_parameter: is the response after doing POST request
        :return: whether the json are equals or not.
        """
        if type(response_get_parameter) and type(response_post_parameter) is not dict:
            return None
        result = True
        for key in response_get_parameter:
            if key in response_post_parameter:
                if response_get_parameter[key] != response_post_parameter[key]:
                    print(
                        "JSON_request: {} >>> request_value({}) not equals to JSON_response: {} >>> response_value({})".
                            format(key, response_get_parameter[key], key, response_post_parameter[key]))
                    result = False
        return result
