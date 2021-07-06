from django.db import models


# Create your models here.
class admin_tbl(models.Model):
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=100, default='')

    class Meta:
        db_table = "admin"


class Categories(models.Model):
    admin = models.ForeignKey(admin_tbl, default='', on_delete=models.CASCADE)
    Cat_name = models.CharField(max_length=100)

    class Meta:
        db_table = "categories"


class Sub_Categories(models.Model):
    category = models.ForeignKey(Categories, default='', on_delete=models.CASCADE)
    subcat_name = models.CharField(max_length=100)

    class Meta:
        db_table = "sub_categories"
