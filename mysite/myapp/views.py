from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login as auth_login, logout
from rest_framework.views import APIView
from . models import *
from . serializers import *
from django.db import connection
from django.contrib.auth.models import User
import json
import copy
from rest_framework import status


class register(APIView):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        check_username = User.objects.raw("SELECT * from auth_user WHERE username = %s", [username])
        check_email = User.objects.raw("SELECT * from auth_user WHERE email = %s", [email])
        #TODO: fix the email check, as it's not working apparently

        if (len(check_username) != 0):
            response = json.dumps("Error: Username already exists in database, please try again")
            return Response(response,status=status.HTTP_400_BAD_REQUEST)

        if(len(check_email) > 0): #TODO: Fix this email checking logic.
            response = json.dumps("Error: Email already exists in database, please try again")
            return Response(response,status=status.HTTP_400_BAD_REQUEST)


        # Make account as email and username doesn't exist in db
        user = User.objects.create_user(username = username, password = password, email = email)
        user.save()
        
        
        response = json.dumps("Account made succesfully")
        return Response(response)


class list(APIView):
    def get(self,request):
        a = []
        dic = {}
        counter = 0
        mod_number = 0
        returned_rows = Module.objects.all()
        print(returned_rows)
        for x in returned_rows:
            dic['code'] = (x.code)
            dic['name'] = (x.name)
            dic['year'] = (x.year)
            dic['semester'] = (x.semester)
            stored = x.teachers.all()
            for z in stored:
                dic[f'teachersname {counter}'] = z.name
                dic[f'teachersinit {counter}'] = z.initals
                counter += 1 
            a.append(copy.deepcopy(dic))
            dic.clear()
            mod_number += 1
            counter = 0
        return Response(a)

class view(APIView):
    def get(self, request):
        teachers_id = 0
        avg = 0
        teacher = Professor.objects.raw("SELECT * FROM myapp_professor")
        dic = {}
        for i in teacher: 
            teachers_id = i.id
            prof_name = i.name
            prof_init = i.initals
            rating= Rating.objects.raw("SELECT * FROM myapp_rating WHERE teachers_id = %s",[teachers_id])  
            print('--------------------')   
            for a in rating:
                avg += a.rating
            
            if(len(rating) == 0):
                continue
            avg /= len(rating)
            if(avg > 1 and avg <=1.49):
                avg = 1
            elif(avg > 1.49 and avg <= 2.0):
                avg = 2
            elif(avg > 2.0 and avg <= 2.49):
                avg = 2
            elif(avg > 2.49 and avg <= 3.0):
                avg = 3
            elif(avg > 3.0 and avg <= 3.49):
                avg = 3
            elif(avg > 3.49 and avg <= 4.0):
                avg = 4
            elif(avg > 4.0 and avg <= 4.49):
                avg = 4
            elif(avg > 4.49 and avg <= 5.0):
                avg = 5
            dic[f'{prof_name}({prof_init})'] = f"{avg}"

            print(f"rating: {avg} for prof: {prof_name}")
            avg = 0 
        # and names now
        return Response(dic)




        



class average(APIView):
    def post(self,request):
        
        mock_professor_id = request.POST.get('professor_init')
        mock_module_code = request.POST.get('module_code')
        teacher = Professor.objects.raw("SELECT * FROM myapp_professor WHERE initals = %s",[mock_professor_id])
        if len(teacher) == 0:
            response = json.dumps("That teacher doesn't exist, please try again")
            return Response(response,status = status.HTTP_400_BAD_REQUEST)
        
        module = Module.objects.raw("SELECT * FROM myapp_module WHERE code = %s",[mock_module_code])  
        if len(module) == 0:    
            response = json.dumps("That module doesn't exist, please try again")
            return Response(response,status = status.HTTP_400_BAD_REQUEST)
 
        teacher_id = 0
        module_id = 0
        average_math = 0
        total_rows = 0
        teacher_name = 0
        dic = {}
        for x in teacher:
            teacher_id = x.id
            teacher_name = x.name
            teacher_init = x.initals

        for x in module:
            module_id = x.id
            print(f"Mod returned id: {module_id}")
            rating = Rating.objects.raw("SELECT * FROM myapp_rating WHERE module_id = %s AND teachers_id = %s",[module_id,teacher_id])
            print(f"rows = {len(rating)}")
            total_rows += len(rating)
            for i in rating:
                average_math += i.rating


        
        
        average_math /= total_rows
        #TODO: add error checking here for 0 numbers so it doesn't explode
        if(average_math > 1 and average_math <=1.49):
            average_math = 1
        elif(average_math > 1.49 and average_math <= 2.0):
            average_math = 2
        elif(average_math > 2.0 and average_math <= 2.49):
            average_math = 2
        elif(average_math > 2.49 and average_math <= 3.0):
            average_math = 3
        elif(average_math > 3.0 and average_math <= 3.49):
            average_math = 3
        elif(average_math > 3.49 and average_math <= 4.0):
            average_math = 4
        elif(average_math > 4.0 and average_math <= 4.49):
            average_math = 4
        elif(average_math > 4.49 and average_math <= 5.0):
            average_math = 5

        print(average_math)
        dic[f'{teacher_name}({teacher_init})'] = average_math

        return Response(dic,status = status.HTTP_200_OK)

class rating(APIView):
    def post(self,request): #TODO: change this to a post request with working data
        #we need to first retrieve, rating, if it doesn't exist make it
        #to do this we need to get the module id since it's rated for that module using the details and WHERE
        #then we need to make an average
        #finally put that data in        mock_professor_id = request.POST.get('professor_init')
        if request.user.is_authenticated:
            mock_professor_id = request.POST.get('professor_init')
            mock_module_code = request.POST.get('mod_code')
            mock_year = request.POST.get('year')
            mock_semester = request.POST.get('sem')
            mock_rating = request.POST.get('rating')
            
            #TODO: deal with this number bs.

            if(mock_rating.isdigit()):
                x = "do nothing"
            else:             
                response = json.dumps("That rating is not a number, please try again")
                return Response(response, status=status.HTTP_400_BAD_REQUEST)

        
            mock_rating = float(mock_rating)
    # This shoudl convert it to the a float. If it's an integer, we will rewrite it as a string
            if(mock_rating.is_integer()):
                print(f'do nothing: {mock_rating}')
                mock_rating = str(mock_rating)
            # else:
            #     if(mock_rating )
            
            teacher = Professor.objects.raw("SELECT * FROM myapp_professor WHERE initals = %s",[mock_professor_id])
            if(len(teacher) == 0):
                response = json.dumps("That teacher doesn't exist, please try again")
                return Response(response,status = status.HTTP_400_BAD_REQUEST)
            module= Module.objects.raw("SELECT * FROM myapp_module WHERE code = %s AND year = %s AND semester = %s",[mock_module_code,mock_year,mock_semester])        
            if(len(module) == 0):
                response = json.dumps("Sorry, there doesn't exist a module with that code or year or rating.")
                return Response(response,status = status.HTTP_400_BAD_REQUEST)

            if(float(mock_rating) < 1.0 or float(mock_rating) > 5.0):
                response = json.dumps("Sorry, Rating has to be between 1 and 5")
                return Response(response,status = status.HTTP_400_BAD_REQUEST)

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
            
            
            response = "You have succesfully rated the teacher"

            response = json.dumps(response)
            return Response(response,status = status.HTTP_200_OK)

        else:
            response = "Please login"
            response = json.dumps(response)
            return Response(response,status = status.HTTP_400_BAD_REQUEST)



class login(APIView):
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password,backend='django.contrib.auth.backends.ModelBackend')
        if user is not None:
            auth_login(request, user)
            request.session.set_expiry(86400)
            response = "Success" 
        else: 
            response = "Fail"
            response = json.dumps(response)
            return Response(response,status = status.HTTP_400_BAD_REQUEST)
        response = json.dumps(response)
        print(type(response))
        return Response(response,status = status.HTTP_200_OK)
# test my login


class logout_user(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            response = f"you are trying to logout,{request.user}"
            logout(request)
            response += "...logged you out, succesfully"
            response = json.dumps(response)
            return Response(response,status = status.HTTP_200_OK)

        else:
            response = "you werent logged in."
            response = json.dumps(response)
            return Response(response,status = status.HTTP_400_BAD_REQUEST)

