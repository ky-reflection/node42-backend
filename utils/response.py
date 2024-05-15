from rest_framework.status import *
from django.http import JsonResponse

def json_response_withdata(code,info,data):
    body={'code':code,'info':info,'data':data}
    return JsonResponse(status=code,data=body)

def json_response_nodata(code,info):
    body={'code':code,'info':info}
    return JsonResponse(status=code,data=body)