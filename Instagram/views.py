from django.shortcuts import render
from rest_framework.views import APIView

''' 실습하던 코드
class Sub(APIView):
    def get(self,request):
        print("get으로 호출")
        return render(request,"Instagram/main.html")

    def post(self, request):
        print("post로 호출")
        return render(request, "Instagram/main.html")
        
'''
