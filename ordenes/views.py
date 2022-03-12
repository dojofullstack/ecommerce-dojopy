from django.shortcuts import render ,redirect
from django.views.generic import  View
from .models import Orden , OrdenProducto


class OrdenAgregar(View):
    def post(self, request):
        data = request.POST
        stock = data.get('stock')[0]
        product_id = data.get('product_id')[0]
        product_slug = data.get('product_slug')
        user = request.user

        if user.is_anonymous:
            return redirect('/accounts/login/')

        # guardar datos en la tabla Ordenes
        obj_orden, created = Orden.objects.get_or_create(user=user, orden_completa=False)

        OrdenProducto.objects.create(
            orden=obj_orden,
            item_id=product_id,
            stock=stock
        )


        return redirect('item_detail', product_slug)


class ResumeOrder(View):
    def get(self, request):
        # data = request.POST
        # stock = data.get('stock')[0]
        # product_id = data.get('product_id')[0]
        # product_slug = data.get('product_slug')
        # user = request.user

        # if user.is_anonymous:
        #     return redirect('/accounts/login/')

        # # guardar datos en la tabla Ordenes
        # obj_orden, created = Orden.objects.get_or_create(user=user, orden_completa=False)

        # OrdenProducto.objects.create(
        #     orden=obj_orden,
        #     item_id=product_id,
        #     stock=stock
        # )

        return render(request, 'order_summary.html')