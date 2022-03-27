from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

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