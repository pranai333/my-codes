from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from dbapp.models import Employee

class empserializer(ModelSerializer):
    class Meta:
        model=Employee
        fields=['empno','empname','salary','department']

class userserializer(ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']