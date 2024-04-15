from django.contrib import admin
from .models import User
# Register your models here.

# admin에 만든 유저 등록
admin.site.register(User)

