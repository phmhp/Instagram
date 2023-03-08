from django.shortcuts import render
from rest_framework.views import APIView
from models import User

# Create your views here.
class Join(APIView):
    def get(self,request):
        return render(request,"user/join.html")
    def post(self,request):
        #Todo 회원가입
        email = request.data.get('email',None)
        nickname = request.data.get('nickname',None)
        name = request.data.get('name',None)
        password = request.data.get('password',None)

        User.objects.create(email=email, nickname=nickname,name=name,password=password)
        #password는 암호화해야하는 민감정보이기 때문에, 암호화해서 넣어야함!
        #패스워드의 경우에는 단방향 암호화를 사용함.
        #단방향 암호화 : 암호화 된 것을 원래의 형태로 되돌릴 수 없음(암호화하면 끝)
        #양방향 암호화 : 암호화 이후에 다시 복호화 가능.
class Login(APIView):
    def get(self,request):
        return render(request,"user/login.html")
    def post(self,request):
        #Todo 로그인
        pass