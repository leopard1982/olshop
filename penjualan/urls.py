from django.urls import path
from penjualan.views import dashboard, add_cart, get_cart, setWishlist, jumlahWishlist, get_jumlah, get_harga_barang
from penjualan.views import get_cart_satu

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/cart/', add_cart, name='add_cart'),
    path('get/cart/', get_cart, name='get_cart'),
    path('get/cart/jumlah/', get_jumlah, name="get_jumlah"),
    path('wishlist/', setWishlist, name='set_wishlist'),
    path('wishlist/jumlah/', jumlahWishlist, name='jumlah_wishlist'),
    path('get/barang/harga/', get_harga_barang, name='get_harga_barang'),
    path('get/cart/satu/', get_cart_satu, name='get_cart_satu')
]
