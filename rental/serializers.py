from rest_framework import serializers
from .models import RentalForm

class RentalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalForm
        fields = ['id', 'userName', 'phoneNumber', 'startDate', 'finishDate', 'items', 'place', 'orderNumber']