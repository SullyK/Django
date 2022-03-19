import requests
import json

# payload = {'username': 'cccadasasdassasfsdfdssdasdsing', 'password': 'examp22le', "email": "asdasd@gmail.com"}

# r = requests.post("http://127.0.0.1:8000/app/register",data=payload)
# x = json.loads(r.text)
# print(x[1:-1])


r = requests.get("http://127.0.0.1:8000/app/list")
x = json.loads(r.text)
x = x.replace(r'\n', '\n')
x = x.replace(' ', ''.ljust(8))

print('{:>8}  {:>8}  {:>8} {:>12} {:>12}'.format("Code", "Name", "Year", "Semester", "Taught By"))

print(x[1:-1])