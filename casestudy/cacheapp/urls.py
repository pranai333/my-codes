from django.urls import path
from . import views

urlpatterns=[
    path('',views.cacheFun),
    path('class/',views.secondview.as_view()),
    path('functionview/',views.functionview,name='functionviewurl'),
    path('select/',views.thirdview.as_view(),name='cbvselecturl'),
    path('insert/',views.insertview.as_view()),
    path('detail/<int:pk>',views.empdetails.as_view()),
    path('update/<int:pk>',views.empupdate.as_view()),
    path('delete/<int:pk>',views.empdelete.as_view()),
]