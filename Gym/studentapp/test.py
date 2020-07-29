import requests
import json
BASE_URL = 'http://127.0.0.1:8000/'
END_POINT= 'api/'

def get_resource(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    r = requests.get(BASE_URL+END_POINT,data=json.dumps(data))
    print(r.status_code)
    print(r.json())

get_resource(10)