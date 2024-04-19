import django_filters.rest_framework
from django.shortcuts import render
from .models import Car, House
from rest_framework import generics, viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from . permissions import AllForAdminOtherReadOnlyPermission


from .serializer import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (AllForAdminOtherReadOnlyPermission, )
    filter_backends = [filters.SearchFilter]
    # filter_backends = [filters.OrderingFilter]
    search_fields = ['brand']


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = CarSerializer

