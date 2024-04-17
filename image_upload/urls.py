from django.urls import path
from . import views
# from .views import bakery_view

app_name = 'image_upload'

urlpatterns = [
    path('', views.image_search, name='image_search'),
    # path('upload', views.image_upload, name='image_upload'),
    # path('search/', bakery_view, name='bakery_view'),
]
