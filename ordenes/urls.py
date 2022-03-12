from django.urls import path
from .views import OrdenAgregar, ResumeOrder


urlpatterns = [
        path('agregar/', OrdenAgregar.as_view(), name='order-add'),
        path('resume/', ResumeOrder.as_view(), name='order-add'),
    ]