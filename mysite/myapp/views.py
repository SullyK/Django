from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login as auth_login, logout
from rest_framework.views import APIView
from . models import *
from . serializers import *
from django.db import connection

class average(APIView):
    def get(self,request):
        mock_professor_id = 'j'
        mock_module_code = 'aaa'
        teacher = Professor.objects.raw("SELECT * FROM myapp_professor WHERE initals = %s",[mock_professor_id])
        module= Module.objects.raw("SELECT * FROM myapp_module WHERE code = %s",[mock_module_code])       
        teacher_id = 0
        module_id = 0
        average_math = 0
        total_rows = 0

        for x in teacher:
            teacher_id = x.id

        for x in module:
            module_id = x.id
            print(f"Mod returned id: {module_id}")
            rating = Rating.objects.raw("SELECT * FROM myapp_rating WHERE module_id = %s AND teachers_id = %s",[module_id,teacher_id])
            print(f"rows = {len(rating)}")
            total_rows += len(rating)
            for i in rating:
                average_math += i.rating


        
        
        average_math /= len(rating)
        average_math = round(average_math)
        print(average_math)
        return Response("average pageee")

class rating(APIView):
    def get(self,request): #TODO: change this to a post request with working data
        #we need to first retrieve, rating, if it doesn't exist make it
        #to do this we need to get the module id since it's rated for that module using the details and WHERE
        #then we need to make an average
        #finally put that data in
        mock_professor_id = 'j'
        mock_module_code = 'aaa'
        mock_year = '2020' 
        mock_semester = '1'
        mock_rating = '4'
        mock_rating = float(mock_rating)
        
        # This shoudl convert it to the a float. If it's an integer, we will rewrite it as a string
        if(mock_rating.is_integer()):
            print(f'do nothing: {mock_rating}')
            mock_rating = str(mock_rating)
        # else:
        #     if(mock_rating )
        
        teacher = Professor.objects.raw("SELECT * FROM myapp_professor WHERE initals = %s",[mock_professor_id])
        module= Module.objects.raw("SELECT * FROM myapp_module WHERE code = %s AND year = %s AND semester = %s",[mock_module_code,mock_year,mock_semester])        
        
        teacher_id = 0
        module_id = 0
        for x in teacher:
            teacher_id = x.id
            print(f"teacher_id = {x.id}")
        
        for x in module:
            module_id = x.id
            print((f"module_id = {x.id}"))
        

        # so now we got the module and professor name id
        # we need to query the db in rating and check if they exist.


        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO myapp_rating(rating, module_id, teachers_id) VALUES (%s, %s, %s)", [mock_rating,module_id,teacher_id]
                )
        
        # # get the avg of these
        # data = Rating.objects.raw("SELECT * FROM myapp_rating WHERE module_id = %s AND teachers_id = %s", [module_id,teacher_id])
        # print(f"rows returned: {len(data)}")


        
        return Response("sdfsdfsdfsd")


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
    
