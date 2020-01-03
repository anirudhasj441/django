from django.db import models

# Create your models here.
class Attendence(models.Model):
    s_pnr = models.IntegerField(primary_key=True)
    s_name = models.CharField(max_length=50)
    s_class = models.CharField(max_length=50)
    month = models.CharField(max_length=50)
    att_per = models.FloatField()
    remark = models.CharField(max_length=50)
    def __str__(self):
        return self.s_name
        