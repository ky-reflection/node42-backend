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
    
    def __str__(self):
        return self.username