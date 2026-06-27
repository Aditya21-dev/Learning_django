from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    password_1 = models.CharField(max_length=100)
    password_2 = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    department_code = models.CharField(max_length=40, unique=True)
    department_description = models.TextField(blank=True)
    department_head = models.CharField(max_length=100)

    def __str__(self):
        return self.department_name

class Employee(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=False)
    dob = models.DateField()
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
    


class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    query = models.TextField()
    status = models.CharField(max_length=20,default='Pending')
    admin_reply = models.TextField(blank=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.department}"
