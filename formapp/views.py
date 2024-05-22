from django.shortcuts import render,redirect
from .forms import firstforms,insertdata,Modelform
from dbapp.models import Employee,Department
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test
from .decorators import decfun,loginfun,checkgroup
from django.core.paginator import Paginator

# Create your views here.

def firstform(request):
    emptyform=firstforms()
    if request.method == 'POST':
       dataform=firstforms(request.POST)
       if dataform.is_valid() == True:
        name=dataform.cleaned_data['name']
        age=dataform.cleaned_data['age']
        return render(request,'formapp/first.html',{'name':name,'age':age,'form':dataform})
    return render(request,'formapp/first.html',{'form':emptyform})


#@user_passes_test( lambda user:user.is_superuser,login_url='emploginurl')
#@decfun
@checkgroup
@login_required(login_url='emploginurl')
def insertFun(request):
   emptyform=insertdata()
   if request.method == 'POST':
      dataform=insertdata(request.POST)
      if dataform.is_valid() == True:
         eno=dataform.cleaned_data['empno']
         ename=dataform.cleaned_data['empname']
         esal=dataform.cleaned_data['salary']
         edpt=dataform.cleaned_data['department']
         res=Department.objects.filter(dptno=edpt)
         if len(res) > 0:
            Employee.objects.create(empno=eno,empname=ename,salary=esal,department=res[0])
            messages.success(request,'Inserted Successfully')
            return render(request,'formapp/insert.html',{'form':emptyform})
         else:
            messages.error(request,'Department not valid')
            return render(request,'formapp/insert.html',{'form':dataform})     
   return render(request,'formapp/insert.html',{'form':emptyform})

def empmodelform(request):
   emptyform=Modelform()
   if request.method == 'POST':
      dataform=Modelform(request.POST,request.FILES)
      if dataform.is_valid()== True:
         dataform.save()
         messages.success(request,'inserted successfully')
         return render(request,'formapp/display.html',{'data':emptyform})
      else:
         messages.error(request,'data not valid')
         return render(request,'formapp/display.html',{'data':dataform})
   return render(request,'formapp/display.html',{'data':emptyform})

@login_required(login_url="emploginurl")
def selectemp(request,pno):
   emp=Employee.objects.all()
   ores=Paginator(emp,3)
   emps=ores.get_page(pno)
   return render(request,'formapp/select.html',{'data':emps})

@login_required(login_url='emploginurl')
def empdetails(request,eno):
   request.session.modified=True
   emp=Employee.objects.filter(empno=eno)
   if 'prev_emp' in request.session:
      if len(request.session['prev_emp'])>5:
         del request.session['prev_emp'][0]
         request.session['prev_emp'] +=[eno]
      else:
         request.session['prev_emp'] +=[eno] 
   else:
      request.session['prev_emp']=[eno]
   #print(request.session['prev_emp'])
   prev_emp=Employee.objects.filter(empno__in=request.session['prev_emp'])
   return render(request,'formapp/empdetails.html',{'data':emp,'data2':prev_emp})

@login_required(login_url='emploginurl')
def homefun(request):
   return render(request,'formapp/home.html')


@loginfun
def loginpage(request):
   if request.method == 'POST':
      user=request.POST['i1']
      pwd=request.POST['i2']
      valid_user=authenticate(request,username=user,password=pwd)
      if valid_user !=None:
         login(request,valid_user)
         return redirect('emphomeurl')
      else:
         messages.error(request,'Invalid credentials')
         return redirect('emploginurl')
   return render(request,'formapp/loginpage.html')

def logoutpage(request):
   logout(request)
   return redirect('emploginurl')

def signuppage(request):
   emptyform=UserCreationForm()
   if request.method =='POST':
      dataform=UserCreationForm(request.POST)
      if dataform.is_valid()== True:
         dataform.save()
         return redirect('emploginurl')
      else:
         return render(request,'formapp/signuppage.html',{'data':dataform})
   return render(request,'formapp/signuppage.html',{'data':emptyform})
