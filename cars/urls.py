from django.urls import path, include
from . import views
from rest_framework import routers
from .views import CarViewSet, HouseViewSet

router = routers.DefaultRouter()
router.register('cars', CarViewSet)
router.register('houses', HouseViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]
