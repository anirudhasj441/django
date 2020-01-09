from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='register home'),
    path('studregister/',views.studRegister,name='Student regster form'),
    path('studregister/verify/',views.studVerify,name='Student regster form'),
    path('teacherregister/',views.teacherRegister,name='Teacher Register Form'),
    path('teacherregister/verify/',views.teacherVerify,name='Teacher Register Form'),
]