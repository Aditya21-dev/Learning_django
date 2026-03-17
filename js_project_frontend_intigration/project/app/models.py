from django.db import models

# Create your models here.

class Booking(models.Model):
    book_name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.TextField()
    phone_no = models.CharField(max_length=15)
    quantity = models.IntegerField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    