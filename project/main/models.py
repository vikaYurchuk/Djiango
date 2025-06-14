from django.db import models


# Create your models here.
class Product(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(blank=True, null=True, upload_to="main/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.PositiveIntegerField( blank=True, null=True)
    fuel_consumption = models.DecimalField(
        max_digits=4, decimal_places=1, verbose_name="Consumption (l/100km)", blank=True, null=True
    )
    color = models.CharField(max_length=50, verbose_name="Color", blank=True, null=True)

    def __str__(self):
        return self.model

    class Meta:
        ordering = ["model"]