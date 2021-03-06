# Generated by Django 3.2.4 on 2021-06-11 21:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=100)),
                ('password', models.CharField(default='', max_length=100)),
            ],
            options={
                'db_table': 'admin',
            },
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cat_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Sub_Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcat_name', models.CharField(max_length=100)),
                ('category', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Admin.categories')),
            ],
            options={
                'db_table': 'sub_categories',
            },
        ),
    ]
