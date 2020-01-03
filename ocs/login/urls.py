from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="Login Home"),
    path('studlogin/',views.studlogin,name="Student Login"),
    path('teacherlogin/',views.teacherlogin,name='Teacher Login'),
    path('studlogin/student/<int:pnr>',views.student,name='student homepage'),
    path('teacherlogin/teacher/<str:tname>',views.teacher,name='teacher homepage')
]