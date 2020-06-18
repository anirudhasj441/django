from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

class Workout(models.Model):
  date = models.DateField(null=True)
  Workout_for = models.CharField(max_length=30,null=True) 
  no_of_workout = models.IntegerField(null=True)
  no_of_set = models.IntegerField(null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,null =True)
  def __str__(self):
    return str(self.pk)
  class Meta:
    verbose_name_plural = 'Workout'
class Exercise(models.Model):
  exercise = models.CharField(max_length=30,null=True)
  repeatation = models.CharField(max_length=30,null=True)
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


class Bmr(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  bmr = models.CharField(max_length=30,null=True)
  date_filled = models.DateTimeField(default=timezone.now)

class Bmi(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  bmi = models.CharField(max_length=30,null=True)
  date_checked = models.DateTimeField(default=timezone.now)
