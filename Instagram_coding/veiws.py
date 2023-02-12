from rest_sframework.views import APIView
from django.shortcuts import render

class Sub(APIView):
    def get(self,request):
        print('get으로 호출한 경우')
        return render(request,"Instagram_coding/main.html")
    def post(self,request):
        print('host으로 호출한 경우')
        return render(request,"Instagram_coding/main.html")



