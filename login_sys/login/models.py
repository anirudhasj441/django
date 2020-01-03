from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(max_length = 50)
    passwd = models.CharField(max_length = 50)
    email = models.EmailField()
    class Meta:
        db_table = "users"
    