from django.db import models
from datetime import date 
# Create your models here.
class Student(models.Model):
    # s_id = models.AutoField(primary_key=True,default="1")
    s_pnr = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    s_dob = models.DateField(null=True,blank=True)
    s_gender = models.CharField(max_length=50,default="")
    s_passwd = models.CharField(max_length=300)
    s_roll = models.IntegerField()
    s_class = models.CharField(max_length=50)
    s_contact = models.IntegerField()
    s_email = models.EmailField()
    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    t_id = models.AutoField(primary_key=True)
    tnr = models.IntegerField()
    t_name = models.CharField(max_length=50)
    t_dob = models.DateField(null=True,blank=True)
    t_email = models.EmailField(default="")
    t_cont = models.IntegerField(null=True)
    t_passwd = models.CharField(max_length=300)
    def __str__(self):
        return self.t_name