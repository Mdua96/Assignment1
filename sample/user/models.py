from django.db import models

# Create your models here.

class user(models.Model):
    First_Name=models.CharField(max_length=30,default='1',primary_key=True)
    Last_Name = models.CharField(max_length=30)
    Email=models.EmailField
    Password=models.CharField(max_length=15)
    Username= models.CharField(max_length=15)

    def __str__(self):
        return self.First_Name

class post(models.Model):
    user=models.ForeignKey(user,default='1',on_delete=models.SET_DEFAULT)
    Text=models.TextField(max_length=100)
    Created_at=models.DateField()
    Updated_at=models.DateField()

