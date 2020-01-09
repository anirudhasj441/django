from django.shortcuts import render
from login.models import Teacher
# Create your views here.
def teacher(request,id):
    teacher = Teacher.objects.get(t_id=id)
    # return HttpResponse('<h1>Welcome '+str(teacher.t_name)+'</h1>')
    return render(request,'teacher/teacher.html',{'name':str(teacher.t_name)})
def addAssignment(request):
    return render(request,'teacher/assignment.html')