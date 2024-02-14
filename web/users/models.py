from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField("생년월일")
    profile_image = models.ImageField("프로필 이미지", upload_to=None, blank=True)