from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from product.views import item_detail
# from order.views import OrderSummary, OrderAdd
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    url(r'^accounts/', include('allauth.urls')),
    path('product/<slug>/', item_detail, name='item_detail'),
    path('orden/', include('ordenes.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
