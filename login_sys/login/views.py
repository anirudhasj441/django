from django.shortcuts import render,redirect
from login.forms import UserForm
from login.models import User
from django.http import HttpResponse
# Create your views here.
def register(request):
    if request.method  == "POST":
        # form = UserForm(request.POST)
        # if form.is_valid():
        #     try:
        #         form.save()
        #         return redirect()
        #     except:
        #         pass
        try:
            uname = request.POST.get("uname")
            email = request.POST.get("email")
            passwd = request.POST.get("passwd")
            com_passwd = request.POST.get("com_passwd")
            user = User()
            if passwd!=com_passwd:
                raise Exception
            else:
                user.uname = uname
                user.passwd = passwd
                user.email = email
                user.save()
        except:
            return redirect("/register")
        else:
            return HttpResponse("data entered!")

    return render(request,'register.html',{})
def login(request):
    is_login = True
    if request.method=="POST":
        try:
            uname = request.POST.get("uname")
            passwd = request.POST.get("passwd")
            print(uname)
            user = User.objects.all()
            uid = 0
            for i in user:
                print(i.uname)
                if uname == i.uname:
                    uid = i.id
                else:
                    continue
            
            # sv_passwd = User.objects.get(id=uid)
            if uid==0:
                raise Exception
            else:
                sv_user = User.objects.get(id=uid)
            if sv_user.passwd != passwd:
                raise Exception
        except:
            is_login = False
            return redirect("/login")
            # return HttpResponse('''<script>alert('username or password is wrong')</script>''')
        else:
            return HttpResponse("<h1>login succesfull!</h1>")
    return render(request,'login.html',{'is_login':is_login})
