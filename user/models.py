from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.
class User(AbstractBaseUser):
    """

    유저 프로필 사진
    유저 닉네임 => 화면에 표기되는 이름
    유저 이름 => 실제 사용자 이름
    유저 이메일주소 => 회원가입할 때 사용하는 아이디
    유저 비밀번호 => 디폴트
    """
    #TextField는 길이제한이 없지만
    #CharField는 길이제한을 걸어줘야함
    profile_image = models.TextField() #프로필 이미지
    nickname = models.CharField(max_length=24,unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)

    #실제로 유저를 선택하면 그 유저의 이름을 어떤 필드로 선택해쓸 것인지?
    USERNAME_FIELD = 'email'
    class Meta: #테임을 이름을 지정할 수 있는 클래스 (기본은 앱이름_클래스이름)
        db_table = "User"

