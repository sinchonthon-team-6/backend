from django.db import models

class RentalForm(models.Model):
    userName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    startDate = models.DateField()
    finishDate = models.DateField()
    items = models.JSONField(default=dict)
    place = models.CharField(max_length=50)
    orderNumber = models.TextField(null=True, blank=True, unique=True)
    email = models.EmailField()