from django.shortcuts import render,redirect
from login.models import Teacher
from student.models import Assigments,AssignmentDate
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
            # in_question = request.POST.get("question")
            # in_a = request.POST.get("opt_a")
            # in_b = request.POST.get("opt_b")
            # in_c = request.POST.get("opt_c")
            # in_d = request.POST.get("opt_d")
            # in_ans = request.POST.get("ans")
            ass = AssignmentDate()
            ass.a_topic = in_topic
            ass.a_date = in_date
            ass.a_duedate = in_duedate
            # ass.que = in_question
            # ass.opt_a = in_a
            # ass.opt_b = in_b
            # ass.opt_c = in_c
            # ass.opt_d = in_d
            # ass.ans = in_ans
            # ass.techer = str(teacher.t_name)
            ass.save()
        except Exception:
            messages.error(request,'Question Not Set!')
        else:
            return redirect('/teacher/'+str(teacher.t_id)+'/addassignment/'+str(ass.a_topic))
    return render(request,'teacher/assignment.html')

def addQuetions(request,id,topic):
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