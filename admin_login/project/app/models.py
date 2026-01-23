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