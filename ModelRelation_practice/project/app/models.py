from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    building = models.CharField(max_length=100)
    hod_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    department = models.OneToOneField(Department,on_delete=models.CASCADE,related_name="teachers")

    def __str__(self):
        return self.name
    
    

class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
    

class Order(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    order_date = models.DateField()
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,related_name="orders")

    def __str__(self):
        return self.product_name