from bson import json_util, ObjectId

from core.utils.singleton_db_connection import MongoDBSingleton
from bson.json_util import dumps


class ResponseDBManager:

    def __init__(self):
        self.connection = MongoDBSingleton()

    def get_json_from_database_all_data(self, collections_name):
        """get_json_from_database_all is a method to select a single record from database.
        `collections_name` is the name of the database."""
        data_base = self.connection.get_connection()
        collections = data_base[collections_name]
        response_database = collections.find({})
        response_in_json_format = dumps(response_database)
        # print('xxxxxxxxxxxxxxx', response_in_json_format)
        return response_in_json_format

    def get_json_from_database(self, collections_name, field_name, id_to_search):
        """get_json_from_database is a method to select a single record from database.
        `collections_name` is the name of the database.
        `field_name` is the field to filter records.
        `id_to_search` is the value to match."""
        data_base = self.connection.get_connection()
        collections = data_base[collections_name]
        # print('xxxxxxxxxxxxxxx',collections)
        result = collections.find_one({field_name: ObjectId(id_to_search)})
        result_json = json_util.dumps(result)
        return result_json

    def compare_response_db_with_get_json(self, collections_name, field_name, id_to_search):
        """compare_response_db_with_get_json is a method to compare the data from database
        with data get_json_from_database.
        `collections_name` is the name of the database.
        `field_name` is the field to filter records.
        `id_to_search` is the value to match.
        @return a verified Get."""
        response = ResponseDBManager.get_json_from_database(self, collections_name, field_name, id_to_search)
        # print('response of get_json_from_database:', response)
        data_base = self.connection.get_connection()
        collections = data_base[collections_name]
        result = collections.find_one({field_name: ObjectId(id_to_search)})
        result_json = json_util.dumps(result)
        # print('response of compare connect to database:', result_json)
        if response == result_json:
            return response
        else:
            return None

    def update_json_from_database(self, collections_name, fields_name, id_field_to_update, new_json_data):
        """update_json_from_database is a method to update a single record from database.
        `collections_name` is the name of the database.
        `fields_name` is the field to update records.
        `id_field_to_update` is the value to update in the field.
        `new_json_data` is the value to filter"""
        db = self.connection.get_connection()
        collections = db[collections_name]
        result = collections.update_one({id_field_to_update: ObjectId(new_json_data)}, {"$set": fields_name})
        return result


'''test with database exchangeservicedb'''

'''test for return all data (Get) 1st class'''
# conn2 = ResponseDBManager()
# test = conn2.get_json_from_database_all_data('subscriptions')
# print(test)
'''test for return data by id (Get) 2nd class'''
# conn = ResponseDBManager()
# test = conn.get_json_from_database('meetings','_id','5b3ab8889dd441bdf8c9f48e')
# print(test)
'''test for compare the data of the second class with a new get with data base (Get) 3th class'''
# conn3 = ResponseDBManager()
# test3 = conn3.compare_response_db_with_get_json('meetings', '_id', '5b3ab8889dd441bdf8c9f48e')
# print(test3)

'''test with database rmserver'''

'''test for return all data (Get) 1st class'''
# conn2 = ResponseDBManager()
# test = conn2.get_json_from_database_all_data('priorities')
# print(test)
'''test for return data by id (Get) 2nd class'''
# conn = ResponseDBManager()
# test = conn.get_json_from_database('meetings','_id','5b3cd48dc643bd8685e59851')
# print(test)
'''test for compare the data of the second class with a new get with data base (Get) 3th class'''
# conn3 = ResponseDBManager()
# test3 = conn3.compare_response_db_with_get_json('meetings', '_id', '5b3cd48dc643bd8685e59851')
# print(test3)
