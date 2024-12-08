from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.models import *
import json
from django.core.serializers import serialize
# Create your views here.
from app.mixin import *
#----------------------------------------------------------------------------------------------------------------------------------------
def data_json(request):
    emp=employees.objects.get(eno=34)
    data={
        "eno":emp.eno,
        "ename":emp.ename,
        "esal":emp.esal,
        "eaddress":emp.eaddress
    }
    json_data=json.dumps(data)
    return HttpResponse(json_data)
#------------------------------------------------------------------------------------------------------------------------------------------

class data_jsoncbv(View):
    def get(self,request,*args,**kwargs):
        emp=employees.objects.get(eno=1)
        data={
        "eno":emp.eno,
        "ename":emp.ename,
        "esal":emp.esal,
        "eaddress":emp.eaddress
        }
        json_data=json.dumps(data)
        return HttpResponse(json_data,content_type="application/json")
    
#--------------------------------------------------------------------------------------------------------------------------------------------
class data_jsoncbv1(View):
    def get(self,request,id,*args,**kwargs):
        emp=employees.objects.get(eno=id)
        data={
        "eno":emp.eno,
        "ename":emp.ename,
        "esal":emp.esal,
        "eaddress":emp.eaddress
        }
        json_data=json.dumps(data)
        return HttpResponse(json_data,content_type="application/json")

#------------------------------------------------------------------------------------------------------------------------------------------

class data_jsoncbv2(View):
    def get(self,request,id,*args,**kwargs):
        emp=employees.objects.get(eno=id)
        json_data=serialize("json",[emp,])
        return HttpResponse(json_data,content_type="application/json")
    
#-------------------------------------------------------------------------------------------------------------------------------------------
class data_jsoncbv3(View):
    def get(self,request,*args,**kwargs):
        emp=employees.objects.all()
        json_data=serialize("json",emp)
        return HttpResponse(json_data,content_type="application/json")
    
#-------------------------------------------------------------------------------------------------------------------------------------------

class data_jsoncbv4(View):
    def get(self,request,*args,**kwargs):
        emp=employees.objects.all()
        json_data=serialize("json",emp)
        data=json.loads(json_data)
        data1=[]
        for i in data:
            data1.append(i["fields"])

        d=json.dumps(data1)
        return HttpResponse(d,content_type="application/json")
    
#---------------------------------------------------------------------------------------------------------------------------------------------

class data_jsoncbv5(mxied_data,View):
    def get(self,request,*args,**kwargs):
        emp=employees.objects.all()
        d=self.datarender(emp)
        return HttpResponse(d,content_type="application/json")
    
    
#-----------------------------------------------------------------------------------------------------------------------------------------
class data_jsoncbv6(View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp=employees.objects.get(eno=id)
        except Exception as p:
            d={"masg":"data is not avalable"}
            json_data=json.dumps(d)
            return HttpResponse(json_data,content_type="application/json",status=404)
        else:
            json_data=serialize("json",[emp,])
            return HttpResponse(json_data,content_type="application/json",status=200)

#---------------------------------------------------------------------------------------------------------------------------------------------

class data_jsoncbv7(httpdata,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp=employees.objects.get(eno=id)
        except Exception as p:
            d={"masg":"data is not avalable"}
            json_data=json.dumps(d)
            return self.datacontent(json_data,status=404)
        else:
            json_data=serialize("json",[emp,])  
            return self.datacontent(json_data)
        

#----------------------------------------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------postdata----------------------------------------------------------





# In [1]: from app.models import *

# In [2]: from django.core.serializers import serialize

# In [3]: emp=employees.objects.all()

# In [4]: json=serialize('json',emp)

# In [5]: json
# Out[5]: '[{"model": "app.employees", "pk": 1, "fields": {"eno": 1, "ename": "kavitha", "esal": 12000, "eaddress": "sullurupeta"}}, 
# {"model": "app.employees", "pk": 2, "fields": {"eno": 36638, "ename": "Destiny Gonzalez", "esal": 12000, "eaddress": "7794 Ballard Passage Suite 807\\nNorth Martin, FL 89399"}}, 
# {"model": "app.employees", "pk": 3, "fields": {"eno": 6036, "ename": "Christina Simpson", "esal": 12000, "eaddress": "78288 Crystal Villages\\nEricamouth, OR 53332"}},
# {"model": "app.employees", "pk": 4, "fields": {"eno": 72231, "ename": "John Fuller", "esal": 12000, "eaddress": "7562 Berg Cliffs Apt. 044\\nNorth Amber, MS 33584"}},
# {"model": "app.employees", "pk": 5, "fields": {"eno": 855, "ename": "Zachary George", "esal": 12000, "eaddress": "899 Hayden Dale\\nPhelpsfort, AK 23521"}}, 
# {"model": "app.employees", "pk": 6, "fields": {"eno": 930, "ename": "Zachary Campbell", "esal": 130000, "eaddress": "50143 Donna Rest Apt. 453\\nJosephville, AL 81431"}},
# {"model": "app.employees", "pk": 7, "fields": {"eno": 265, "ename": "Melissa Wells", "esal": 12000, "eaddress": "Unit 8667 Box 4545\\nDPO AA 61092"}}, 
# {"model": "app.employees", "pk": 8, "fields": {"eno": 977, "ename": "Stephen Alexander", "esal": 10000, "eaddress": "1720 Sutton Roads Suite 140\\nPerezview, AL 03042"}}, 
# {"model": "app.employees", "pk": 9, "fields": {"eno": 525, "ename": "Patrick Blackburn", "esal": 12000, "eaddress": "288 Briana Well Suite 778\\nSouth Amanda, PR 80264"}}, 
# {"model": "app.employees", "pk": 10, "fields": {"eno": 95, "ename": "Shawn Barber", "esal": 12000, "eaddress": "89443 Pamela Ramp Apt. 393\\nNathanstad, HI 84951"}},
#  {"model": "app.employees", "pk": 11, "fields": {"eno": 109, "ename": "Robert Glenn", "esal": 130000, "eaddress": "Unit 3790 Box 6479\\nDPO AA 25739"}},
# {"model": "app.employees", "pk": 12, "fields": {"eno": 100, "ename": "Fred Adams", "esal": 12000, "eaddress": "7541 Robert Forks Suite 809\\nKleinfurt, PA 97794"}},
#  {"model": "app.employees", "pk": 13, "fields": {"eno": 815, "ename": "Daniel Lang", "esal": 12000, "eaddress": "933 Knight Trafficway Suite 458\\nSouth Kimberlybury, ME 75535"}},
#  {"model": "app.employees", "pk": 14, "fields": {"eno": 34, "ename": "Samuel Huber", "esal": 130000, "eaddress": "7911 Barnes Gardens Suite 989\\nNew Kristie, VT 91958"}}]'


# In [6]: import json

# In [8]:  j=serialize('json',emp)

# In [9]: data=json.loads(j)

# In [10]: data
# Out[10]: 
# [{'model': 'app.employees',
#   'pk': 1,
#   'fields': {'eno': 1,
#    'ename': 'kavitha',
#    'esal': 12000,
#    'eaddress': 'sullurupeta'}},
#  {'model': 'app.employees',
#   'pk': 2,
#   'fields': {'eno': 36638,
#    'ename': 'Destiny Gonzalez',
#    'esal': 12000,
#    'eaddress': '7794 Ballard Passage Suite 807\nNorth Martin, FL 89399'}},
#  {'model': 'app.employees',
#   'pk': 3,
#   'fields': {'eno': 6036,
#    'ename': 'Christina Simpson',
#    'esal': 12000,
#    'eaddress': '78288 Crystal Villages\nEricamouth, OR 53332'}},
#  {'model': 'app.employees',
#   'pk': 4,
#   'fields': {'eno': 72231,
#    'ename': 'John Fuller',
#    'esal': 12000,
#    'eaddress': '7562 Berg Cliffs Apt. 044\nNorth Amber, MS 33584'}},
#  {'model': 'app.employees',
#   'pk': 5,
#   'fields': {'eno': 855,
#    'ename': 'Zachary George',
#    'esal': 12000,
#    'eaddress': '899 Hayden Dale\nPhelpsfort, AK 23521'}},
#  {'model': 'app.employees',
#   'pk': 6,
#   'fields': {'eno': 930,
#    'ename': 'Zachary Campbell',
#    'esal': 130000,
#    'eaddress': '50143 Donna Rest Apt. 453\nJosephville, AL 81431'}},
#  {'model': 'app.employees',
#   'pk': 7,
#   'fields': {'eno': 265,
#    'ename': 'Melissa Wells',
#    'esal': 12000,
#    'eaddress': 'Unit 8667 Box 4545\nDPO AA 61092'}},
#  {'model': 'app.employees',
#   'pk': 8,
#   'fields': {'eno': 977,
#    'ename': 'Stephen Alexander',
#    'esal': 10000,
#    'eaddress': '1720 Sutton Roads Suite 140\nPerezview, AL 03042'}},
#  {'model': 'app.employees',
#   'pk': 9,
#   'fields': {'eno': 525,
#    'ename': 'Patrick Blackburn',
#    'esal': 12000,
#    'eaddress': '288 Briana Well Suite 778\nSouth Amanda, PR 80264'}},
#  {'model': 'app.employees',
#   'pk': 10,
#   'fields': {'eno': 95,
#    'ename': 'Shawn Barber',
#    'esal': 12000,
#    'eaddress': '89443 Pamela Ramp Apt. 393\nNathanstad, HI 84951'}},
#  {'model': 'app.employees',
#   'pk': 11,
#   'fields': {'eno': 109,
#    'ename': 'Robert Glenn',
#    'esal': 130000,
#    'eaddress': 'Unit 3790 Box 6479\nDPO AA 25739'}},
#  {'model': 'app.employees',
#   'pk': 12,
#   'fields': {'eno': 100,
#    'ename': 'Fred Adams',
#    'esal': 12000,
#    'eaddress': '7541 Robert Forks Suite 809\nKleinfurt, PA 97794'}},
#  {'model': 'app.employees',
#   'pk': 13,
#   'fields': {'eno': 815,
#    'ename': 'Daniel Lang',
#    'esal': 12000,
#    'eaddress': '933 Knight Trafficway Suite 458\nSouth Kimberlybury, ME 75535'}},
#  {'model': 'app.employees',
#   'pk': 14,
#   'fields': {'eno': 34,
#    'ename': 'Samuel Huber',
#    'esal': 130000,
#    'eaddress': '7911 Barnes Gardens Suite 989\nNew Kristie, VT 91958'}}]

# In [11]:

