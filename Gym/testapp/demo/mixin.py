import json
from django.core.serializers import serialize
from django.http import HttpResponse

class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json',qs)
        p_dict = json.loads(json_data)
        # start iteration
        final_list = []
        for obj in p_dict:
            emp_data = obj['fields']
            final_list.append(emp_data)
        json_data = json.dumps(final_list)
        print(type(json_data))
        return json_data

class HttpResponseMixin(object):
    def render_to_http_response(self, json_data, status=200):
        return HttpResponse(json_data, content_type='application/json',status=status)