from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.generic import View
from .models import Employee
# from django.core.serializers import serialize
from demo.mixin import SerializeMixin, HttpResponseMixin
from demo.utils import is_json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .forms import EmployeeForm

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
@method_decorator(csrf_exempt, name='dispatch')
class SimpleViewGETCBV(SerializeMixin,HttpResponseMixin,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id) 
        except Employee.DoesNotExist:
            emp=None
        return emp
    
    def get(self,request,id,*args, **kwargs):
        try:
            emp= Employee.objects.get(id=id) 
        except:
            json_data = json.dumps({'msg':'the requested resource is not available'})
            return self.render_to_http_response(json_data, status=400)
        else:
            json_data = self.serialize([emp,])
            return self.render_to_http_response(json_data)

    def put(self,request,id,*args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Matched Resource Not Found'})
            return self.render_to_http_response(json_data, status=404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send appropriate data'})
            return self.render_to_http_response(json_data, status=400)
        empdata = json.loads(data)
        original_data ={
            'name':emp.name,
            'roll':emp.roll,
            'marks':emp.marks,
            'addr':emp.addr,
            }
        original_data.update(empdata)
        form = EmployeeForm(original_data, instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'resource added successfully'})
            return self.render_to_http_response(json_data)        
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)

    def delete(self, request, id, *args, **kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'Matched Resource Not Found, Please try Again'})
            return self.render_to_http_response(json_data, status=404)
        t = emp.delete()
        print(t)
        status,deleted_item = emp.delete()
        if status == 1:
            json_data = json.dumps({'msg':'Your Data Deleted Successfully'})
            return self.render_to_http_response(json_data)
        else:
            json_data = json.dumps({'msg':'Sorry!!!! Please try Again'})
            return self.render_to_http_response(json_data, status=404)


@method_decorator(csrf_exempt, name='dispatch')
class SimpleListCBV(SerializeMixin,HttpResponseMixin,View):
    def get(self, requst, *args, **kwargs):
        qs = Employee.objects.all()
        # make the queryset serialize
        json_data = self.serialize(qs)     
        # print(type(json_data))
        return self.render_to_http_response(json_data, status=200)

    def post(self, requst, *args, **kwargs):
        data = requst.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'please send appropriate data'})
            return self.render_to_http_response(json_data, status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'resource added successfully'})
            return self.render_to_http_response(json_data)        
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data, status=400)