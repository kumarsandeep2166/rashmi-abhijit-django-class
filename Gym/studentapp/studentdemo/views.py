from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .mixins import SerializeMixin, HttpResponseMixin
from .models import Student
from .utils import is_json
import json
# Create your views here.

def student_list(request):
    return HttpResponse('<h1>Hello</h1>')

class StudentCRUDView(SerializeMixin,HttpResponseMixin,View):

    def get_object_by_id(self, id):
        try:
            stu = Student.objects.get(id=id)
        except Student.DoesNotExist:
            stu = None
        return stu

    def get(self, request, *args, **kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please Provide Valid Data!!'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id = pdata.get('id', None)
        if id is not None:
            stu = self.get_object_by_id(id)
            if stu is None:
                json_data = json.dumps({'msg':'No matched records found!!'})
                return self.render_to_http_response(json_data,status=400)
            json_data = self.serialize([stu,])
            return self.render_to_http_response(json_data)

        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self, request, *args, **kwargs):
        pass

    def put(self, request, *args, **kwargs):
        pass

    def delete(self, request, *args, **kwargs):
        pass