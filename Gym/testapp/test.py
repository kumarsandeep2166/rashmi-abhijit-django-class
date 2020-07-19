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
    r= requests.get(BASE_URL+ENDPOINT+str(id)+'/')
    if r.status_code in range(200, 300):
        print(r.status_code)
        print(r.json())
    else:
        print(r.status_code)
        print('something goes wrong')
# id = input('enter an id:')
# get_resource(id)

def get_all():
    ENDPOINT = 'listcbv/'
    r = requests.get(BASE_URL+ENDPOINT)
    print(r.status_code)
    print(r.json())
    print(type(r.json()))
# get_all()

def create_resource():
    ENDPOINT = 'listcbv/'
    new_emp = {
        'name':'Swaynashu',
        'roll':500,
        'marks':456.78,
        'addr':'BBSR'
    }
    resp = requests.post(BASE_URL+ENDPOINT, data=json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())
# create_resource()

def update_resource(id):
    new_emp = {        
        'marks':4897,
        'addr':'Delhi'
    }
    r= requests.put(BASE_URL+ENDPOINT+str(id)+'/', data=json.dumps(new_emp))
    print(r.status_code)
    print(r.json())
# update_resource(6)

def delete_resource(id):
    r= requests.delete(BASE_URL+ENDPOINT+str(id)+'/')
    print(r.status_code)
    print(r.json())
delete_resource(6)