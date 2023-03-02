from Instagram.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import path
from .views import UploadFeed
urlpatterns = [
    path('upload', UploadFeed.as_view())
]
