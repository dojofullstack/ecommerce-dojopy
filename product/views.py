from django.shortcuts import render
from .models import Product
from ordenes.models import Orden, OrdenProducto


def item_detail(request, slug):
    item = Product.objects.get(slug=slug)

    object_list = Product.objects.all()[:10]

    count_order = 0
    if not request.user.is_anonymous:
        order = Orden.objects.filter(user=request.user, orden_completa=False)
        if order:
            orden = order.first()
            #mis_ordenes = order.orden_producto.all()  # consulta inversa desde la tabla Orden
            mis_ordenes = OrdenProducto.objects.filter(orden=orden)
            for my_orden in mis_ordenes:
                stock = my_orden.stock
                count_order += stock

    ctx = {
            'item': item,
            'object_list': object_list,
            'count_order': count_order
            }
    return render(request, 'item.html', ctx)
