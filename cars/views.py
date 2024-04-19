from django.shortcuts import render
from .models import Car, House
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from . permissions import AllForAdminOtherReadOnlyPermission


from .serializer import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllForAdminOtherReadOnlyPermission, )


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = CarSerializer

