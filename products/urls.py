
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
    path('', views.index,name='home'),
    path('product_list',views.list_products,name='list_product'),
    path('detail_product/<pk>',views.detail_products,name='detail_product')

]

