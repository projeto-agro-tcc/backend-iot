from backend_iot.enviroments import RECEIVED_DATADB
from utils.MongoDatabase import get_collection_handle, get_db_handle


class CatchDataFromReceivedData:

    def get_data(self):
        db_handle, mongo_client = get_db_handle()
        collection = get_collection_handle(db_handle, RECEIVED_DATADB)
        documents = list(collection.find())
        if documents:
            for doc in documents:
                for data in doc['data']:
                    collection_data = get_collection_handle(db_handle, data['ref'])
                    if len(self.it_exist(collection_data, data)) == 0:
                        self.save_data(collection_data, data)
                collection.delete_one(doc)
        else:
            print("No data")

    def save_data(self, collection, data):
        obj = {
            'time': data['time'],
            'unit': data['unit'],
            'value': data['value'],
            'dev_id': data['dev_id']
        }
        collection.insert_one(obj)

    def it_exist(self, collection, data):
        obj = data.copy()
        obj.pop('ref')
        list_obj = list(collection.find(obj).limit(1))
        return list_obj
