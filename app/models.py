from django.db import models

# Create your models here.
class employees(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=200)
    esal=models.IntegerField()
    eaddress=models.CharField(max_length=200)
