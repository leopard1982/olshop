from django.shortcuts import render
from administrasi.forms import formUsers
from administrasi.forms import formUserInformations
from administrasi.models import UserInformations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from penjualan.models import shoppingCart
from django.contrib.auth.models import User
from api_rest.models import Produk
from django.db.models import F, Count

# Create your views here.
def dashboard(request):
    form = formUsers()
    form_user_informasi = formUserInformations()
    try:
        data_info = UserInformations.objects.get(user_id=request.user.username)
    except:
        data_info = None

    context = {
        'form':form,
        'data_info':data_info,
        'form_user_informasi':form_user_informasi
    }
    return render(request,'penjualan/dashboard.html',context)

@api_view(["POST"])
def add_cart (request):
    if request.method == 'POST':
            kode_barang = request.data['kode_barang']
            jumlah_barang = request.data['jumlah_barang']
        
            data = shoppingCart.objects.all().filter(username_cart = User.objects.get(username=request.user.username),kode_produk=Produk.objects.get(produk_kode=kode_barang))
            if(data.count()>0):
                shoppingCart.objects.all().filter(username_cart = User.objects.get(username=request.user.username),kode_produk=Produk.objects.get(produk_kode=kode_barang)).update(jumlah=F('jumlah')+int(jumlah_barang))
                print('ditambahkan')
            else:
                shoppingCart.objects.create(username_cart=request.user.username,jumlah=jumlah_barang,kode_produk=Produk.objects.get(produk_kode=kode_barang))
                print('baru')
            jumlah_shopping = shoppingCart.objects.filter(username_cart = User.objects.get(username=request.user.username)).count()
            # jumlah_shopping = shoppingCart.objects.values('kode_produk').filter(username_cart = User.objects.get(username=request.user.username)).annotate(jumlah_itemnya=Count('kode_produk'))
            #jumlah_shopping = shoppingCart.objects.annotate(jumlah_itemnya=Count('kode_produk')).count()
            print(jumlah_shopping)
            return Response({'status':True,'jumlah_shopping':jumlah_shopping})
             
    return Response({'status':False})