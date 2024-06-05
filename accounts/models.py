from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid
from django.conf import settings

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('accountant', 'Accountant'),
        ('manager', 'Manager'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='admin')


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, unique=True)
    updated_time_stamp = models.DateTimeField(auto_now=True)
    created_time_stamp = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    # display user with full name in the database
    def __str__(self):
        return self.username
    
