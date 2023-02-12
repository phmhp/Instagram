"""Instagram_coding URL Configuration

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
from django.contrib import admin
from django.urls import path
from .veiws import Sub

urlpatterns = [
     path('admin/', admin.site.urls), #http://127.0.0.1:8000/andmin/ 일 경우 admin.site.urls가 실행된다는 뜻!
     path("main/",Sub.as_view()) #http://127.0.0.1:8000/ 일때 뭘 실행시킬 것이냐? => views.py가 실행되도록 Sub.as_view() => #Sub클래스를 view로 사용하겠다는 뜻

]
