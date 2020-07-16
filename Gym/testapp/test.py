import requests
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apicbv/'
r= requests.get(BASE_URL+ENDPOINT)
print(r)
data = r.json()
print(data)
print(type(data))
print(data['eno'])
print(data['ename'])
print(data['esal'])
print(data['eaddr'])

# status_code
# 100 --- information
# 200 --- success
# 300 ---  redirection
# 400 ---  Error
# 500 ---- Server Error