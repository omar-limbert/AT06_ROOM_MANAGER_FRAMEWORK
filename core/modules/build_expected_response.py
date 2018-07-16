def build_expected_response(json_request, json_response):
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
