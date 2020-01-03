from django.db import models

# Create your models here.
class Assigments(models.Model):
    topic = models.CharField(max_length=50,default="")
    date = models.DateField()
    due_date = models.DateField()
    task = models.CharField(max_length=100)
    def __str__(self):
        return self.date
