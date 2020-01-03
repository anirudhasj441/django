from django.shortcuts import render,redirect
from django.http import HttpResponse , HttpResponseRedirect
from .models import Student,Teacher
from passlib.hash import argon2
# Create your views here.
def index(request):
    return HttpResponse("login page here")

def studlogin(request):
    if request.method=="POST":
        try:
            in_pnr = request.POST.get("pnr")
            in_passwd = request.POST.get("passwd")
            stud = Student.objects.get(s_pnr=in_pnr)
            if argon2.verify(in_passwd,str(stud.s_passwd)):
                return redirect('student/'+in_pnr)        
            else:
                raise Student.DoesNotExist

        except Student.DoesNotExist:
            return render(request,'login/studlogin.html',{'not_found':True})
        except ValueError:
            return render(request,'login/studlogin.html',{'value_error':True})
    return render(request,'login/studlogin.html',{'not_found':False})

def teacherlogin(request):
    if request.method=="POST":
        try:
            in_tname = request.POST.get("t_name")
            in_passwd = request.POST.get("t_passwd")
            teacher = Teacher.objects.get(t_name=in_tname)
            if argon2.verify(in_passwd,teacher.t_passwd):
                return redirect('teacher/'+in_tname)
            else:
                raise Teacher.DoesNotExist    
        except Teacher.DoesNotExist:
            return render(request,'login/teacherlogin.html',{'not_found':True})        
    return render(request,'login/teacherlogin.html',{'not_found':False})

def student(request,pnr):
        stud = Student.objects.get(s_pnr=pnr)
        return HttpResponse("<h2>welcome "+str(stud.s_name)+"</h2>")
def teacher(request,tname):
    teacher = Teacher.objects.get(t_name=tname)
    return HttpResponse('<h1>Welcome '+str(teacher.t_name)+'</h1>')
