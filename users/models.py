from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True)


class Admin(models.Model):
    image = models.ImageField(upload_to='admin_image', blank=True)