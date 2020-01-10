from django.shortcuts import render
from login.models import Student
from .models import Assigments
# Create your views here.
def student(request,pnr):
        stud = Student.objects.get(s_pnr=pnr)
        # return HttpResponse("<h2>welcome "+str(stud.s_name)+"</h2>")
        return render(request,'student/student.html',{'pnr':pnr})

def assignment(request,pnr):
        assignments = Assigments.objects.all()
        for i in assignments:
                print(i.opt_a)
        return render(request,'student/assignment.html',{'assignments':assignments})