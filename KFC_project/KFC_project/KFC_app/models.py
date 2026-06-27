from django.db import models

# Create your models here.

class KFC_User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
