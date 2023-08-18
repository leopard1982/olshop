from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from api_rest.serializersnya import serialProduk
from api_rest.models import Produk
from django.db.models import Q

# Create your views here.
@api_view(['POST'])
def add_produk(request):
    if request.method == 'POST':
        serial = serialProduk(data=request.data)
        if serial.is_valid():
            serial.save()

    datanya = Produk.objects.all()
    serial = serialProduk(datanya,many=True)
    return Response(serial.data)

@api_view(['POST','GET'])
def get_produk(request):
    datanya = Produk.objects.all()
    if request.method == 'POST':
        datanya = datanya.filter(Q(produk_kode__icontains=request.POST['filter']) | Q(produk_nama__icontains=request.POST['filter']))

        serial = serialProduk(datanya,many=True)
        return Response(serial.data)
    else:
        return Response({'error':'Invalid'})

def view_produk(request):
    data = Produk.objects.all()
    context = {
        'data':data
    }
    return render(request, 'rest_api/aturItem.html',context)