from rest_framework.status import *
from django.http import JsonResponse


def my_json_response(code, info, data=None):
    if data:
        body = {'code': code, 'info': info, **data}
    else:
        body = {'code': code, 'info': info}

    return JsonResponse(status=code, data=body)
