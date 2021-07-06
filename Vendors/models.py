from django.db import models

from Admin.models import Categories ,Sub_Categories
from Signup.models import User_model,Customer_model


# Create your models here.
class Store(models.Model):
    user = models.OneToOneField(User_model, default='', on_delete=models.CASCADE)
    store_Name = models.CharField(max_length=50, unique='True')
    ntn = models.CharField(max_length=20)
    store_image = models.ImageField(upload_to="uploads", null=True, blank=True)

    class Meta:
        db_table = "Stores_tbl"


class Products(models.Model):
    category = models.ForeignKey(Categories, default='', on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Sub_Categories, default='', on_delete=models.CASCADE)
    store = models.ForeignKey(Store, default='', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=1)
    discount_price=models.IntegerField(default=1)
    product_quantity = models.IntegerField(default=0)
    product_status = models.CharField(max_length=50, default=1)
    product_description = models.CharField(max_length=200, null=True, default='NO Description Available')
    product_image = models.ImageField(upload_to="uploads", null=True, blank=True)

    class Meta:
        db_table = "Products_tbl"
    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.filter(id__in=ids)
