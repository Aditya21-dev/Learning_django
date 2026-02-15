from django.db import models

# Create your models here.
class Aadhaar(models.Model):
    aadhaar_number = models.CharField(max_length=12, unique=True)
    created_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.aadhaar_number
 

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    aadhaar = models.OneToOneField(Aadhaar,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name