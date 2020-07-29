import json
from django.http import HttpResponse
from django.core.serializers import serialize

class HttpResponseMixin(object):
    def render_to_http_response(self, json_data):
        return HttpResponse(json_data,content_type='application/json', status=200)

class SerializeMixin(object):
    def serialize(self, qs):
        json_data = serialize('json',qs)
        pdata = json.loads(json_data)
        final_list = []
        for obj in pdata:
            stu_data = obj['fields']
            final_list.append(stu_data)
        json_data = json.dumps(final_list)
        return json_data
