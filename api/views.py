from django.shortcuts import render
from dbapp.models import Employee
from django.http import JsonResponse
from .serializers import empserializer,userserializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import authentication_classes,permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST,HTTP_200_OK
from rest_framework.decorators import api_view
import json

# Create your views here.
def getdata(request):
    emps=Employee.objects.all().values()
    data=[d for d in emps]
    #print(data)
    res=json.dumps(data)
    return JsonResponse(res,safe=False)


@api_view(['GET','POST'])
#@authentication_classes([TokenAuthentication])
#@permission_classes([IsAuthenticated])
def getdatarest(request):
    if request.method == 'GET':
        emps=Employee.objects.all()
        employee=empserializer(emps,many=True)
        return Response(employee.data)
    elif request.method == 'POST':
        emps=empserializer(data=request.data)
        if emps.is_valid()== True:
            emps.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(data=emps.errors,status=HTTP_400_BAD_REQUEST)
            
@api_view(['GET','PUT','DELETE'])
def modifyhandler(request,pk):
    emps=Employee.objects.get(empno=pk)

    if request.method == 'GET':
        empsobj=empserializer(emps)
        return Response(data=empsobj.data,status=HTTP_200_OK)
    elif request.method == 'PUT':
        emp=empserializer(emps,data=request.data)
        
        if emp.is_valid()== True:
            emp.save()
            return Response(status=HTTP_200_OK)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        emps.delete()
        return Response(status=HTTP_200_OK)
    
@api_view(['POST'])
def registeruser(request):
    user=userserializer(data=request.data)
    if user.is_valid() == True:
        udetails=user.save()

        tkn=Token.objects.create(user=udetails)
        userdetails={
            'username':udetails.username,
            'token':tkn.key
        }
        return Response(userdetails,status=HTTP_200_OK)
    else:
        return Response(user.errors,status=HTTP_400_BAD_REQUEST)