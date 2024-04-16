from django.db import models
from django.contrib.auth.models import AbstractUser
import django.utils.timezone
# 장고에서 만든 유저에 상속 받아 덮어씌우기
# 장고에도 기본적으로 유저가 있다. auth 밑에
# 우리는 커스텀할거라 기존 user 테이블이랑 충돌할 수 있어서 db 삭제하고 진행

class User(AbstractUser):
    birthday = models.DateField(blank=True, null=True)
    GENDER_CHOICES = (
        ('남성', "남성"),
        ('여성', "여성"),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)

