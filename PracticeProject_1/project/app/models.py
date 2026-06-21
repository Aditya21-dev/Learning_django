from django.db import models

# Create your models here.

class User:
    u_name = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=254)
    password = models.CharField(max_length=5)
    contact = models.CharField(max_length=10)

    def __str__(self):
        return self.u_name