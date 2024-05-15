from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
# Create your models here.
class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = [
        ('charter', 'Charter'),
        ('judge', 'Judge'),
        ('host', 'Host'),
        ('admin', 'Administrator'),
    ]
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=20, choices=USER_ROLE_CHOICES, default='charter')
    date_joined = models.DateTimeField(auto_now_add=True,editable=False)
    bio = models.TextField(blank=True, null=True)
    email_verification=models.BooleanField(default=False)
    admin_verification=models.BooleanField(default=False)
    def __str__(self):
        return self.username
    
# class EmailVerifyString(models.Model):
#     code = models.CharField(max_length=256)
#     user = models.OneToOneField('User', on_delete=models.CASCADE)
#     c_time = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.user.name + ":   " + self.code

#     class Meta:
#         ordering = ["-c_time"]
#         verbose_name = "email_verify_code"