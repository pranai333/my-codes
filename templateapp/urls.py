from django.urls import path
from .import views

urlpatterns=[
    path('first/',views.firstFun),
    path('second/',views.secondFun),
]