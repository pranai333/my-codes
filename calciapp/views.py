from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calciFun(request):
    if request.method == 'POST':
        #print(request.POST)
        n1=int(request.POST['i1'])
        n2=int(request.POST['i2'])
        if 'add' in request.POST:
            res=n1+n2
            action='Addition'
        elif 'sub' in request.POST:
            res=n1-n2
            action='Subtraction'
        elif 'mul' in request.POST:
            res=n1*n2  
            action='Multiplication'  
        else :
            res=n2/n1   
            action="Division" 
        return render(request,'calci.html',{'action':action,'result':res,'input1':n1,'input2':n2})
    return render(request, 'calci.html')
    return HttpResponse('function called')
