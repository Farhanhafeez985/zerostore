import datetime

from django.db import models

# Create your models here.
from Signup.models import Customer_model
from Vendors.models import Products,Store


class Order(models.Model):

    customer=models.ForeignKey(Customer_model,on_delete=models.CASCADE)
    total_price=models.IntegerField(default=1)
    address=models.CharField(max_length=200,default='')
    phone=models.CharField(max_length=20,default='')
    date=models.DateField(default=datetime.datetime.today)
    postcode=models.CharField(default='',max_length=15)
    city=models.CharField(max_length=30, default='')
    Order_id=models.BigIntegerField(default=1)

    def placeorder(self):
        self.save()
    class Meta:
        db_table = "Order_tbl"

class Order_details(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,default='')
    order=models.ForeignKey(Order,on_delete=models.CASCADE,default='')
    store=models.ForeignKey(Store,on_delete=models.CASCADE,default='')
    quantity=models.IntegerField(default=1)
    price=models.IntegerField(default=1)
    status=models.CharField(max_length=50,default='Order is not Confirmed Yet.')

    class Meta:
        db_table = "Order_details_tbl"