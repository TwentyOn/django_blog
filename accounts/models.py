from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    biografy = models.TextField()
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username