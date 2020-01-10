from django.shortcuts import render
from login.models import Teacher
from student.models import Assigments
from django.contrib import messages
# Create your views here.
def teacher(request,id):
    teacher = Teacher.objects.get(t_id=id)
    # return HttpResponse('<h1>Welcome '+str(teacher.t_name)+'</h1>')
    return render(request,'teacher/teacher.html',{'name':str(teacher.t_name)})
def addAssignment(request,id):
    teacher = Teacher.objects.get(t_id=id)
    if request.method == "POST":
        try:
            in_topic = request.POST.get("topic")
            in_date = request.POST.get("date")
            in_duedate = request.POST.get("duedate")
            in_question = request.POST.get("question")
            in_a = request.POST.get("opt_a")
            in_b = request.POST.get("opt_b")
            in_c = request.POST.get("opt_c")
            in_d = request.POST.get("opt_d")
            in_ans = request.POST.get("ans")
            ass = Assigments()
            ass.topic = in_topic
            ass.date = in_date
            ass.due_date = in_duedate
            ass.que = in_question
            ass.opt_a = in_a
            ass.opt_b = in_b
            ass.opt_c = in_c
            ass.opt_d = in_d
            ass.ans = in_ans
            ass.techer = str(teacher.t_name)
            ass.save()
        except Exception:
            messages.error(request,'Question Not Set!')
        else:
            messages.success(request,'Question set! Succesfully')
    return render(request,'teacher/assignment.html')