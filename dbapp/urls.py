from django.urls import path
from .import views

urlpatterns=[
    path('',views.dbappFun,name="inserturl"),
    path('select/',views.selectFun,name="selecturl"),
    path('update/<int:eno>/',views.updateFun,name="update1url"),
    path('delete/<int:eno>/',views.deleteFun,name='delete1url')
]