# Generated by Django 3.2.4 on 2021-06-11 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0002_customer_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_model',
            name='user_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
