from rest_framework import serializers
from penjualan.models import shoppingCart, wishlistCart
from api_rest.models import Produk
from django.contrib.auth.models import User


class serialProduk(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = "__all__"


class serialUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class serialCart(serializers.ModelSerializer):
    kode_produk = serialProduk()

    class Meta:
        model = shoppingCart
        fields = "__all__"


class serialWishlist(serializers.ModelSerializer):
    username_wishlist = serialUser()
    kode_produk_wishlist = serialProduk()

    class Meta:
        model = wishlistCart
        fields = "__all__"
