# Generated by Django 5.1 on 2024-08-23 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_remove_rentalform_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='rentalform',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
