from django.urls import path
from django.contrib.auth.views import LoginView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView, TokenVerifyView
)

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.user_register),
    path('verification/', views.user_verification),
    path('authlevel/', views.user_auth_level),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenRefreshView.as_view(), name='token_verify'),
]
