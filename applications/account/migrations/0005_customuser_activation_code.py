# Generated by Django 4.1.5 on 2023-01-23 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_customuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activation_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]