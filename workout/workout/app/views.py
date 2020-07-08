from django.shortcuts import render,redirect
from app.models import Workout,Exercise,Bmi,Bmr
from django import template
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib import messages
from django.utils import timezone,dateformat
from datetime import datetime
#Exceptions 
class PasswordNotMatch(Exception):
  pass
class EmptyUserName(Exception):
  pass
# Create your views here.
def index(request):
  return render(request,'app/index.html')
  
def addWorkout(request):
  if request.user.is_authenticated:
    if request.method == "POST":
      dt = request.POST.get('date')
      print('date=',dt)
      wf = request.POST.get('workout')
      ne = request.POST.get('no_of_exercise')
      ns = request.POST.get('no_of_set')
      workout = Workout.objects.create(date=dt,Workout_for=wf,no_of_workout=ne,no_of_set=ns,user=request.user)
      return redirect('/add_exercise/'+str(workout.pk))
  else:
    messages.warning(request,'Please Log In to Add Workout')
    return redirect('/')
  return render(request,'app/add.html')
  
def addExersice(request,id):
  try:
    workout = Workout.objects.get(pk=id)
  except Workout.DoesNotExist:
    return redirect('/disp')
  else:
    ex =[]
    rep = []
    params = {
      'workouts':workout,
      'range' : range(1,int(workout.no_of_workout)+1)
    }
    if request.method == "POST":
      for i in range(1,int(workout.no_of_workout)+1):
        ex.append(request.POST['exersice'+str(i)])
        rep.append(request.POST['repeatation'+str(i)])
      for i in range(len(ex)):
        exersice = Exercise.objects.create(exercise = ex[i],repeatation = rep[i],workout = workout)
      return redirect('index')
    else:
      Workout.objects.get(pk=id).delete()
    return render(request,'app/add_exersice.html',params)
  
def dispData(request):
  if request.user.is_authenticated:
    workout = Workout.objects.filter(user=request.user).order_by("-date")
    ex = []
    for i in workout:
      ex.append( Exercise.objects.filter(workout=i))
    print(type(ex))
    params = {
      'workouts':workout,
      'exersices':ex,
      'range': range(1,len(ex)+1)
    }
    return render(request,'app/disp.html',params)
  else:
    messages.warning(request,'Please Log in')
    return redirect('/')
  
def updateData(request,id):
  try:
    workout = Workout.objects.get(pk=id)
  except Workout.DoesNotExist:
    return redirect('/disp')
  else:
    params = {
      'workout':workout,
    }
    if request.method == "POST":
      dt = request.POST.get('date')
      print('date=',dt)
      wf = request.POST.get('workout')
      ne = request.POST.get('no_of_exercise')
      ns = request.POST.get('no_of_set')
      workout.date = dt
      workout.Workout_for = wf
      workout.no_of_workout = ne
      workout.no_of_set = ns
      workout.save()
      return redirect('/update_exersice/'+str(workout.pk))
  return render(request,'app/update.html',params)
  
def updateExersice(request,id):
  workout = Workout.objects.get(pk=id)
  exersices = Exercise.objects.filter(workout=workout)
  ex =[]
  rep = []
  params = {
    'workouts':workout,
    'range' : range(1,int(workout.no_of_workout)+1)
  }
  if request.method == "POST":
    exersices.delete()
    for i in range(1,int(workout.no_of_workout)+1):
      ex.append(request.POST['exersice'+str(i)])
      rep.append(request.POST['repeatation'+str(i)])
    print(ex)
    print(rep)
    for i in range(len(ex)):
      exersice = Exercise.objects.create(exercise = ex[i],repeatation = rep[i],workout = workout)
    return redirect('disp')
  return render(request,'app/add_exersice.html',params)


def delete(request,id):
  workout = Workout.objects.get(pk=id)
  workout.delete()
  return redirect('/disp')

def userLogin(request):
  if request.user.is_authenticated:
    return redirect('/')
  else:
    if request.method == "POST":
      uname = request.POST['uname']
      passwd = request.POST['passwd']
      user = authenticate(username=uname,password=passwd)
      if user is not None:
        login(request,user)
        messages.success(request,"Welcome "+request.user.first_name+" "+request.user.last_name)
        return redirect('/')
      else:
        messages.error(request,"Invalid Credentials")

  return render(request,'app/login.html')

def userLogout(request):
  logout(request)
  return redirect('/')

def userSingup(request):
  if request.user.is_authenticated:
    return redirect('/')
  else:
    if request.method == "POST":
      fname = request.POST['first_name']
      lname = request.POST['last_name']
      uname = request.POST['uname']
      email = request.POST['email']
      passwd = request.POST['passwd']
      con_passwd = request.POST['con_passwd']
      try:
        if passwd != con_passwd:
          raise PasswordNotMatch 
        if len(uname.replace(" ",""))==0:
          raise EmptyUserName
        user = User.objects.create_user(username=uname,email=email,password=passwd,first_name=fname,last_name=lname)
      except PasswordNotMatch:
        messages.error(request,"Password and Confirm Password should be same")
      except EmptyUserName:
        messages.error(request,"User name should not be empty")
      except IntegrityError:
        messages.error(request,'Username Already Exists')
      else:
        messages.success(request,'Registration Succesfully done')
  return render(request,'app/register.html')

def bmrCalculator(request):
  return render(request,"app/bmr.html")

def bmrSubmit(request):
  bmr = request.GET["bmr"]
  try:
    user_bmr = Bmr.objects.get(user=request.user)
    user_bmr.bmr = bmr
    user_bmr.date_filled = str(timezone.now())
    user_bmr.save()
  except user_bmr.DoesNotExist:
    Bmr.objects.create(user=request.user,bmr=bmr)
  return redirect('/bmr_calculator')

def bmiCalculator(request):
  return render(request,"app/bmi.html")

def bmiSubmit(request):
  bmi = request.GET["bmi"]
  Bmi.objects.create(user=request.user,bmi=bmi)
  return redirect('/bmi_calculator')

def stopwatch(request):

  return render(request,"app/stopwatch.html")