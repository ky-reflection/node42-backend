from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.node42_config import NODE42_AUTH_LEVEL
import uuid
# Create your models here.


class CustomUser(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True)
    avatar = models.ImageField(
        upload_to='avatars/', blank=True, null=True, verbose_name='头像')
    node42_auth_level = models.IntegerField(
        choices=NODE42_AUTH_LEVEL.choices, default=NODE42_AUTH_LEVEL.GUEST, verbose_name='身份')
    date_joined = models.DateTimeField(auto_now_add=True, editable=False)
    bio = models.TextField(blank=True, null=True, verbose_name='简介')
    email_verification = models.BooleanField(
        default=False, verbose_name='邮箱验证')
    admin_verification = models.BooleanField(
        default=False, verbose_name='身份验证')

    def __str__(self):
        return self.username

# class PrivacySettings(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='privacy_settings')
#     phone_number_visible = models.BooleanField(default=False)
#     birth_date_visible = models.BooleanField(default=False)
#     address_visible = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.user.username}'s Privacy Settings"
