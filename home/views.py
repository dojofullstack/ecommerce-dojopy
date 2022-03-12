from django.shortcuts import render
from product.models import Product, Category, Ecommerce, ImagesCover
from ordenes.models import Orden, OrdenProducto


def home(request):
    ecommerce = Ecommerce.objects.get(name='dojopy')
    categories = Category.objects.all()
    object_list = Product.objects.all()
    imges_cover = ImagesCover.objects.filter(ecommerce=ecommerce.id)

    count_order = 0
    if not request.user.is_anonymous:
        order = Orden.objects.filter(user=request.user, orden_completa=False)
        if order:
            orden = order.first()
            # mis_ordenes = order.orden_producto.all()  # consulta inversa desde la tabla Orden
            mis_ordenes = OrdenProducto.objects.filter(orden=orden)
            for my_orden in mis_ordenes:
                stock = my_orden.stock
                count_order += stock

    context = {
        'user': request.user,
        'ecommerce': ecommerce,
        'categories': categories,
        'object_list': object_list,
        'imges_cover': imges_cover,
        'count_order': count_order
    }
    print(ecommerce.name)
    return render(request, 'home.html', context)
