from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns=[
    path('',views.getdata),
    path('rest/',views.getdatarest),
    path('modify/<int:pk>/',views.modifyhandler),
    path('signup/',views.registeruser),
    path('login/',obtain_auth_token)
]