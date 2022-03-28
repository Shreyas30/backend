from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
import pandas as pd
from pymongo import MongoClient
import json
import os
import environ

env = environ.Env()
environ.Env.read_env()

def set_http_response(data=None, error=None, content_type = "application/json"):
    if error:
        success = False
    else:
        success = True
    res = {
        "data": data,
        "success": success,
        "error":error
    }
    return Response(res)

def set_json_response(data=None, error=None):
    if error:
        success = False
    else:
        success = True
    res = {
        "data": data,
        "success": success,
        "error":error
    }

    return JsonResponse(res, safe=False)

def send_dataset_to_db(csv_path, coll_name):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: count of the documants in the new collection
    """
    db_url = env('DATABASE_URL')
    db_name = env('DATASET_DB_NAME')

    client = MongoClient(db_url)
    db = client[db_name]
    coll = db[coll_name]

    data = pd.read_csv(csv_path)
    payload = json.loads(data.to_json(orient='records'))
    coll.remove()
    coll.insert(payload)

    return coll.count()

def import_dataset_from_db(coll_name):
    db_url = env('DATABASE_URL')
    db_name = env('DATASET_DB_NAME')

    client = MongoClient(db_url)
    db = client[db_name]
    coll = db[coll_name]

    # make an API call to the MongoDB server
    mongo_docs = coll.find()

    # Convert the mongo docs to a DataFrame
    docs = pd.DataFrame(mongo_docs)
    # Discard the Mongo ID for the documents
    docs.pop("_id")

    return docs