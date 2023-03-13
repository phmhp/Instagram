from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from django.contrib.auth.hashers import make_password

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

        # password는 암호화해야하는 민감정보이기 때문에, 암호화해서 넣어야함!
        # 패스워드의 경우에는 단방향 암호화를 사용함.
        # 단방향 암호화 : 암호화 된 것을 원래의 형태로 되돌릴 수 없음(암호화하면 끝)
        # 양방향 암호화 : 암호화 이후에 다시 복호화 가능.
        User.objects.create(email=email,
                            nickname=nickname,
                            name=name,
                            password=make_password(password),
                            profile_image="default_profile.jpg")
        return Response(status=200)
class Login(APIView):
    def get(self,request):
        return render(request,"user/login.html")
    def post(self,request):
        #Todo 로그인
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        #filter에서는 쿼리셋을 리턴하기때문에, 결과가 하나든 여러개든 리스트 형태로 반환을 하게 됨.
        # 이 때, first()를 함으로써 여러개가 아니라 하나만 리턴할 수 있는 것. (만약 두개있으면 첫번째 것만 리턴) => 이렇게 함으로써 user객체에 바로 접근이 가능. (ex- user.email이나 user.password형태로 사용 가능.)
        user=User.objects.filter(email=email).first()

        #만약 해당 email에 대한 회원이 없다면
        if user is None:
            return Response(status=400, data=dict(message="회원정보가 잘못됐습니다."))

        #check_password(password)를 해서 만약 맞으면 True, 틀리면 False를 반환할 것.
        if user.check_password(password):
            #TODO 로그인이 성공했다면-> 세션 or 쿠키에 넣는다.
            return Response(status=200)
        else: #로그인에 실패했다면
            return Response(status=400, data=dict(message="회원정보가 잘못됐습니다."))
