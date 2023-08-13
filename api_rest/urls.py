from django.urls import path
from api_rest.views import add_produk, get_produk

urlpatterns = [
    path('add/produk/', add_produk,name='add_produk'),
    path('get/produk/', get_produk,name='get_produk'),
]
