from core.utils.singleton_db_connection import SingletonMongoClient


class DataBaseManager:

    @staticmethod
    def get_items():
        get_connection = SingletonMongoClient().get_connection()
        data_base = get_connection["rmserver"]
        return data_base

    @staticmethod
    def remove_docs_from_collection_db(host, port, data_base_name, collection):
        get_connection = SingletonMongoClient.get_connection(host)
        client = get_connection(host, port)
        data_base = client[data_base_name]
        data_base[collection].delete_many({})


if __name__ == "__main__":
    is_equal = DataBaseManager.get_items()
    print(is_equal)

