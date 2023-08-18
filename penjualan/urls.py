from django.urls import path
from penjualan.views import dashboard, add_cart

urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('add/cart/',add_cart,name='add_cart'),
]
