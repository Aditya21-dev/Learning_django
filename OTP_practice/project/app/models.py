from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length=15)

    def __str__(self):
        return self.name