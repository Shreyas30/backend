import io
from api.models import Datasets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from api.serializers import DatasetSerializer
from api.utils import set_http_response
from api.constants import INSERT_DATASET_ERROR, FETCH_DATASET_ERROR
import logging


# Create your views here.
@api_view(['POST'])
def insert_dataset(request):
    try:
        serializer = DatasetSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()

            res = {
                "msg":"Data Saved Successfully"
            }

            logging.info("Data Saved Successfully")

            return set_http_response(data=res)
        else:
            return set_http_response(error=serializer.errors)

    except Exception as ex:
        logging.error("Error in saving the dataset. Exception: %s", str(ex))

        res = {
            "msg" : INSERT_DATASET_ERROR
        }

        return set_http_response(error=res)


@api_view(['GET'])
def get_all_dataset(request):
    try:
        datasets = Datasets.objects.all()

        serializer = DatasetSerializer(datasets, many = True)
        
        logging.info("Data Fetched Successfully")
        return set_http_response(data=serializer.data)

    except Exception as ex:

        logging.error("Error in fetching the dataset. Exception: %s", str(ex))

        res = {
            "msg" : FETCH_DATASET_ERROR
        }

        return set_http_response(error=res)