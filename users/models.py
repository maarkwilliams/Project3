from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = CloudinaryField('image', blank=True, null=True)
