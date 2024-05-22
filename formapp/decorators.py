from django.shortcuts import redirect
from django.contrib import messages

def decfun(fun):
    def innerfun(request):
        if request.user.is_superuser== True:
            return fun(request)
        else:
            return redirect('emphomeurl')
        
    return innerfun

def loginfun(f):
    def innerfun(request):
        if request.user.is_authenticated:
            return redirect('emphomeurl')
        else:
            return f(request)
    return innerfun

def checkgroup(ff):
    def innerfun(request):
        if 'python' in str(request.user.groups.all()[0]):
            return ff(request)
        else:
            messages.error(request,'you dont have permissions')
            return redirect('emphomeurl')

    return innerfun    