# Generated by Django 4.1.5 on 2023-01-17 14:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='amount',
        ),
    ]