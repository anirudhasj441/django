from django.shortcuts import render,redirect
from login.models import Teacher,Student
from student.models import Assigments,AssignmentDate,SolvedAssignments
from django.contrib import messages
from datetime import date,timedelta
from django.contrib.sessions.models import Session
# Create your views here.
def teacher(request,id):
    if request.session.has_key('teacher_loged'):
        teacher = Teacher.objects.get(t_id=id)
        # return HttpResponse('<h1>Welcome '+str(teacher.t_name)+'</h1>')
        return render(request,'teacher/teacher.html',{'name':str(teacher.t_name)})
    else:
        return redirect('/')
def addAssignment(request,id):
    if request.session.has_key('teacher_loged'):
        teacher = Teacher.objects.get(t_id=id)
        top = AssignmentDate.objects.all()
        prev_topic=[]
        for topics in top:
            if topics.a_date>=date.today()-timedelta(days=1):
                print(topics.a_date)
                print(date.today()-timedelta(days=1))
                print('condition satisfy')
                prev_topic.append(topics.a_topic)
        if request.method == "POST":
            try:
                in_topic = request.POST.get("topic")
                in_date = request.POST.get("date")
                in_duedate = request.POST.get("duedate")
                ass = AssignmentDate()
                ass.a_topic = in_topic
                ass.a_date = in_date
                ass.a_duedate = in_duedate
                ass.save()
            except Exception:
                messages.error(request,'Question Not Set!')
            else:
                return redirect('/teacher/'+str(teacher.t_id)+'/addassignment/'+str(ass.a_topic))
        return render(request,'teacher/assignment.html',{'prev_topic':prev_topic})
    else:
        return redirect('/')

def addQuetions(request,id,topic):
    if request.session.has_key('teacher_loged'):
        teacher = Teacher.objects.get(t_id=id)
        assignment = AssignmentDate.objects.get(a_topic=topic)
        if request.method == "POST":
            try:
                in_question = request.POST.get("question")
                in_a = request.POST.get("opt_a")
                in_b = request.POST.get("opt_b")
                in_c = request.POST.get("opt_c")
                in_d = request.POST.get("opt_d")
                in_ans = request.POST.get("ans")
                ass = Assigments()
                ass.que = in_question
                ass.opt_a = in_a
                ass.opt_b = in_b
                ass.opt_c = in_c
                ass.opt_d = in_d
                ass.ans = in_ans
                ass.topic = assignment.a_topic
                ass.date = assignment.a_date
                ass.due_date = assignment.a_duedate
                ass.date_id = str(assignment.id)
                ass.techer = teacher.t_id
                ass.save()
            except Exception:
                messages.error(request,'Question Not Set!')
            else:
                messages.success(request,'Question set Succesfully!')
        return render(request,'teacher/addquestions.html')
    else:
        return redirect('/')

def assignmentStatus(request,id):
    if request.session.has_key('teacher_loged'):
        top = []
        topics = AssignmentDate.objects.all()
        for i in topics:
            if i.a_duedate>date.today()-timedelta(days=10):
                top.append(i)
        params = {
            'topics':top,
        }
        return render(request,'teacher/status.html',params)
    else:
        return redirect('/')

def status(request,id,topic):
    if request.session.has_key('teacher_loged'):
        names = []
        ass = AssignmentDate.objects.get(a_topic=topic)
        data = SolvedAssignments.objects.filter(topic=topic)
        for i in data:
            stud = Student.objects.get(s_pnr=i.s_pnr)
            names.append(stud)
        params = {
            'names':names,
            'ass':ass,
            'data':data,
            'active':True,
        }
        return render(request,'teacher/status.html',params)
    else:
        return redirect('/')


def logout(request):
    del request.session['teacher_loged']
    return redirect('/')