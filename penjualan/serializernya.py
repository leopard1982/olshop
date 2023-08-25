from rest_framework import serializers
from penjualan.models import shoppingCart
from api_rest.models import Produk

class serialProduk(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields = "__all__"

class serialCart(serializers.ModelSerializer):
    kode_produk = serialProduk()
    class Meta:
        model = shoppingCart
        fields = "__all__"