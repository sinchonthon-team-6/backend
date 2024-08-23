from django.db import models

class RentalForm(models.Model):
    userName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    startDate = models.DateField()
    finishDate = models.DateField()
<<<<<<< HEAD
    items = models.JSONField(default=list)
=======
    items = models.JSONField(default=dict)
>>>>>>> 8d4c58b0826196837cd5e3ffd99bdd84d7572f38
    place = models.CharField(max_length=50)
    orderNumber = models.TextField(null=True, blank=True, unique=True)