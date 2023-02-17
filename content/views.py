from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
import os

class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all() #select * from content_feed;와 동일한 역할을 함. #.models.py에서 정의한 Feed의 객체들을 모두 feed_list라는 리스트에 넣어줌
        print(feed_list)

        return render(request, "Instagram/main.html")