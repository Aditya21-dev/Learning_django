from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name
    


class Payment(models.Model):
    amount = models.CharField(max_length=100)
    order_id = models.CharField(max_length=1000)
    razorpay_payment_id = models.CharField(max_length=1000, blank=True)
    paid = models.BooleanField(default=False)




class Order_Payment(models.Model):
    amount = models.IntegerField()  # paise me store karo (50000 = ₹500)
    order_id = models.CharField(max_length=255, unique=True)
    razorpay_payment_id = models.CharField(max_length=255, blank=True, null=True)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_id