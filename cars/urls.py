from django.urls import path
from . import views


urlpatterns = [
    path('cars', views.CarsAPIView.as_view()),
    path('cars/<int:pk>', views.CarAPIView.as_view()),
]
