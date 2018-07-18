from bson.objectid import ObjectId
from core.utils.singleton_db_connection import MongoDBSingleton


class DataBaseManager:

    def mongo_db(self, name_db, field, field_value):
        """mongo_db is a method to select a single record from database.
        `name_db` is the name of the database.
        `field` is the field to filter records.
        `field_value` is the value to match."""
        self.connection = MongoDBSingleton()
        data_base = self.connection.get_connection()
        collections = data_base[name_db]
        result = collections.find_one({field: ObjectId(field_value)})
        return result

    def update_mongo(self, name_db, fields_values, where_field, where_value):
        """update_mongo_db is a method to update a single record from database.
        `name_db` is the name of the database.
        `field` is the field to update records.
        `field_value` is the value to update in the field.
        `where_value` is the value to filter"""

        self.connection = MongoDBSingleton()
        db = self.connection.get_connection()
        collections = db[name_db]
        result = collections.update_one({where_field: ObjectId(where_value)}, {"$set": fields_values})
        return result

