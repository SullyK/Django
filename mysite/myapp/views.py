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
        mock_prof_id = 'j' #id for professor
        mock_mod_id = 'comp'
        pro_id = Professor.objects.raw('SELECT id FROM myapp_professor WHERE initals = %s',[mock_prof_id])
        pro_name = 0
        mod_id = Module.objects.raw('SELECT id FROM myapp_module WHERE code = %s',[mock_mod_id])
        mod_name = 0 
        mod_code = 0
        pro_test = 0
        mod_test = 0
        pro_initals = 0
        for x in pro_id:
            pro_test = x.id
            pro_name = x.name
            pro_initals = x.initals
        for x in mod_id:
            mod_test = x.id
            mod_name = x.name
            mod_code =x.code
        


        # print(p.id)
        # for x in p.id:
        print(f"professor id: {pro_test}")
        print(f"module id: {mod_test}")

        returned = Rating.objects.raw('SELECT * FROM myapp_rating WHERE module_id = %s AND teachers_id = %s', [mod_test,pro_test] )
        for x in returned:
            print(x.rating)
            reponse = {f"The rating of {pro_name} ({pro_initals}) in module {mod_name} ({mod_code}) is {pro_test}"}
        # for x in returned:
        #     print(x)
        # for x in returned:
        #     if(mock_prof_id == x.teachers.initals and mock_module == x.module.id):
        #         print(f'{x.teachers.initals} teaching {x.module.id} a has rating of {x.rating}')
        # if len((returned)) > 1:
        #     print("error: too many returned results from query...")
        # elif(len((returned) < 1)):
        #     print("error: You need at least 1 returned result from the DB")
        # probably should do try and assert exception handling 
        # print(returned)

            # for rating in returned:
            #     print(rating.module.name)
            #     print(rating.teachers.name)
            #     print(rating.rating)
            #     print('---------------------')
            
            
        
     # get list of all staff IDs
        # print(staff)
        # list = []

        # serializer = ProfessorSerializer(data, many=True)
        return Response(reponse)


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
    
