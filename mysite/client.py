from urllib import response
import requests
import json

s = requests.Session()

#Register

# payload = {'username': 'cccadasasdassasfsdfdssdasdsing', 'password': 'examp22le', "email": "asdasd@gmail.com"}

# r = requests.post("http://127.0.0.1:8000/app/register",data=payload)
# x = json.loads(r.text)
# print(x[1:-1])


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

