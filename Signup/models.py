# Create your models here.
from django.db import models


class User_model(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=500, null=True )
    confirm_password=models.CharField(max_length=500 ,null=True)
    image = models.ImageField(upload_to="uploads", null=True, blank=True )
    user_type = models.CharField(max_length=100)

    class Meta:
        db_table = "users_tbl"


class Customer_model(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=500, null=True )
    confirm_password=models.CharField(max_length=500 ,null=True)
    image = models.ImageField(upload_to="uploads", null=True, blank=True)
    phone= models.CharField(max_length=20)
    user_type = models.CharField(max_length=100,default= '')

    class Meta:
        db_table = "customers_tbl"