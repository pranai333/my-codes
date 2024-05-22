from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calcFun(request):
    if request.method == 'POST':
        #print(request.POST)
        n1=int(request.POST['i1'])
        n2=int(request.POST['i2'])
        res=n1+n2
        output=str(res)
        return render( request,'calculator.html',{'answer':output})
    return render(request , 'calculator.html',)


    
    
    
    
    