from django.shortcuts import render

# Create your views here.

def sessionfun(request):
    request.session.modified=True
    if request.method == 'POST':
        fruit=request.POST['t1']
        if 'fruits' in request.session:
            request.session['fruits'].append(fruit)
        else:    
            request.session['fruits']=[fruit]
        return render(request,'sessionapp/session.html',{'data':request.session['fruits']})
    return render(request,'sessionapp/session.html')