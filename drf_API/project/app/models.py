from django.db import models

# Create your models here.
class User(models.Model):
    name = models.TextField()
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    city = models.TextField()
    