from bson.objectid import ObjectId
from core.utils.singleton_db_connection import SingletonMongoClient


class DataBaseManager:

    @staticmethod
    def get_all_items(post_id):
        client = SingletonMongoClient().get_connection()
        data_base = client["rmserver"]
        if data_base is not None:
            result = client["rmserver"].collection.find_one({'_id': ObjectId(post_id)})
        else:
            result = client["rmserver"].collection.find_one({'_id'})
        return result

    @staticmethod
    def remove_docs_from_collection_db(host, port, data_base_name, collection):
        get_connection = SingletonMongoClient.get_connection(host)
        client = get_connection(host, port)
        data_base = client[data_base_name]
        data_base[collection].delete_many({})


if __name__ == "__main__":
    is_equal = DataBaseManager.get_all_items('478521365985478542693652')
    print(is_equal)

