from django.contrib import admin
from .models import Orden, OrdenProducto
# Register your models here.

admin.site.register(Orden)
admin.site.register(OrdenProducto)