from django.db import models

class RentalForm(models.Model):
    userName = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    startDate = models.DateField()
    finishDate = models.DateField()
    items = models.JSONField(default=dict)
<<<<<<< HEAD
    orderNumber = models.TextField(null=True, blank=True, unique=True)
    email = models.EmailField(null=True)
    price = models.IntegerField(null=True)
=======
    place = models.CharField(max_length=50)
    orderNumber = models.TextField(null=True, blank=True, unique=True)
    email = models.EmailField()
>>>>>>> c8abbf7a8c967b8fb453e61d0be3605b20ba4fc8
