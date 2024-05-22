from django.db import models

# Create your models here.
class Employee(models.Model):
    emplyno=models.IntegerField(primary_key="True")
    emplyname=models.CharField(max_length=20)
    salary=models.IntegerField()