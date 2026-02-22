from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

class Todo(models.Model):
    task = models.CharField()
    