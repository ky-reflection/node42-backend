from rest_framework_simplejwt.authentication import JWTAuthentication
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
enable_admin_auth_role_list=['judge','host','admin']

def get_user_from_token(request):
    jwt_authentication = JWTAuthentication()
    user, _ = jwt_authentication.authenticate(request)
    return user

def find_user_by_username(username):
    User = get_user_model()
    try:
        user = User.objects.get(username=username)
        return user
    except ObjectDoesNotExist:
        return None