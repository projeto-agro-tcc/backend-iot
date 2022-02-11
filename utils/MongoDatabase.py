from pymongo import MongoClient
from backend_iot.settings_prod import URI_MONGO, DB_NAME


def get_db_handle():
    client = MongoClient(URI_MONGO)
    db_handle = client[DB_NAME]
    return db_handle, client


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
