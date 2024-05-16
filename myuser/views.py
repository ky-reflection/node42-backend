from rest_framework.decorators import api_view
import rest_framework.status as http_status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from .models import CustomUser
from utils.response import my_json_response
from utils.user import get_user_from_token, find_user_by_username
from utils.node42_config import NODE42_AUTH_LEVEL, is_valid_auth_level


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['POST'])
def user_register(request):
    try:
        username = request.data['username']
        password = request.data['password']
        if CustomUser.objects.filter(username=username).exists():
            return my_json_response(http_status.HTTP_400_BAD_REQUEST, "User existed.")
        if len(password) < 6:  # 要求六位密码
            return my_json_response(http_status.HTTP_400_BAD_REQUEST, "Bad parameter.")
        _user = CustomUser.objects.create_user(
            username=username, password=password)
    except:
        return my_json_response(http_status.HTTP_400_BAD_REQUEST, "Bad parameter.")
    return my_json_response(http_status.HTTP_200_OK, f"User {username} registered.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_verification(request):
    operator = get_user_from_token(request)
    if operator.node42_auth_level >= NODE42_AUTH_LEVEL.ADMIN:
        try:
            username = request.data['username']
            user = find_user_by_username(username)
            if user:
                user.admin_verification = True
                user.save()
                return my_json_response(http_status.HTTP_200_OK, f'User {username} verified.')
            else:
                return my_json_response(http_status.HTTP_404_NOT_FOUND, f"User {username} not found.")
        except:
            return my_json_response(http_status.HTTP_400_BAD_REQUEST, "Bad parameter.")
    else:
        return my_json_response(http_status.HTTP_403_FORBIDDEN, "Foridden.")


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def user_auth_level(request):
    operator: CustomUser = get_user_from_token(request)
    operator_auth = operator.node42_auth_level
    if operator_auth >= NODE42_AUTH_LEVEL.HOST:
        try:
            username = request.data['username']
            auth_level = request.data['auth_level']
            if is_valid_auth_level(auth_level):
                user: CustomUser = find_user_by_username(username)
                if user:
                    target_auth = user.node42_auth_level
                    if user.username == operator.username:
                        return my_json_response(http_status.HTTP_400_BAD_REQUEST, f"A mi nuo si.")
                    if target_auth >= operator_auth or auth_level >= operator_auth:
                        return my_json_response(http_status.HTTP_403_FORBIDDEN, "Foridden.")
                    user.admin_verification = True
                    user.save()
                    return my_json_response(http_status.HTTP_200_OK, f'Set {username} level {auth_level}.')
                else:
                    return my_json_response(http_status.HTTP_404_NOT_FOUND, f"User {username} not found.")
            else:
                return my_json_response(http_status.HTTP_400_BAD_REQUEST, f"Auth {auth_level} not found.")
        except:
            return my_json_response(http_status.HTTP_400_BAD_REQUEST, "Bad parameter.")
    else:
        return my_json_response(http_status.HTTP_403_FORBIDDEN, "Foridden.")
