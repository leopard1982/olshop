from rest_framework import serializers
from penjualan.models import shoppingCart

class serialCart(serializers.ModelSerializer):
    class Meta:
        model = shoppingCart
        fields = "__all__"