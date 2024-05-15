from django.urls import path
from django.contrib.auth.views import LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,TokenVerifyView
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    # path("login/"),
    path('test/',views.auth_test),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenRefreshView.as_view(), name='token_verify'),
]