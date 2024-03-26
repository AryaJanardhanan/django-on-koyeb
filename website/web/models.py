from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, default=0)
    last_name = models.CharField(max_length=100, default=0)
    username = models.CharField(max_length=100, default=0)
    email = models.EmailField(default=0)

    def __str__(self):
        return self.user.username


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Image(models.Model):
    image = models.ImageField(upload_to='gallery/')

