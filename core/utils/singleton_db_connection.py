from pymongo import MongoClient


class DBManager(type):
    """Singleton that keep only one value for all instances"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(DBManager, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonMongoClient(object, metaclass=DBManager):
    """ Class based on Singleton type to work with MongoDB connections"""
    def __init__(self):
        """ This method is to initialize logger.
            """
        self._connection = MongoClient('localhost', 27017)

    def get_connection(self):
        """This method is to get connection.
            @:return _connection.
            """
        return self._connection
