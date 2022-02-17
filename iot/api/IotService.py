from utils.MongoDatabase import get_db_handle, get_collection_handle

from bson.json_util import dumps


class IotService:

    def __init__(self):
        pass

    def getDataByParams(self, time_to_start, time_to_end, dev_id, colection):
        db_handle, mongo_client = get_db_handle()
        collection = get_collection_handle(db_handle, colection)
        serialized_obj = dumps(list(collection.find({'dev_id': dev_id,
                                                     'time': {'$lt': int(time_to_end), '$gt': int(time_to_start)}})))
        return serialized_obj
