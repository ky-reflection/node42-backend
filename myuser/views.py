from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
import rest_framework.status as http_status
import django.http.response as http_responce
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,JsonResponse
from .models import CustomUser
from utils.response import json_response_nodata,json_response_withdata
from utils.user import get_user_from_token,enable_admin_auth_role_list,find_user_by_username

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['POST'])
def user_register(request):
    try:
        username=request.data['username']
        password=request.data['password']
        if CustomUser.objects.filter(username=username).exists():
            return json_response_nodata(http_status.HTTP_400_BAD_REQUEST,"User existed.")
        if len(password)<6: #要求六位密码
            return json_response_nodata(http_status.HTTP_400_BAD_REQUEST,"Bad parameter.")
        _user = CustomUser.objects.create_user(username=username,password=password)
    except:
        return json_response_nodata(http_status.HTTP_400_BAD_REQUEST,"Bad parameter.")
    return json_response_nodata(http_status.HTTP_200_OK,f"User {username} registered.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_verification(request):
    operator=get_user_from_token(request)
    if operator.role in enable_admin_auth_role_list:
        try:
            username=request.data['username']
            user=find_user_by_username(username)
            if user:
                user.admin_verification=True
                user.save()
                return json_response_nodata(http_status.HTTP_200_OK,f'User {username} verified.')
            else:
                return json_response_nodata(http_status.HTTP_404_NOT_FOUND,f"User {username} not found.")
        except:
            return json_response_nodata(http_status.HTTP_400_BAD_REQUEST,"Bad parameter.")
    else:
        return json_response_nodata(http_status.HTTP_403_FORBIDDEN,"Foridden.")
