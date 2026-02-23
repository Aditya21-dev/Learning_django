from django.db import models

# Create your models here.

from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    doctor_type = models.CharField(max_length=100) 
    doctor = models.CharField(max_length=100)
    date = models.DateField()
    problem = models.TextField()

    def __str__(self):
        return self.name