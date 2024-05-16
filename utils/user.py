from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from myuser.models import CustomUser
from django.core.exceptions import ObjectDoesNotExist


def get_user_from_token(request) -> CustomUser:
    jwt_authentication = JWTAuthentication()
    user, _ = jwt_authentication.authenticate(request)
    return user


def find_user_by_username(username) -> CustomUser:
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        return user
    except ObjectDoesNotExist:
        return None
