from django.db import models
import hashlib

# Create your models here.
class POLICE_LOGIN(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    district=models.CharField(max_length=100,null=True)
    state=models.CharField(max_length=100,null=True)