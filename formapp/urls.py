from django.urls import path
from . import views

urlpatterns=[
    path('firstform',views.firstform),
    path('',views.loginpage,name="emploginurl"),
    path('logoutpage',views.logoutpage,name='emplogouturl'),
    path('signuppage',views.signuppage,name='empsignupurl'),
    path('insert/',views.insertFun,name="inserturl"),
    path('modelinsert/',views.empmodelform,name="modelinserturl"),
    path('select/<int:pno>',views.selectemp,name="selecturl"),
    path('detail/<int:eno>/',views.empdetails,name="detailurl"),
    path('homepage/',views.homefun,name='emphomeurl')
]