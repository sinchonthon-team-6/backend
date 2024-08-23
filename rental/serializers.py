from rest_framework import serializers
from .models import RentalForm
import secrets
import string
from django.core.mail import send_mail
from django.conf import settings

class RentalFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentalForm
        fields = ['id', 'userName', 'phoneNumber', 'startDate', 'finishDate', 'items', 'place', 'orderNumber','email']

    def create(self, validated_data):
        
        rental_form = RentalForm.objects.create(**validated_data)
        
        
        rental_form.orderNumber = self.generate_secure_random_string()
        rental_form.save()

        
        self.send_order_number_email(rental_form)

        return rental_form

    def generate_secure_random_string(self, length=8):
        characters = string.ascii_letters + string.digits
        return ''.join(secrets.choice(characters) for _ in range(length))

    def send_order_number_email(self, rental_form):
        subject = '대여 정보'
        message = (
            f"물품이 성공적으로 신청되었습니다., {rental_form.userName}님!\n\n"
            f"당신의 주문번호는 다음과 같습니다.: {rental_form.orderNumber}.\n\n"
            f"상세정보:\n여행목적지: {rental_form.place}\n"
            f"대여 시작 날짜: {rental_form.startDate}\n"
            f"대여 종료 날짜: {rental_form.finishDate}\n\n"
            f"즐거운 여행 되시길 바랍니다!"
        )
        recipient_list = [rental_form.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)