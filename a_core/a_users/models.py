from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='avatars/',
        null=True,
        blank=True
    )
    displayname = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    info = models.TextField(
        null=True,
        blank=True
    )