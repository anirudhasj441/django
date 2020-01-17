from django.shortcuts import render,redirect
from login.models import Student,Teacher
from passlib.hash import argon2
from django.http import HttpResponse
from django.contrib import messages
from smtplib import *
import random
import json

# Create your views here.

in_spnr = ""
in_sname = ""
in_sdob = ""
in_sgender = ""
in_sclass =""
in_sroll = ""
in_scont = ""
in_semail =""
in_spasswd = "" 
in_scpasswd = ""

in_tname = ""
in_tnr = ""
in_tdob = ""
in_temail = ""
in_tcont = ""
in_tpasswd = ""
in_tcpasswd = ""

otp = 0

def index(request):
    return render(request,'register/index.html')

def studRegister(request):
    global in_spnr,in_sname,in_sdob,in_sgender,in_sclass,in_sroll,in_scont,in_semail,in_spasswd,in_scpasswd
    if request.method=="POST":
        try:
            in_spnr = request.POST.get("pnr")
            in_sname = request.POST.get("s_name")
            in_sdob = request.POST.get("dob")
            in_sgender = request.POST.get("gender")
            in_sclass = request.POST.get("class")
            in_sroll = request.POST.get("roll")
            in_scont = request.POST.get("Contact")
            in_semail = request.POST.get("email")
            in_spasswd = request.POST.get("passwd")
            in_scpasswd = request.POST.get("c_passwd")
            if in_spasswd != in_scpasswd:
                raise Exception
        except Exception:
            # return render(request,'register/studregister.html',{'register':False})
            messages.error(request,'Password and Confirm Password should be same')
        else:
            otpGeneratorStud()
            return redirect('verify/')
            # print(in_sname)
            # print(in_sclass)
            # print(in_scont)
            # print(in_sgender)
    return render(request,'register/studregister.html')


def teacherRegister(request):
    global in_tname,in_tnr,in_tdob,in_temail,in_tcont,in_tpasswd,in_tcpasswd
    if request.method=="POST":
        try:
            in_tname = request.POST.get("t_name")
            in_tnr = request.POST.get("tnr")
            in_tdob = request.POST.get("dob")
            in_temail = request.POST.get("email")
            in_tcont = request.POST.get("contact")
            in_tpasswd = request.POST.get("passwd")
            in_tcpasswd = request.POST.get("c_passwd")
            if in_tpasswd != in_tcpasswd:
                raise Exception
        except Exception:
            # return render(request,'register/teacherregister.html',{'register':False})
            messages.error(request,'Password and Confirm Password should be same')
        else:
            otpGeneratorTeacher()
            return redirect('verify/')
    return render(request,'register/teacherregister.html')

def otpGeneratorStud():
    global otp
    otp = random.randint(1000,9999)
    reciever = in_semail
    msg = "Hi "+str(in_sname)+"\n\n"+"Thank you for register\n\nOTP:"+str(otp)
    conn = SMTP('smtp.gmail.com',587)
    conn.ehlo()
    conn.starttls()
    conn.login('anirudhasj441@gmail.com','82682290')
    conn.sendmail('anirudhasj441@gmail.com',reciever,msg)
    conn.quit()

def otpGeneratorTeacher():
    global otp
    otp = random.randint(1000,9999)
    reciever = in_temail
    msg = "Hi "+str(in_tname)+"\n\n"+"Thank you for register\n\nOTP:"+str(otp)
    conn = SMTP('smtp.gmail.com',587)
    conn.ehlo()
    conn.starttls()
    conn.login('anirudhasj441@gmail.com','82682290')
    conn.sendmail('anirudhasj441@gmail.com',reciever,msg)
    conn.quit()

def studVerify(request):
    if request.method == "POST":
        try:
            in_otp = request.POST.get("otp")
            if int(in_otp) != otp:
                raise Exception
            else:
                stud = Student()
                passwd = argon2.hash(in_spasswd)
                stud.s_pnr = in_spnr
                stud.s_name = in_sname
                stud.s_dob = in_sdob
                stud.s_gender = in_sgender
                stud.s_class = in_sclass
                stud.s_roll = in_sroll
                stud.s_contact = in_scont
                stud.s_email = in_semail
                stud.s_passwd = passwd
                stud.save()
        except Exception:
            # return render(request,'register/verify.html',{'register':True})        
            messages.error(request,'OTP is Wrong!')
        else:
            messages.success(request,'Succesfullly Register!')
            return redirect('/register/studregister')
    return render(request,'register/verify.html')

def teacherVerify(request):
    if request.method == "POST":
        try:
            in_otp = request.POST.get("otp")
            print(otp)
            print(in_otp)
            if int(in_otp) != otp:
                raise Exception
            else:
                teacher = Teacher()
                passwd = argon2.hash(in_tpasswd)
                teacher.tnr = in_tnr
                teacher.t_name = in_tname
                teacher.t_dob = in_tdob
                teacher.t_email= in_temail
                teacher.t_cont = in_tcont
                teacher.t_passwd = passwd
                teacher.save()
        except Exception:
            messages.error(request,'OTP is Wrong!')
        else:
            messages.success(request,'Succesfullly Register!')
            return redirect('/register/teacherregister/')
    return render(request,'register/verify.html')