from django.db import models
from django.conf import settings



class ImagesCover(models.Model):
    ecommerce = models.ForeignKey('Ecommerce', on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='covers/', verbose_name='cover')


class Category(models.Model):
    title = models.CharField(max_length=300, verbose_name="nombre")
    primaryCategory = models.BooleanField(default=False, verbose_name="Categoria primaria")

    def __str__(self):
        return self.title


class Product(models.Model):
    ecommerce = models.ForeignKey('Ecommerce', on_delete=models.CASCADE, verbose_name="Nombre de Tienda")
    name = models.CharField(max_length=300, verbose_name="Nombre de Producto")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name="Categoria")
    slug = models.SlugField()
    price = models.FloatField(verbose_name="Precio")
    discount_price = models.FloatField(blank=True, null=True,verbose_name="Precio con Descuento")
    preview_text = models.TextField(max_length=250, verbose_name='Texto Previo')
    detail_text = models.TextField(max_length=1000, verbose_name='Detalle de Producto')
    image_product = models.ImageField(upload_to='products/', blank=True, verbose_name="Imagen de producto")

    def __str__(self):
        return self.name


class Ecommerce(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='owner')
    name = models.CharField(max_length=250, verbose_name="Nombre de Tienda")
    logo = models.ImageField(upload_to='ecommerce_logo/',blank=False, verbose_name="Logo de Empresa")
    phone = models.CharField(max_length=250, verbose_name="Telefono")
    email = models.EmailField()
    descripcion = models.TextField(max_length=500, verbose_name="Descripción")

    def __str__(self):
        return self.name


# class AttributeProduct(models.Model):
#     product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Producto")
#     attribute = models.CharField(max_length=250, verbose_name="Atributo")
#     value = models.CharField(max_length=250, verbose_name="valor")

#     def __str__(self):
#         return f'{self.attribute} - {self.value}'
