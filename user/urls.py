from Instagram.settings import MEDIA_URL, MEDIA_ROOT
from django.urls import path
from .views import Join,Login,Logout
urlpatterns = [
    path('join', Join.as_view()),
    path('login', Login.as_view()),
    path('logout', Logout.as_view())

]
