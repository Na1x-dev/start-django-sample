from django.shortcuts import render
from .models import Car, House
from rest_framework import generics, viewsets

from .serializer import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = CarSerializer

