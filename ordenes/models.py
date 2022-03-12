from django.db import models
from django.conf import settings
from product.models import Product
# Create your models here.

class Orden(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    orden_completa = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user} {self.orden_completa}'


class OrdenProducto(models.Model):
    orden = models.ForeignKey('Orden', on_delete=models.CASCADE, related_name='orden_producto')
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.orden.user} {self.stock}'
