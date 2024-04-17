from django.contrib import admin
from django.urls import path, include
from . import views

app_name="user"

urlpatterns = [
    path("", views.login_view, name='login'),
    path("signup/", views.signup_view, name='signup'),

]