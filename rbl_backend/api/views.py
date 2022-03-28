import io
from api.models import UsersModel
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from api.serializers import UserSerializer
from api.utils import (
    set_http_response,
    send_dataset_to_db,
    import_dataset_from_db
) 
from api.constants import INSERT_DATASET_ERROR, FETCH_DATASET_ERROR
import logging

# Create your views here.
@api_view(['POST'])
def insert_dataset(request):
    try:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            try:
                dataset = request.FILES.get("dataset")
                if not dataset:
                    res = {
                        "msg":"Dataset file is required"
                    }
                    return set_http_response(error=res)

                collection_name = serializer.validated_data["username"]

                no_of_rows = send_dataset_to_db(dataset, collection_name)

                logging.info("Inserted the dataset with %s rows.", no_of_rows)

                serializer.save()
                res = {
                    "msg":"Data Saved Successfully"
                }

                logging.info("Data Saved Successfully")

                return set_http_response(data=res)

            except Exception as ex:
                logging.error("Error in saving the dataset. Exception: %s", str(ex))
                raise ex
                
        else:
            logging.info("Error in saving Dataset. Error: ", serializer.errors)
            return set_http_response(error=serializer.errors)

    except Exception as ex:
        logging.error("Error in inserting User Records. Exception: %s", str(ex))

        res = {
            "msg" : INSERT_DATASET_ERROR
        }

        return set_http_response(error=res)

@api_view(['POST'])
def describe_dataset(request):
    try:
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            dataset = import_dataset_from_db(serializer.data['username'])
            describe = dataset.describe()
            print(describe)
            res = {
            "msg": "Describe Functionality Implemented Successfully",
            "describe": describe.to_json()
            }
            logging.info("Describe Functionality Implemented Successfully")

            return set_http_response(data=res)

        else:
            logging.error("Error in showing dataset describe. Error: %s", serializer.errors)
            return set_http_response(error=serializer.errors)
        
    except Exception as ex:

        logging.error("Error in fetching the dataset. Exception: %s", str(ex))

        res = {
            "msg" : FETCH_DATASET_ERROR
        }

        return set_http_response(error=res)