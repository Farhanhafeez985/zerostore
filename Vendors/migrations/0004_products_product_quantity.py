# Generated by Django 3.2.4 on 2021-06-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vendors', '0003_remove_products_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_quantity',
            field=models.IntegerField(default=0),
        ),
    ]