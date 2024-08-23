from rest_framework import serializers
from .models import RentalForm
import secrets
import string

class RentalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalForm
<<<<<<< HEAD
        fields = ['id', 'userName', 'phoneNumber', 'startDate', 'finishDate', 'items', 'orderNumber','email','price']
=======
        fields = ['id', 'userName', 'phoneNumber', 'startDate', 'finishDate', 'items', 'place', 'orderNumber','email']
>>>>>>> c8abbf7a8c967b8fb453e61d0be3605b20ba4fc8

    def create(self, validated_data):
        rental_form = RentalForm.objects.create(**validated_data)
        rental_form.orderNumber = self.generate_secure_random_string()
        rental_form.save()
        return rental_form

    def generate_secure_random_string(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))
