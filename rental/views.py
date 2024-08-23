from django.shortcuts import render

from rest_framework.decorators import api_view
from .serializers import RentalFormSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def create_rentalform(request):
    serializer = RentalFormSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response("Invalid Data", status=status.HTTP_400_BAD_REQUEST)
