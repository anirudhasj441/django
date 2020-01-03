from django.db import models

# Create your models here.
class Result(models.Model):
    seat_no = models.CharField(max_length=50,primary_key=True)
    s_name = models.CharField(max_length=50)
    s_class = models.CharField(max_length=50)
    s_per = models.FloatField()
    def __str__(self):
        return self.seat_no