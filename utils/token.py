from rest_framework_simplejwt.authentication import JWTAuthentication
def get_user_from_token(request):
    jwt_authentication = JWTAuthentication()
    user, _ = jwt_authentication.authenticate(request)
    return user