# Generated by Django 3.2.4 on 2021-06-17 07:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0003_auto_20210617_1034'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order_details',
            old_name='products',
            new_name='order',
        ),
    ]
