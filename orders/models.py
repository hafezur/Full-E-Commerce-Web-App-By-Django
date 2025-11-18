from django.db import models
from django.contrib.auth.models import User
from store.models import Product
from category.models import Category
from accounts.models import Account
# Create your models here.

class Payment(models.Model):
    user=models.ForeignKey(Account,on_delete=models.CASCADE) # any one User had multiple payment
    payment_id=models.CharField(max_length=100)
    payment_method=models.CharField(max_length=100)
    amount_paid=models.IntegerField()
    status=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
class Order(models.Model):
    STATUS=(
        ('New','New'),
        ('Accepted','Accepted'),
        ('Completed','Completed'),
        ('Cancelled','Cancelled'),

    )
    id = models.AutoField(primary_key=True)
    user=models.ForeignKey(Account,on_delete=models.CASCADE)
    #order_number=models.CharField(max_length=30) # before
    order_number=models.IntegerField(null=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    phone=models.CharField(max_length=12)
    email=models.EmailField(max_length=50)
    find_product_name=models.JSONField(default=list)
    address_line1=models.CharField(max_length=150)
    address_line2=models.CharField(max_length=150)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    order_note=models.CharField(max_length=100)
    order_total=models.FloatField(null=True)
    tax=models.FloatField( null=True )
    status=models.CharField(max_length=15, choices=STATUS, default='New')
    ip=models.CharField(max_length=100, blank=True, null=True)
    is_ordered=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

class OrderedProduct(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE)
    user=models.ForeignKey(Account, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    ordered=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True)
    
class PaymentGateWaySettings(models.Model):
    store_id = models.CharField(max_length=500, blank=True, null=True)
    store_pass = models.CharField(max_length=500, blank=True, null = True)