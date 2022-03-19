from urllib import response
import requests
import json



# payload = {'username': 'cccadasasdassasfsdfdssdasdsing', 'password': 'examp22le', "email": "asdasd@gmail.com"}

# r = requests.post("http://127.0.0.1:8000/app/register",data=payload)
# x = json.loads(r.text)
# print(x[1:-1])


r = requests.get("http://127.0.0.1:8000/app/list")
data = r.json()
print('{:>8}  {:>8}  {:>8} {:>12} {:>12}'.format("Code", "Name", "Year", "Semester", "Taught By"))

for x in data:
    print(x['code'].rjust(8*6))
    # print(type(data))
    # print(data)
# print((data))















# json_data = r.json()
# print(type(json_data))

# data = json.loads(r.text)
# data = 


# x = x.replace(r'\n', '\n')
# x = x.replace(' ', ''.ljust(8))


# print(x[1:-1])
