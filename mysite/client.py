from urllib import response
import requests
import json

while(True):

    print("Please choose one of the following options:")
    print("Enter register to Register")
    print("Enter login to Login")
    print("Enter exit to Exit")
    mm_answer = input()
    if(mm_answer == 'register'):
        print("Registering!")
        username = input("Enter Username:")
        password = input("Enter Password:")
        email = input("Enter Email:")
        payload = {'username': username, 'password': password, "email": email}
        r = requests.post("http://127.0.0.1:8000/api/register",data=payload)
        x = json.loads(r.text)
        print(x[1:-1])
        print("Taking you back to the main menu")
        print("---------------------------------")
        continue

    elif(mm_answer == 'login'):
        print("Logging in!")
        sess = requests.Session()  #Create a session to store cookies.
        username = input("Enter Username:")
        password = input("Enter Password:")

        payload = {
        'username': username,
        'password': password,
    }

        r = sess.post("http://127.0.0.1:8000/api/login",data=payload)
        cookies = dict(r.cookies)

        x = json.loads(r.text)
        if x[1:-1] == "Success":
            csrftoken = sess.cookies['csrftoken']
            print("Login Success! :)")
            while(True):
                print("▬▬ι═════════════════════════-   -════════════════════════ι▬▬")
                print("Please choose one of the following options:")
                print("Enter list for List (list all module instances and professors)")
                print("Enter view to View (rating of all professors)")
                print("Enter average to Average (view average of a certain professor in certain module)")
                print("Enter rate to Rate (rate a professor in certain module instance)")
                print("Enter logout to logout")
                print("enter exit to exit")
                print("▬▬ι═════════════════════════-   -════════════════════════ι▬▬")

                choice = input()
            
                if(choice == 'list'):
                    r = requests.get("http://127.0.0.1:8000/api/list")
                    data = r.json()
                    print('{:>0}  {:>5}  {:>25} {:>12} {:>12}'.format("Code", "Name", "Year", "Semester", "Taught By"))
                    print('════════════════════════════════════════════════════════════════════')

                    item = 0
                    counter = 0
                    for x in data:
                        print(f"{x['code']:5s} {x['name']:28s} {str(x['year']):10s} {str(x['semester']):10s}", end="", flush=True)

                        while True:
                            if f'teachersname {counter}' not in x:
                                counter = 0
                                item += 1
                                print("\n════════════════════════════════════════════════════════════════════")
                                break
                            else:
                                if(counter > 0 ):
                                    print(f",",end="", flush=True)
                                print(f"{data[item]['teachersname ' + str(counter)]:2s}", end="", flush=True)
                                print(f"({data[item]['teachersinit ' + str(counter)]:1s})", end="", flush=True)
                                counter += 1

                elif(choice == 'view'):
                    r = sess.get("http://127.0.0.1:8000/api/view")
                    json_data = json.loads(r.text)
                    for key,value in json_data.items():
                        stars = int(value) * '*'
                        print(f"The rating of {key} is {stars}")
            #TODO: check if the two terms are mashed together in the average for a module instance

                elif(choice == 'average'):
                    print("Please enter the Professor's unique ID")
                    professor_init = input()
                    print("Please enter the module code")
                    mod_code = input()

                    payload = {
                        'csrfmiddlewaretoken': csrftoken,
                        "professor_init" : professor_init,
                        "module_code" : mod_code
                    }


                    r = sess.post("http://127.0.0.1:8000/api/average", data = payload, cookies=cookies)
                    json_data = json.loads(r.text)
                    if(type(json_data) is dict):
                        x = "do nothing"

                    else:
                        text = json_data[1:-1]
                        if(text) == ("That teacher doesn't exist, please try again"):
                            print("*********************")
                            print(text)
                            print("*********************")
                            print("Taking you back to the menu")
                            continue

                        text2 = json_data[1:-1]
                        if(text2) == ("That module doesn't exist, please try again"):
                            print("*********************")
                            print("That module doesn't exist or isn't associated with given teacher id")
                            print("*********************")
                            print("Taking you back to the menu")
                            continue

                    for k,v in json_data.items():
                        stars = int(v) * '*'
                        print(f"The rating of {k} is {v}")

                elif(choice == 'rate'):
                    print("Please enter the Professor's unique ID")
                    professor_init = input()
                    print("Please enter the module code")
                    mod_code = input()
                    print("Please enter the year")
                    year = input()
                    print("Please enter the semester")
                    sem = input()
                    print("Please enter the rating you wish to give")
                    rating = input()

                    payload = {
                        'csrfmiddlewaretoken': csrftoken,
                        'professor_init' : professor_init,
                        'mod_code' : mod_code,
                        'year' : year,
                        'sem' : sem,
                        'rating' : rating
                    }

                    r = sess.post("http://127.0.0.1:8000/api/rating",data =payload, cookies=cookies)
                    json_data = json.loads(r.text)
                    if(json_data[1:-1] == "That rating is not a number, please try again"):
                        print("That rating is not a number, please try again")
                        continue
                    if(json_data == "That teacher doesn't exist, please try again"):
                        print("That teacher doesn't exist, please try again")
                        continue
                    elif(json_data == "Sorry, there doesn't exist a module with that code, year and rating"):
                        print("Sorry, there doesn't exist a module with that code, year and rating")
                    elif(json_data == "Rating has to be between 1 and 5"):
                        print("Sorry, Rating has to be between 1 and 5")
                        continue

                elif(choice == 'logout'):
                    r = sess.get("http://127.0.0.1:8000/api/logout",cookies=cookies)
                    x = json.loads(r.text)
                    for i in range(3):
                        print("............")

                    print("Logging out complete!")
                    print("Returning you to the main menu!")
                    break

                elif(choice == 'exit'):
                    print("Logging you out before exiting....")
                    r = sess.get("http://127.0.0.1:8000/api/logout",cookies=cookies)
                    x = json.loads(r.text)
                    print("Logging out complete!")

                    print("Exiting the client, have a very safe day!")
                    exit(0)


                else:
                    print("****************************")
                    print("Please pick a valid option.")
                    print("****************************")
                    continue



        else:
            print("Login Failed. Taking you back to the main menu.")


    elif(mm_answer == 'exit'):
        print("Exiting the client, have a very safe day!")
        break

    else:
        print("Please select a valid option.")
        continue
    #Register



    #Login

    # payload = {
    #     'username': 'sully',
    #     'password': 'left4dead2'
    # }

    # r = s.post("http://127.0.0.1:8000/api/login",data=payload)
    # cookies = dict(r.cookies)
    # x = json.loads(r.text)
    # print(x[1:-1])


    # # logout

    # r = s.get("http://127.0.0.1:8000/api/logout_user",cookies=cookies)
    # x = json.loads(r.text)
    # print(x[1:-1])

    # view

    # r = s.get("http://127.0.0.1:8000/api/view")
    # json_data = json.loads(r.text)
    # for key,value in json_data.items():
    #     stars = int(value) * '*'
    #     print(f"The rating of {key} is {stars}")

    # average for eacher

    # payload = {
    #     "professor_init" : "j.h",
    #     "module_code" : "xx1"
    # }


    # r = s.post("http://127.0.0.1:8000/api/average", data = payload)
    # json_data = json.loads(r.text)
    # for key,value in json_data.items():
    #     stars = int(value) * '*'
    #     print(f"The rating of {key} is {stars}")

    #TODO: check user is logged in for whatever needs login

    #TODO: change the payload to user input

    #rate



        # r = s.get("http://127.0.0.1:8000/api/rating")
        # json_data = json.loads(r.text)
        # print(json_data[1:-1])


    #list

