from django.db import models

# Create your models here.
class Student(models.Model):
    s_pnr = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    s_passwd = models.CharField(max_length=300,default="")
    s_roll = models.IntegerField()
    s_class = models.CharField(max_length=50)
    s_contact = models.IntegerField()
    s_email = models.EmailField()
    def __str__(self):
        return self.s_name

class Teacher(models.Model):
    t_id = models.IntegerField(primary_key=True)
    t_name = models.CharField(max_length=50)
    t_passwd = models.CharField(max_length=300,default="")
    def __str__(self):
        return self.t_name


