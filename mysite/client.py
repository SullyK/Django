from urllib import response
import requests
import json



while(True):

    print("Please choose one of the following options:")
    print("Enter 1 to Register")
    print("Enter 2 to Login")
    print("Enter 3 to Exit")
    mm_answer = input()
    if(mm_answer == '1'):
        print("Registering!")
        username = input("Enter Username:")
        password = input("Enter Password:")
        email = input("Enter Email:")
        payload = {'username': username, 'password': password, "email": email}
        r = requests.post("http://127.0.0.1:8000/app/register",data=payload)
        x = json.loads(r.text)
        print(x[1:-1])
        print("Taking you back to the main menu")
        print("---------------------------------")
        continue

    elif(mm_answer == '2'):
        print("Logging in!")
        sess = requests.Session()  #Create a session to store cookies.
        username = input("Enter Username:")
        password = input("Enter Password:")

        payload = {
        'username': username,
        'password': password,
    }

        r = sess.post("http://127.0.0.1:8000/app/login",data=payload)
        cookies = dict(r.cookies)
        x = json.loads(r.text)
        if x[1:-1] == "Success":
            print("Login Success! :)")
            print("Please choose one of the following options:")
            print("Enter 1 for List (list all module instances and professors)")
            print("Enter 2 to View (rating of all professors)")
            print("Enter 3 to Average (view average of a certain professor in certain module)")
            print("Enter 4 to Rate (rate a professor in certain module instance)")
            print("Enter 5 to logout)")
            print("enter 6 to exit")
            choice = input()

            if(choice == '1'):
                


        else:
            print("Login Failed. Taking you back to the main menu.")









    elif(mm_answer == '3'):
        print("Exiting the client, have a very safe day!")
        break
    #Register



    #Login

    # payload = {
    #     'username': 'sully',
    #     'password': 'left4dead2'
    # }

    # r = s.post("http://127.0.0.1:8000/app/login",data=payload)
    # cookies = dict(r.cookies)
    # x = json.loads(r.text)
    # print(x[1:-1])


    # # logout

    # r = s.get("http://127.0.0.1:8000/app/logout_user",cookies=cookies)
    # x = json.loads(r.text)
    # print(x[1:-1])

    # view

    # r = s.get("http://127.0.0.1:8000/app/view")
    # json_data = json.loads(r.text)
    # for key,value in json_data.items():
    #     stars = int(value) * '*'
    #     print(f"The rating of {key} is {stars}")

    # average for eacher

    # payload = {
    #     "professor_init" : "j.h",
    #     "module_code" : "xx1"
    # }


    # r = s.post("http://127.0.0.1:8000/app/average", data = payload)
    # json_data = json.loads(r.text)
    # for key,value in json_data.items():
    #     stars = int(value) * '*'
    #     print(f"The rating of {key} is {stars}")

    #TODO: check user is logged in for whatever needs login

    #TODO: change the payload to user input

    #rate



    # r = s.get("http://127.0.0.1:8000/app/rating")
    # json_data = json.loads(r.text)
    # print(json_data[1:-1])


    #list

    # r = requests.get("http://127.0.0.1:8000/app/list")
    # data = r.json()
    # print('{:>0}  {:>5}  {:>18} {:>12} {:>12}'.format("Code", "Name", "Year", "Semester", "Taught By"))
    # print('---------------------------------------------------------------')

    # item = 0
    # counter = 0
    # for x in data:
    #     print(f"{x['code']:5s} {x['name']:20s} {str(x['year']):10s} {str(x['semester']):10s}", end="", flush=True)

    #     while True:
    #         if f'teachersname {counter}' not in x:
    #             counter = 0
    #             item += 1
    #             print("\n---------------------------------------------------------------------------")
    #             break
    #         else:
    #             if(counter > 0 ):
    #                 print(f",",end="", flush=True)
    #             print(f"{data[item]['teachersname ' + str(counter)]:2s}", end="", flush=True)
    #             print(f"({data[item]['teachersinit ' + str(counter)]:1s})", end="", flush=True)
    #             counter += 1

