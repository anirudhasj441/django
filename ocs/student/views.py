from django.shortcuts import render,redirect
from login.models import Student
from .models import Assigments,AssignmentDate,Result,SolvedAssignments
from django.contrib.sessions.models import Session
from datetime import date
# Create your views here.
def student(request,pnr):
        if request.session.has_key('stud_loged'):
                stud = Student.objects.get(s_pnr=pnr)
                # return HttpResponse("<h2>welcome "+str(stud.s_name)+"</h2>")
                return render(request,'student/student.html',{'pnr':pnr})
        else:
                return redirect('/')

def assignment(request,pnr):
        if request.session.has_key('stud_loged'):
                ass = []
                assignments = AssignmentDate.objects.all()
                for i in assignments:
                        print(i.a_duedate)
                        print(date.today())
                        if i.a_duedate>date.today():
                                ass.append(i)
                return render(request,'student/assignment.html',{'assignments':ass})
        else:
                return redirect('/')
def questions(request,pnr,topic):
        if request.session.has_key('stud_loged'):
                que = Assigments.objects.filter(topic=topic)
                date = AssignmentDate.objects.get(a_topic=topic)
                return render(request,'student/questions.html',{'assignments':que,'date':date.a_date,'duedate':date.a_duedate})
        else:
                return redirect('/')
def result(request,pnr,topic):
        if request.session.has_key('stud_loged'):
                correct = 0
                attemp = 0
                Result.objects.all().delete()
                if request.method == "POST":
                        ans = Assigments.objects.filter(topic=topic)
                        j=1
                        for i in ans:
                                a = request.POST.get("ans"+str(i.id))
                                if a != None:
                                        res = Result()
                                        res.topic = i.topic
                                        res.s_pnr = pnr
                                        res.que = i.que
                                        res.s_ans = a
                                        res.ans = i.ans
                                        res.save()
                                        attemp+=1
                                        print(a)
                                        print(i.ans.lower())
                                        if a.lower() == i.ans.lower():
                                                correct += 1
                                        print('j=',j)
                                        # res.save_base()
                                        j+=1
                                else:
                                        continue                
                        incorrect = attemp-correct
                s_res = Result.objects.filter(topic=topic)
                sa = SolvedAssignments()
                sa.s_pnr = pnr
                sa.topic = topic
                sa.attemp = attemp
                sa.correct = correct
                sa.s_name = Student.objects.get(s_pnr=pnr)
                sa.s_date = date.today()
                sa.save()
                return render(request,'student/result.html',{'marks':correct,'attemp':attemp,'incorrect':incorrect,'res':s_res})
        else:
                return redirect('/')

def logout(request):
    del request.session['stud_loged']
    return redirect('/')

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
