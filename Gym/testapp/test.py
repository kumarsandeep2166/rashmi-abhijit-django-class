import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
ENDPOINT = 'apicbv/'



# status_code
# 100 --- information
# 200 --- success
# 300 ---  redirection
# 400 ---  Error
# 500 ---- Server Error

def get_resource(id):
    r= requests.get(BASE_URL+ENDPOINT+id+'/')
    print(r)
    data = r.json()
    print(data)
# get_resource(6)

def get_all():
    ENDPOINT = 'listcbv/'
    r = requests.get(BASE_URL+ENDPOINT)
    print(r.status_code)
    print(r.json())
get_all()