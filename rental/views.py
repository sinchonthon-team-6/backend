from django.dispatch import receiver
from django.shortcuts import render

from rest_framework.decorators import api_view
from django.db.models.signals import post_save

from .serializers import RentalFormSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import RentalForm
from django.core.mail import send_mail
from django.conf import settings

@api_view(['GET','POST','DELETE'])
def get_create_rentalform(request):
    if request.method == 'POST':
        serializer = RentalFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        query = request.GET.get('orderNumber',None)
        if query is None:
            return Response("주문번호가 필요합니다.", status=status.HTTP_400_BAD_REQUEST)
        rentalForm = RentalForm.objects.get(orderNumber=query)
        serializer = RentalFormSerializer(instance=rentalForm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        query = request.GET.get('orderNumber',None)
        if query is None:
            return Response("주문번호가 필요합니다.", status=status.HTTP_400_BAD_REQUEST)
        RentalForm.objects.get(orderNumber=query).delete()
        return Response('해당하는 대여 신청이 삭제되었습니다.',status=status.HTTP_204_NO_CONTENT)
<<<<<<< HEAD
=======

<<<<<<< HEAD
    
>>>>>>> c8abbf7a8c967b8fb453e61d0be3605b20ba4fc8
=======

    
>>>>>>> c475940c9052cbc3590b403851ba38afd5f49594
