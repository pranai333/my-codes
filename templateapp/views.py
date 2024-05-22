from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def firstFun(request):
    return render(request,'first.html')
    return HttpResponse('function called')

def secondFun(request):
    return render(request,'second.html')