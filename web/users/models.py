from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    birthday = models.DateField("생년월일", null=True)
    profile_image = models.ImageField("프로필 이미지", upload_to="users/profile", blank=True, null=True)
    like_restaurants = models.ManyToManyField(
        "single_pages.Restraunt", # single_pages라는 앱에있는 Restraunt 모델과 사용자가 관계를 맺는다는 뜻
        verbose_name = "좋아요 누른 Restaurant 목록",
        related_name="like_users", # 역방향일때 이름을 정해줌. 좋아요를누른 유저들을 부를 이름
        blank=True,
    )