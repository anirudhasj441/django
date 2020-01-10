from django.db import models

# Create your models here.
class Assigments(models.Model):
    topic = models.CharField(max_length=50,default="")
    date = models.DateField()
    due_date = models.DateField()
    que = models.CharField(max_length=100)
    opt_a = models.CharField(max_length=50)
    opt_b = models.CharField(max_length=50)
    opt_c = models.CharField(max_length=50)
    opt_d = models.CharField(max_length=50)
    ans = models.CharField(max_length=50)
    techer = models.CharField(max_length=50)
    def __str__(self):
        return str(self.date)