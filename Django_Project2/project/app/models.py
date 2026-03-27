from django.db import models

# Create your models here.

class Dishes(models.Model):
    name = models.CharField()
    image = models.ImageField() 
    price = models.CharField()
    type = models.BooleanField()