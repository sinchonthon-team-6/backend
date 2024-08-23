from django.shortcuts import render

from rest_framework.decorators import api_view
from .serializers import RentalFormSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import RentalForm

@api_view(['GET','POST'])
def get_create_rentalform(request):
    if request.method == 'POST':
        serializer = RentalFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
    else:
        query = request.GET.get('orderNumber',None)
        if query is None:
            return Response("주문번호가 필요합니다.", status=status.HTTP_400_BAD_REQUEST)
        rentalForm = RentalForm.objects.get(orderNumber=query)
        serializer = RentalFormSerializer(instance=rentalForm)
        return Response(serializer.data, status=status.HTTP_200_OK)