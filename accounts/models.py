from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    biografy = models.TextField()
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    # переопределение функции с целью изменения размера поступаемых пользовательских изображений
    def save(self, *args, **qwargs):
        super().save(*args, **qwargs)

        image = Image.open(self.avatar.path)

        if image.height > 100 or image.width > 100:
            image.thumbnail((100, 100))
            image.save(self.avatar.path)
