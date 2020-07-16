from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from .models import Employee
# Create your views here.
def simpleview(request):
    emp_data = {
        'eno':100,
        'ename':'abhijit',
        'esal':1000,
        'eaddr':'Mumbai',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

class SimpleViewCBV(View):
    def get(self,request,*args, **kwargs):
        try:
            emp= Employee.objects.get(id=5)
            emp_data = {
                'ename':emp.name,
                'eroll':emp.roll,
                'emark':emp.marks,
                'eaddr':emp.addr,
            }
            json_data = json.dumps(emp_data)
        except:
            json_data = json.dumps({'msg':'the requested resource is not available'})
            return HttpResponse(json_data, content_type='application/json')
        else:
            return HttpResponse(json_data, content_type='application/json')

# id passed to get()
class SimpleViewGETCBV(View):
    def get(self,request,id,*args, **kwargs):
        try:
            emp= Employee.objects.get(id=id)
            emp_data = {
                'ename':emp.name,
                'eroll':emp.roll,
                'emark':emp.marks,
                'eaddr':emp.addr,
            }
            json_data = json.dumps(emp_data)
        except:
            json_data = json.dumps({'msg':'the requested resource is not available'})
            return HttpResponse(json_data, content_type='application/json')
        else:
            return HttpResponse(json_data, content_type='application/json')