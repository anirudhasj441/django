from django.db import models
from ocs.settings import DATE_INPUT_FORMATS
from datetime import date

# Create your models here.
class AssignmentDate(models.Model):
    a_date = models.DateField()
    a_duedate = models.DateField()
    a_topic = models.CharField(max_length=50)


class Assigments(models.Model):
    topic = models.CharField(max_length=50,default="")
    date = models.DateField(null=True,blank=True)
    due_date = models.DateField(null=True,blank=True)
    que = models.CharField(max_length=100)
    opt_a = models.CharField(max_length=50)
    opt_b = models.CharField(max_length=50)
    opt_c = models.CharField(max_length=50)
    opt_d = models.CharField(max_length=50)
    ans = models.CharField(max_length=50)
    techer = models.CharField(max_length=50)
    date_id = models.IntegerField(null =True)
    def __str__(self):
        return str(self.que)