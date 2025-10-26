from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User
from django.shortcuts import reverse


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(
        upload_to=f'images/accounts/',
        validators=[FileExtensionValidator(('png', 'jpg', 'jpeg',), 'Не разрешенный формат')]
    )

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def get_absolute_url(self):
        return reverse('profile_detail', args=[self.pk])
