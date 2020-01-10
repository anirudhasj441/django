from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Student,Teacher
from passlib.hash import argon2
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'login/index.html')

def studlogin(request):
    if request.method=="POST":
        try:
            in_pnr = request.POST.get("pnr")
            in_passwd = request.POST.get("passwd")
            stud = Student.objects.get(s_pnr=in_pnr)
            if argon2.verify(in_passwd,str(stud.s_passwd)):
                return redirect('/student/'+str(stud.s_pnr))        
            else:
                raise Student.DoesNotExist

        except Student.DoesNotExist:
            # return render(request,'login/studlogin.html',{'not_found':True})
            messages.error(request,'PNR or Password incorrect')
        except ValueError:
            return render(request,'login/studlogin.html',{'value_error':True})
    return render(request,'login/studlogin.html',{'not_found':False})

def teacherlogin(request):
    if request.method=="POST":
        try:
            in_tnr = request.POST.get("tnr")
            in_passwd = request.POST.get("t_passwd")
            teacher = Teacher.objects.get(tnr=in_tnr)
            if argon2.verify(in_passwd,teacher.t_passwd):
                return redirect('/teacher/'+str(teacher.t_id))
            else:
                raise Teacher.DoesNotExist
        except Teacher.DoesNotExist:
            # return render(request,'login/teacherlogin.html',{'not_found':True})
            messages.error(request,'Name or Passwrd incorrect')
    return render(request,'login/teacherlogin.html',{'not_found':False})