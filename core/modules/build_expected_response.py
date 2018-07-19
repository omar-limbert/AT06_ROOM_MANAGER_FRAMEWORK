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
                        res_dict_build[str(key_response)] = json_response[key_response]
                    elif key_response not in res_dict_build:
                        res_dict_build[str(key_response)] = json_response[key_response]
            return res_dict_build

        except KeyError:
            print("Build expected response: Key error")
