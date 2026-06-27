from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.CharField(max_length=10)
    city = models.CharField(max_length=45)
    def __str__(self):
        return self.name