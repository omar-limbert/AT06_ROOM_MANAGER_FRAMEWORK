from pymongo import MongoClient


class MongoDBSingleton(object):
    '''Connection to mongodb in singleton'''

    __instance = None
    __client = None
    __db = None

    def __new__(cls, *args, **kwargs):
        if MongoDBSingleton.__instance is None:
            MongoDBSingleton.__instance = object.__new__(cls)
        return MongoDBSingleton.__instance

    def __init__(self):
        if MongoDBSingleton.__client is None:
            MongoDBSingleton.__client = MongoClient('mongodb://10.28.136.135:27017')
            MongoDBSingleton.__db = MongoDBSingleton.__client['rmserver']
            # MongoDBSingleton.__db = MongoDBSingleton.__client['exchangeservicedb']

    def get_connection(self):
        return MongoDBSingleton.__db
