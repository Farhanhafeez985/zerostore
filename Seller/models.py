from django.db import models

# Create your models here.
from Admin.models import Categories, Sub_Categories
from Signup.models import User_model

class Used_Products(models.Model):
    user=models.ForeignKey(User_model,default='',on_delete=models.CASCADE,)
    category = models.ForeignKey(Categories, default='', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sub_Categories, default='', on_delete=models.CASCADE,null=True)
    ad_title = models.CharField(max_length=50)
    ad_price = models.IntegerField(default=1)
    ad_condition = models.CharField(max_length=50, default='')
    ad_description = models.CharField(max_length=200, null=True, default='')
    ad_image = models.ImageField(upload_to="uploads", null=True, blank=True ,default='uploads/default.jpg')
    ad_location=models.CharField(max_length=50)
    ad_phone =models.CharField(max_length=20, default= '')

    class Meta:
        db_table = "used_products_tbl"