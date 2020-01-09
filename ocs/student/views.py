from django.shortcuts import render
from login.models import Student
# Create your views here.
def student(request,pnr):
        stud = Student.objects.get(s_pnr=pnr)
        # return HttpResponse("<h2>welcome "+str(stud.s_name)+"</h2>")
        return render(request,'student/student.html',{'name':str(stud.s_name)})