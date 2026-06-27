from django.db import models

# Create your models here.

role=(('admin','admin'),('staff','staff'),('user','user'))

class Employee(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    department=models.CharField(max_length=20)
    role=models.CharField(max_length=20,choices=role)
    password = models.CharField(max_length=20,null=True)