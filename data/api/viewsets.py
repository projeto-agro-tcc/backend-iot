from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from utils.MongoDatabase import get_db_handle, get_collection_handle
from backend_iot.settings import RECEIVED_DATADB


class DataViewSet(ModelViewSet):

    @action(detail=False, methods=['POST'])
    def data(self, request, *args, **kwargs):
        db_handle, mongo_client = get_db_handle()
        collection = get_collection_handle(db_handle, RECEIVED_DATADB)
        collection.insert_one(request.data)
        return Response(status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['POST'])
    def connection_status(self, request, *arg, **kwargs):
        response = {
            "seq": 1,
            "status": 201,
            "message": 'It is working'
        }
        return Response(status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def signal_status(self, request, *arg, **kwargs):
        response = {
            "seq": 1,
            "status": 201,
            "message": 'It is working'
        }
        return Response(status=status.HTTP_200_OK)

