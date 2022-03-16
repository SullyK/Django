from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login as auth_login, logout
from .views import APIView
from . models import *
from . serializers import *


class test(APIView):
    def get(self,request):
        data = Module.objects.all()
        serializer = ModuleSerializer(data, many=True)
        return Response(serializer.data)


class login(APIView):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password,backend='django.contrib.auth.backends.ModelBackend')
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
            print (request.user.id)
            response = f"You are {request.user}"
        else:
            response = "you aren't logged in"
        return Response(response)

class logout_user(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            response = f"you are trying to logout,{request.user}"
            logout(request)
            response += " + logged you out, succesfully"
        else:
            response = "you werent logged in."
        return Response(response)
        