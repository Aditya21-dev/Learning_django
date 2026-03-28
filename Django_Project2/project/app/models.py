from django.db import models

# Create your models here.

class Dishes(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField()
    type = models.CharField()

    def __str__(self):
        return self.name



class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name