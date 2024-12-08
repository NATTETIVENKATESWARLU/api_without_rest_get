from django.contrib import admin
from app.models import *

# Register your models here.

class employee_1(admin.ModelAdmin):
    list_display=["eno","ename","esal","eaddress"]


admin.site.register(employees,employee_1)
