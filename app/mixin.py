from django.core.serializers import serialize
import json

class mxied_data(object):
    def datarender(self,qr):
        json_data=serialize("json",qr)
        data=json.loads(json_data)
        data1=[]
        for i in data:
            data1.append(i["fields"])

        json_data=json.dumps(data1)
        return json_data
    
from django.http import HttpResponse
class httpdata(object):
    def datacontent(self,json_data,status=200):
        return HttpResponse(json_data,content_type="application/json",status=status)