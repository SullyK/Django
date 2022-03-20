from urllib import response
import requests
import json



# payload = {'username': 'cccadasasdassasfsdfdssdasdsing', 'password': 'examp22le', "email": "asdasd@gmail.com"}

# r = requests.post("http://127.0.0.1:8000/app/register",data=payload)
# x = json.loads(r.text)
# print(x[1:-1])


r = requests.get("http://127.0.0.1:8000/app/list")
data = r.json()
# print(data)
# print(type(data))
print('{:>0}  {:>9}  {:>20} {:>12} {:>12}'.format("Code", "Name", "Year", "Semester", "Taught By"))
print('---------------------------------------------------------------')

item = 0
counter = 0
for x in data:
    # print(x)
    while True:
        if f'teachers {counter}' not in x:
            counter = 0
            item += 1
            print("-----------")
            break
        else:
            print(data[item]['teachers ' + str(counter)])
            counter += 1

#     print(str(x['code']).ljust(10),end="", flush=True)
#     print(str(x['name']).ljust(3),end="", flush=True)
#     print(str(x['year']).ljust(15),end="", flush=True)
#     print(str(x['semester']).ljust(8*4))
#     print(len(str(x['teachers ' + str(int)])))
#     print('{:>0} {:>15}'.format(x['code'],x['name']))

    # print(f"{x['code']:10s} {x['name']:20s} {str(x['year']):10} {str(x['semester']):10s} {str(x[f'teachers {int}    ']):10s}")
    # int += 1

    # print(str(x['name']).ljust(3),end="", flush=True)
    # print(str(x['year']).ljust(15),end="", flush=True)
    # print(str(x['semester']).ljust(8*4))

    # print(type(data))
    # print(data)
# print((data))















# json_data = r.json()
# print(type(json_data))

# data = json.loads(r.text)
# data = 


# x = x.replace(r'\n', '\n')
# x = x.replace(' ', ''.ljust(8))


# print(x[1:-1]