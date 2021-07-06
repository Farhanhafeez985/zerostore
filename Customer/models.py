from django.db import models

from Signup.models import Customer_model, User_model
from Vendors.models import Products


# Create your models here.

class Wishlist(models.Model):
    user = models.ForeignKey(Customer_model, on_delete=models.CASCADE)
    item = models.ManyToManyField(Products)

    class Meta:
        db_table = "Wishlist_tbl"

class Comments(models.Model):
    user = models.ForeignKey(Customer_model, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    comment=models.CharField(max_length=250,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)


    class Meta:
        db_table = "Comments_tbl"
