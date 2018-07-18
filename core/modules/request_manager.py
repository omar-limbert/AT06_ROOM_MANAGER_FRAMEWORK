import requests


# Class that performs API requests.
class RequestManager:

    def __init__(self, headers, params, body):
        self.headers = headers
        self.params = params
        self.body = body

    def set_headers(self, headers):
        self.headers = headers

    def set_params(self, params):
        self.params = params

    def set_body(self, body):
        self.body = body

    @staticmethod
    def build_url(base_url, endpoint, item_id):
        if item_id is not None:
            return "{}/{}/{}".format(base_url, endpoint, item_id)
        else:
            return "{}/{}".format(base_url, endpoint)

    def execute_request(self, method, base_url, endpoint, item_id):
        '''
            Performs an API request.
            @:param method: The method.
            @:param base_url: The base URL.
            @:param endpoint: The endpoint.
            @:param item_id: Id of the item for perform the request.
            '''
        uri = RequestManager.build_url(base_url, endpoint, item_id)
        if self.headers is not None:
            if method == 'DELETE':
                return requests.delete(uri, headers=self.headers)
            elif self.params is not None:
                if method == 'GET':
                    return requests.get(uri, headers=self.headers, params=self.params)
            elif self.body is not None:
                if method == 'POST' or method == 'PUT':
                    return requests.request(method, uri, headers=self.headers, json=self.body)
        else:
            if method == 'GET':
                return requests.get(uri)
            elif method == 'POST':
                return requests.post(uri, json=self.body)
