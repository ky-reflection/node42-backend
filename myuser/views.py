from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
import json
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from utils.token import get_user_from_token
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def auth_test(request):
    jwt_authentication = JWTAuthentication()
    user=get_user_from_token(request)
    if user:
        # Get user information
        username = user.username
        email = user.role
        # Add more user information as needed
        return Response({"username": username, "email": email})
    else:
        return Response({"error": "Invalid token"})

