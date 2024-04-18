from django.shortcuts import render
from .models import Car
from rest_framework import generics

from .serializer import CarSerializer


class CarsAPIView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
