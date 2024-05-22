from django.shortcuts import render,redirect
from django.http import HttpResponse
from dbapp.models import Employee,Department
from django.db.models import Sum,Avg,Min,Max

# Create your views here.

def dbappFun(request):
   if request.method == 'POST':
      eno=int(request.POST['empno'])
      ename=request.POST['empname']
      esal=int(request.POST['esal'])
      edpt=int(request.POST['edpt'])
      dptno=Department.objects.filter(dptno=edpt)
      if len(dptno) > 0:
         emp=Employee(empno=eno,empname=ename,salary=esal,department=dptno[0])
         emp.save()
         return HttpResponse('records submited')
      else:
         return HttpResponse('Department not found')
   emp=Department.objects.all()   
   return render(request,'dbapp/insert.html',{'data':emp})

def selectFun(request):
   #emps=Employee.objects.all()
   emps=Employee.objects.select_related('department')
   sum=Employee.objects.aggregate(total_salary=Sum('salary'))['total_salary']
   avg=Employee.objects.aggregate(total_avg=Avg('salary'))['total_avg']
   return render(request,'dbapp/select.html',{'data':emps,'sum':sum,'avg':avg})

def updateFun(request,eno):
   if request.method == 'POST':
      eno=int(request.POST['i1'])
      ename=request.POST['i2']
      esal=int(request.POST['i3'])
      edpt=int(request.POST['i4'])
      dptno=Department.objects.filter(dptno=edpt)
      if len(dptno) > 0:
         emp=Employee(empno=eno,empname=ename,salary=esal,department=dptno[0])
         emp.save()
         return HttpResponse('records submited')
      else:
         return HttpResponse('Department not found')
   emps=Employee.objects.filter(empno =eno)
   edpt=Department.objects.all()
   return render(request,'dbapp/update.html',{'data':emps,'data2':edpt})

def deleteFun(request,eno):
   emp=Employee.objects.filter(empno=eno)
   emp.delete()
   return redirect('selecturl')
   
   