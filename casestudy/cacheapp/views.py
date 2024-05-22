from django.shortcuts import render
from django.urls import reverse
from dbapp.models import Employee
from django.views.decorators.cache import cache_page
from django.views import View
from django.http import HttpResponse
from django.views.generic.list import ListView
from dbapp.models import Employee
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView


# Create your views here.

#@cache_page(60)
def cacheFun(request):
    res=Employee.objects.all()
    return render(request,'cacheapp/cache.html',{'data':res})

class FirstView(View):
    def get(self,request):
        return render(request,'cacheapp/classbasedview.html')
    
    def post(self,request):
        t1=request.POST['t1']
        return render(request,'cacheapp/classbasedview.html',{'data':t1})
    

def functionview(request):
    if request.method == 'POST':
        t1=request.POST['t1']
        return render(request,'cacheapp/classbasedview.html',{'data':t1})
    
    return render(request,'cacheapp/classbasedview.html')    

class secondview(FirstView):
    def get(self,request):
        return HttpResponse('second view')
    
class thirdview(ListView):
    model=Employee
    template_name='cacheapp/cbvselect.html'

class insertview(CreateView):
    model=Employee
    fields='__all__'
    template_name='cacheapp/cbvinsert.html'  

    def get_success_url(self):
        return reverse('cbvselecturl')
    
class empdetails(DetailView):
    model=Employee
    template_name='cacheapp/cbvdetail.html'   

class empupdate(UpdateView):
    model=Employee
    fields='__all__'
    template_name='cacheapp/cbvupdate.html'  

    def get_success_url(self):
        return reverse('cbvselecturl')
    
class empdelete(DeleteView):
    model=Employee
    template_name='cacheapp/cbvdelete.html'    
    
    def get_success_url(self):
        return reverse('cbvselecturl')