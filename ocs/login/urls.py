from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Login Home"),
    path('studlogin/',views.studlogin,name="Student Login"),
    path('teacherlogin/',views.teacherlogin,name='Teacher Login'),
]