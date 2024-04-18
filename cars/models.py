from django.db import models


# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=60)
    mark = models.CharField(max_length=60)
    year = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.mark} {self.year} - {self.price}$"