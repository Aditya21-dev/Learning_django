from django.db import models

# Create your models here.

class KFC_User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=15)