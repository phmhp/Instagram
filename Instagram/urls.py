"""Instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import sys

from Instagram.settings import MEDIA_URL, MEDIA_ROOT

sys.path.append(r'C:\toyProject\CreateInstagram\Instagram\Instagram')
from django.contrib import admin
from django.urls import path,include
from content.views import Main,UploadFeed    #다른 폴더의 소스를 참조하는 거라서 . 이 필요
urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/',Main.as_view()), #이렇게 하면 content.views.py에 있는 Main클래스가 실행이 될 것. (이후 동작에 대한 설명은 Main클래스에 메모해놓음)
    path('content/',include('content.urls')),
    path('user/',include('user.urls'))

]
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT) #media 폴더의 파일들을 조회할 수 있도록 해주는 부분임. (=이 부분이 없으면 파일조회가 불가능하다고 함)