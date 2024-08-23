# Generated by Django 5.1 on 2024-08-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RentalForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('phoneNumber', models.CharField(max_length=50)),
                ('startDate', models.DateField()),
                ('finishDate', models.DateField()),
                ('items', models.JSONField(default=list)),
                ('place', models.CharField(max_length=50)),
                ('orderNumber', models.TextField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
