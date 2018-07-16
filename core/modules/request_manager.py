import requests


# Class that performs API requests.
class RequestManager:
    '''
    Builds an url for performing an API request.
    @:param base_url: The base url for append the endpoint.
    @:param endpoint: The endpoint.
    @:param item_id: Id of the element.
    '''

    @staticmethod
    def build_url(base_url, endpoint, item_id=''):
        return "{}/{}/{}".format(base_url, endpoint, item_id)

    '''
    Performs an API request.
    @:param method: The method.
    @:param url: The comlete URL.
    @:param headers: Dictionary of HTTP Headers to send.
    @:param params: Dictionary or bytes to be sent in the query string.
    @:param body: A JSON serializable Python object to send in the body of the request.
    '''

    @staticmethod
    def execute_request(method, url, headers={},
                        params={}, body={}):
        return requests.request(method, url, headers=headers, params=params, json=body).json()
