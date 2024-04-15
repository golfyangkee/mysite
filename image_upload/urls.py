from django.urls import path
from . import views

app_name = 'image_upload'

urlpatterns = [
    path('', views.image_search, name='image_search'),
    #path('upload', views.image_upload, name='image_upload'),
]