from django.urls import path
from .import views


urlpatterns=[
    path('',views.casestudyFun,name="caseurl"),
    path('questions/',views.casestudy,name="questionsurl"),
    path('score/',views.ScoreFun,name="scoreurl")
]