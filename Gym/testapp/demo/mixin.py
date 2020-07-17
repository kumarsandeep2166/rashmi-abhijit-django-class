import json
from django.core.serializers import serialize

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
        return json_data