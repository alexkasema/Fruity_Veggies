from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#! After creating this go to settings.py and add AUTH_USER_MODEL
class User(AbstractUser):
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)

    #! we need to install pillow for this to work
    avatar = models.ImageField(null=True, default="avatar.jpg")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
