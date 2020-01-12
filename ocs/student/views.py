from django.shortcuts import render
from login.models import Student
from .models import Assigments,AssignmentDate
# Create your views here.
def student(request,pnr):
        stud = Student.objects.get(s_pnr=pnr)
        # return HttpResponse("<h2>welcome "+str(stud.s_name)+"</h2>")
        return render(request,'student/student.html',{'pnr':pnr})

def assignment(request,pnr):
        assignments = AssignmentDate.objects.all()
        return render(request,'student/assignment.html',{'assignments':assignments})
def questions(request,pnr,topic):
        # print(date)
        # datemod = changeFormat(date)
        # print(datemod)
        que = Assigments.objects.filter(topic=topic)
        return render(request,'student/questions.html',{'assignments':que})

def result(request,pnr,topic):
        correct = 0
        # datemod = changeFormat(date)
        if request.method == "POST":
                ans = Assigments.objects.filter(topic=topic)
                for i in ans:
                        a = request.POST.get("ans"+str(i.id))
                        print(a)
                        print(i.ans.lower())
                        if a.lower() == i.ans.lower():
                                correct += 1
        print(correct)

def changeFormat(date):
        datelist = date.split()
        month = datelist[0][:len(datelist[0])-1]
        dt = datelist[1][:len(datelist[1])-1]
        yr = datelist[2]
        if month=="Jan":
                mm = "01"
        elif month=="Feb":
                mm = "02"
        elif month=="Mar":
                mm = "03"
        elif month=="Apr":
                mm = "04"
        elif month=="May":
                mm = "05"
        elif month=="Jun":
                mm = "06"
        elif month=="Jul":
                mm = "07"
        elif month=="Aug":
                mm = "08"
        elif month=="Sep":
                mm = "09"
        elif month=="Oct":
                mm = "10"
        elif month=="Nov":
                mm = "11"
        else:
                mm = "12"
        dateMod = yr+"-"+mm+"-"+dt
        return dateMod
