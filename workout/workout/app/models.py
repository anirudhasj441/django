from django.db import models

# Create your models here.

class Workout(models.Model):
  date = models.DateField(null=True)
  Workout_for = models.CharField(max_length=30,null=True) 
  no_of_workout = models.IntegerField(null=True)
  no_of_set = models.IntegerField(null=True)
  def __str__(self):
    return str(self.pk)
  class Meta:
    verbose_name_plural = 'Workout'
class Exercise(models.Model):
  exercise = models.CharField(max_length=30,null=True)
  repeatation = models.CharField(max_length=30,null=True)
  workout = models.ForeignKey(Workout, on_delete=models.CASCADE)