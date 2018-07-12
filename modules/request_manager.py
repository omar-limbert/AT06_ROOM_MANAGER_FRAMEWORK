import requests

headers = {'Accept': 'application/json'}


# Method for build url
def build_uri(base_url, end_point):
    uri = base_url + end_point
    return uri

# Performs a request with GET method.
def get_request(base_url, end_point, credentials, param):
    uri = build_uri(base_url, end_point)
    response = requests.get(url=uri, headers=headers, params=param)
    return response

# Performs a request with POST method.
def post_request(base_url, end_point, credentials, data):
    uri = build_uri(base_url,end_point)
    response = requests.post(url=uri, headers=headers, json=data)
    return response

# Performs a request with PUT method.
def put_request(base_url, end_point, credentials, data):
    uri = build_uri(base_url, end_point)
    response = requests.put(url=uri, headers=headers, json=data)
    return response

# Performs a request with DELETE method.
def delete_request(base_url, end_point, credentials, params):
    uri = build_uri(base_url, end_point)
    response = requests.delete(url=uri, headers=headers, params=params)
    return response

# Performs a request with GET or DELETE method.
def get_delete_request(base_url, end_point, method, credentials, item_id, params):
    response = None
    uri = build_uri(base_url, end_point)
    if item_id is not None:
        headers['Credentials'] = credentials
        headers['ServiceName'] = 'ExchangeServer'
        uri = "{}/{}".format(uri, item_id)
        if method == 'GET':
            response = requests.get(url=uri, headers=headers, params=params)
        elif method == 'DELETE':
            response = requests.delete(url=uri, headers=headers, params=params)
    elif method == 'GET':
        if credentials is not None:
            headers['Credentials'] = credentials
            response = requests.get(url=uri, headers=headers, params=params)
        else:
            response = requests.get(url=uri, headers=headers, params=params)
    return response

# Performs a request with POST or PUT method.
def post_put_request(base_url, end_point, method, credentials, item_id, data):
    response = None
    uri = build_uri(base_url, end_point)
    headers['Content-Type'] = 'application/json'
    headers['Credentials'] = credentials
    if item_id is not None:
        headers['ServiceName'] = 'ExchangeServer'
        uri = "{}/{}".format(uri, item_id)
        if method == 'POST':
            response = requests.post(url=uri, headers=headers, json=data)
        elif method == 'PUT':
            response = requests.put(url=uri, headers=headers, json=data)
    elif method == 'POST':
        response = requests.post(url=uri, headers=headers, json=data)
    return response

# Executes a request.
def request(base_url, endpoint, method, credentials, item_id, data, params):
    headers['ServiceName'] = 'ExchangeServer'
    if method == 'GET':
        return get_delete_request(base_url, endpoint, method, credentials, item_id, params)
    elif method == 'POST':
        headers['Content-Type'] = 'application/json'
        headers['Credentials'] = credentials
        return post_request(base_url, endpoint, credentials, data)
    elif method == 'PUT':
        headers['Content-Type'] = 'application/json'
        return put_request(base_url, endpoint, credentials, data)
    elif method == 'DELETE':
        return delete_request(base_url, endpoint, credentials, data)



