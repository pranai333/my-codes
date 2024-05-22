from django.urls import path
from . import views


urlpatterns=[
    path('display/',views.displayFun,name="displayurl"),
    path('insert/',views.insertFun,name='inserturl'),
    path('update/<int:eno>/',views.updateFun,name="updateurl"),
    path('delete/<int:eno>/',views.deleteFun,name="deleteurl")
]