from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def displayfun(request):
    if request.method == 'post':
        return render(x)
    return HttpResponse('wellcome to my world')
                        

