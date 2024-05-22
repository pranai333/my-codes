from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee

# Create your views here.
def displayFun(request):
    res=Employee.objects.all()
    return render(request,'revision/display.html',{'data':res})

def insertFun(request):
    if request.method == "POST":
        eno=int(request.POST['i1'])
        ename=request.POST['i2']
        esal=int(request.POST['i3'])
        Employee.objects.create(emplyno=eno,emplyname=ename,salary=esal)
        return redirect('displayurl')
    return render(request,'revision/insert.html')

def updateFun(request,eno):
    if request.method == "POST":
        enum=request.POST['i1']
        ename=request.POST['i2']
        esal=request.POST['i3']
        emp=Employee(emplyno=enum,emplyname=ename,salary=esal)
        emp.save()
        return redirect('displayurl')
    eno=Employee.objects.filter(emplyno=eno)
    return render(request,'revision/update.html',{'rev':eno})

def deleteFun(request,eno):
    res=Employee.objects.filter(emplyno=eno)
    res.delete()
    return redirect('displayurl')
