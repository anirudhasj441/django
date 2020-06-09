from django.shortcuts import render,redirect
from .models import Workout,Exercise
from django import template

register = template.Library()
@register.filter
def index(list, index):
    return list[index]

# Create your views here.
def index(request):
  return render(request,'app/index.html')
  
def addWorkout(request):
  if request.method == "POST":
    dt = request.POST.get('date')
    print('date=',dt)
    wf = request.POST.get('workout')
    ne = request.POST.get('no_of_exercise')
    ns = request.POST.get('no_of_set')
    workout = Workout.objects.create(date=dt,Workout_for=wf,no_of_workout=ne,no_of_set=ns)
  return redirect('/add_exercise/'+str(workout.pk))
  
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
    return render(request,'app/add_exersice.html',params)
  
def dispData(request):
  workout = Workout.objects.all().order_by("-date")
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