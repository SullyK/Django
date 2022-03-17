from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login as auth_login, logout
from rest_framework.views import APIView
from . models import *
from . serializers import *

# class view(APIView):
#     def get(self,request):
#         staff = Professors.objects.all().values('id').values_list('id',flat=True)  # get list of all staff IDs
#         list = []
#         for mod_professor in staff: # for each memember of staff
#             data = Ratings.objects.filter(Professor=mod_professor) # find the ratings in the ratings table that apply to that member of staff
#             if not data: # if they have no ratings do nothing
#                 print("none")
#             else: # if they have ratings
#                 all_ratings = 0
#                 rating_count = 0
#                 for rating in data: # for each rating they have 
#                     all_ratings += rating['rating'] # add the ratings to variable (need to convert to int)
#                     rating_count = rating_count+1 # increase ratings count
#                 average = all_ratings/rating_count # calculate their average rating
#                 final_data = (mod_professor['name']+average)  # store the professors name and average rating
#                 list.append(final_data) # add proffessors name and average rating to list
#         serializer = RatingsSerializer(staff, many=True) # serialize list (may need to make new serializer class for this)

#         return Response(serializer.data) # return response

class test(APIView):
    def get(self,request):
        # staff = Professor.objects.all()
        data = [] 
        for p in Professor.objects.raw('SELECT * FROM myapp_professor'):
            print(p.id)
            data.append(p)
        
     # get list of all staff IDs
        # print(staff)
        # list = []

        serializer = ProfessorSerializer(data, many=True)
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
    
