from django.shortcuts import render,redirect
from .models import  user,questions
from django.http import HttpResponse


# Create your views here.
def casestudyFun(request):
    if request.method == "POST":
        csname=request.POST['ip1']
        csid=int(request.POST['ip2'])
        case=user.objects.create(user_name=csname,user_id=csid)
        return redirect('questionsurl')
    return render(request,'casestudy/login.html')


def casestudy(request):
    user1=user.objects.all().first()
    ques=questions.objects.all()
    return render(request,'casestudy/questions.html',{'user':user1,'ques':ques})

def ScoreFun(request):
    numofques=questions.objects.count()
    quesattempted=0
    quescorrect=0
    quesincorrect=0
    if request.method == 'POST':
        questionsall=questions.objects.all()
        for q in questionsall:
            submit=request.POST.get(q.text)
            if submit:
                quesattempted += 1
                if submit == q.correct_answer:
                    quescorrect += 1
                else:
                    quesincorrect += 1
    return render(request,'casestudy/score.html',{'correct':quescorrect,'attempts':quesattempted,'numofques':numofques,'incorrect':quesincorrect})    


