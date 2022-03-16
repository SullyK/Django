from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login as auth_login
from rest_framework.views import APIView



class login(APIView):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            request.session.set_expiry(86400)
            response = {"you are active": "brooo"}
            print(user.id)
        else: 
            response = {"uffffff": "aaaaa"}

        return Response(response)
# curl --data "user/pass" http://127.0.0.1:8000/app/ | jq
# test my login

class check_user(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            print (user.id)
        else:
            response = "you aren't logged in"
            return Response(response)
