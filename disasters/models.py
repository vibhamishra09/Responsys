from django.db import models
from django.contrib.auth.models import User
class About(models.Model):
     
     disaster_name = models.CharField(max_length=122)
     date_disaster= models.CharField(max_length=122)
     dead=models.CharField(max_length=1299)
     injured = models.CharField(max_length=122)
     heading= models.CharField(max_length=1220)
     description=models.CharField(max_length=12000)
     category = models.CharField(max_length=122)
class User(models.Model):
     user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True)  
     userid = models.CharField(max_length=122)
     password= models.CharField(max_length=122)
def __str__(self):
        return self.name
# Create your models here.
