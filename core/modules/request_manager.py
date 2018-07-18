import requests


# Class that performs API requests.
class RequestManager:

    def __init__(self):
        self.headers = {}
        self.parameters = {}
        self.body = {}
        self.item_id = ""
        self.base_url = ""

    def set_headers(self, headers):
        self.headers = headers

    def set_parameters(self, parameters):
        self.parameters = parameters

    def set_body(self, body):
        self.body = body

    def set_item_id(self, item_id):
        self.item_id = item_id

    def set_base_url(self, base_url):
        self.base_url = base_url

    def get_body(self):
        return self.body

    def get_headers(self):
        return self.headers

    def get_parameters(self):
        return self.parameters

    def get_item_id(self):
        return self.item_id

    def get_base_url(self):
        return self.base_url

    def build_url(self, endpoint):
        if len(self.item_id) != 0:
            return "{}{}/{}".format(self.base_url, endpoint, self.item_id)
        else:
            return "{}{}".format(self.base_url, endpoint)

    def execute_request(self, method, endpoint):
        '''
            Performs an API request.
            @:param method: The method.
            @:param base_url: The base URL.
            @:param endpoint: The endpoint.
            @:param item_id: Id of the item for perform the request.
            '''
        uri = RequestManager.build_url(self, endpoint)
        print(uri,self.item_id)
        if len(self.headers):
            if method == 'DELETE':
                print("delete?")
                print(uri)
                return requests.delete(uri, headers=self.headers)
            elif len(self.parameters):
                if method == 'GET':
                    return requests.get(uri, headers=self.headers, params=self.parameters)
            elif len(self.body):
                if method == 'POST' or method == 'PUT':
                    return requests.request(method, uri, headers=self.headers, json=self.body)
        else:
            if method == 'GET':
                return requests.get(uri)
            elif method == 'POST':
                return requests.post(uri, json=self.body)
