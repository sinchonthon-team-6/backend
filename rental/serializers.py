from rest_framework import serializers
from .models import RentalForm
import secrets
import string

class RentalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalForm
        fields = ['id', 'userName', 'phoneNumber', 'startDate', 'finishDate', 'items', 'place', 'orderNumber']

    def create(self, validated_data):
        rental_form = RentalForm.objects.create(**validated_data)
        rental_form.orderNumber = self.generate_secure_random_string()
        rental_form.save()
        return rental_form

    def generate_secure_random_string(self, length=8):
        characters = string.ascii_letters + string.digits
<<<<<<< HEAD
        return ''.join(secrets.choice(characters) for _ in range(length))
    
=======
        return ''.join(secrets.choice(characters) for _ in range(length))
>>>>>>> 3a83a1df5a874b8bde619f1e2be141ad1bd723e2
