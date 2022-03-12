from django.contrib import admin
from .models import Ecommerce, ImagesCover, Category, Product
# Register your models here.

admin.site.register(Ecommerce)
admin.site.register(ImagesCover)
admin.site.register(Category)
admin.site.register(Product)


# class AttributesCategoryInline(admin.TabularInline):
#     model = AttributeProduct
#     extra = 1


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     inlines = [AttributesCategoryInline, ]
