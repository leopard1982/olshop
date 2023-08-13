from rest_framework import serializers
from api_rest.models import Produk

class serialProduk(serializers.ModelSerializer):
    class Meta:
        model = Produk
        fields= "__all__"