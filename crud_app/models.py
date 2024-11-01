from django.db import models

# Create your models here.

class Info(models.Model):
    Name=models.CharField(max_length=50,default="")
    Age=models.IntegerField(default="")
    Contact=models.IntegerField(default="")
    Mail=models.CharField(max_length=50,default="")
    
