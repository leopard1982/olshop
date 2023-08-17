from rest_framework import serializers
from administrasi.models import Kota, Kecamatan

class serialKota(serializers.ModelSerializer):
    class Meta:
        model = Kota
        fields = "__all__"

class serialKecamatan(serializers.ModelSerializer):
    class Meta:
        model = Kecamatan
        fields = "__all__"