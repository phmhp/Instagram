import os
from uuid import uuid4

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self,request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed;와 동일한 역할을 함.
                                                      # .models.py에서 정의한 Feed의 객체들을 모두 feed_list라는 리스트에 넣어줌
        return render(request, "Instagram/main.html",context=dict(feeds=feed_list)) #딕셔너리 형태로 제공! (원래는 json형태로 줘야하는데, 딕셔너리도 json과 호환이 가능해서 일단은 딕셔너리 형태로 해볼 것)
        #render(request, template_name, context=None)

class UploadFeed(APIView):
    def post(self,request):

        file = request.FILES['file']

        uuid_name = uuid4().hex #파일 이름이 한글이나 특수문자로 인해 에러가 나는 것을 방지 하기 위해 랜덤한 id값을 부여 (uuid는 파이썬의 기본적인 함수. uuid().hex하면 랜덤한 값을 줌)
        from Instagram.settings import MEDIA_ROOT
        save_path = os.path.join(MEDIA_ROOT, uuid_name) #MEDIA_ROOT은 Instagram.settings.py에서 정의함. = BASE_DIR에 media를 붙이고, 랜덤한 이름(uuid)을 쓰겠다!
                                                        # 다시 말하자면, 클라이언트에서 파일을 업로드하고자 하면 그 업로드하는 파일들은 루트프로젝트 경로의 media/에 uuid로 생성된 랜덤한 이름으로 저장이 됨 . (~/media/uuid4로 생성된 이름)
        with open(save_path, 'wb+') as destination: #실제로 파일이 저장되는 부분에 해당함. ( save_path에 파일을 열어서 청크를 하나씩 하나씩 가져와서 쓰는 부분임) = 파일을 열어서 파일을 읽어서 파일로 만들 때는 이 with 구문을 씀.
                                                    #with open(파일저장경로, .....
            for chunk in file.chunks():
                destination.write(chunk)
        #여기까지 하고나면 파일이 저장이 됨.



        file = uuid_name #랜덤한 값으로 부여된 파일 이름
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get("user_id")
        profile_image = request.data.get('profile_image')


        #피드에 저장하는 과정
        #피드에 가져올 때는 feed.objects.all()로 했었는데, 만들 때는 feed.objects.create()하면 됨.
        #create할 때는 model에 있는 모든 값을 넣어줘야함.
        Feed.objects.create(image=image, content=content, user_id=user_id , profile_image=profile_image,like_count=0) #models.py에서 정의한 Feed의 필드 이름들이 앞의 image,content ...에 해당하고 뒤에 있는 image,content..는 바로 윗 문단에서 정의한 것들이라서, 만약 윗 문단에서 다른 이름으로 변수명을 정했다면 해당 변수명을 작성해주면 됨 )
        return Response(status=200) #Response객체 = rest_framework에 response에 Response라는 함수가 존재함. 그 함수를 통해서 결과가 200인지 정보를 줌.

