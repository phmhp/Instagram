from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
import os

class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all() #select * from content_feed;와 동일한 역할을 함. #.models.py에서 정의한 Feed의 객체들을 모두 feed_list라는 리스트에 넣어줌
        for feed in feed_list :
            #print(feed.content)
            #print(feed_list) #얘가 실행되기 위해서는 Instagram 폴더의 urls.py에서 설정을 해줘야함.


        #render (request, template_name, context=None)
            return render(request, "Instagram/main.html",context=dict(feeds=feed_list)) #딕셔너리 형태로 제공! (원래는 json형태로 줘야하는데, 딕셔너리도 json과 호환이 가능해서 일단은 딕셔너리 형태로 해볼것)
