from django.shortcuts import render
from administrasi.forms import formUsers
from administrasi.forms import formUserInformations
from administrasi.models import UserInformations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from penjualan.models import shoppingCart, wishlistCart
from django.contrib.auth.models import User
from api_rest.models import Produk
from django.db.models import F, Count
from penjualan.serializernya import serialCart, serialWishlist

# Create your views here.


def dashboard(request):
    form = formUsers()
    form_user_informasi = formUserInformations()
    try:
        data_info = UserInformations.objects.get(user_id=request.user.username)
    except:
        data_info = None

    context = {
        'form': form,
        'data_info': data_info,
        'form_user_informasi': form_user_informasi
    }
    return render(request, 'penjualan/dashboard.html', context)


@api_view(["POST"])
def add_cart(request):
    if request.method == 'POST':
        kode_barang = request.data['kode_barang']
        print(kode_barang)
        jumlah_barang = request.data['jumlah_barang']

        data = shoppingCart.objects.all().filter(username_cart=User.objects.get(
            username=request.user.username), kode_produk=Produk.objects.get(produk_kode=kode_barang))
        if (data.count() > 0):
            shoppingCart.objects.all().filter(username_cart=User.objects.get(username=request.user.username),
                                              kode_produk=Produk.objects.get(produk_kode=kode_barang)).update(jumlah=int(jumlah_barang))

        else:
            shoppingCart.objects.create(username_cart=request.user.username, jumlah=jumlah_barang,
                                        kode_produk=Produk.objects.get(produk_kode=kode_barang))

        jumlah_shopping = shoppingCart.objects.filter(
            username_cart=User.objects.get(username=request.user.username)).count()

        # update total_harga
        mscart = shoppingCart.objects.all().filter(
            username_cart=User.objects.get(username=request.user.username))
        for ms in mscart:

            harga_produk = Produk.objects.get(
                produk_kode=ms.kode_produk.produk_kode).produk_harga
            shoppingCart.objects.filter(kode_produk=Produk.objects.get(
                produk_kode=ms.kode_produk.produk_kode)).update(harganya=harga_produk)
            shoppingCart.objects.filter(kode_produk=Produk.objects.get(
                produk_kode=ms.kode_produk.produk_kode)).update(total_harga=F('harganya')*F('jumlah'))
            print(ms.kode_produk.produk_kode)

        # jumlah_shopping = shoppingCart.objects.values('kode_produk').filter(username_cart = User.objects.get(username=request.user.username)).annotate(jumlah_itemnya=Count('kode_produk'))
        # jumlah_shopping = shoppingCart.objects.annotate(jumlah_itemnya=Count('kode_produk')).count()
        myshoppingcart = serialCart(shoppingCart.objects.all().filter(
            username_cart=User.objects.get(username=request.user.username)), many=True)

        context = {
            'status': True,
            'jumlah_shopping': jumlah_shopping,
            'myshoppingcart': myshoppingcart.data
        }
        return Response(context)

    return Response({'status': False})


@api_view(['POST'])
def get_cart(request):
    if request.method == 'POST':
        try:
            jumlah = shoppingCart.objects.all().filter(
                username_cart=request.user.username).count()
        except:
            jumlah = 0

        myshoppingcart = serialCart(shoppingCart.objects.all().filter(
            username_cart=request.user.username), many=True)

        context = {
            'status': True,
            'jumlah_shopping': jumlah,
            'myshoppingcart': myshoppingcart.data
        }
        return Response(context)
    return Response({'jumlah': 0})


@api_view(['POST'])
def get_cart_satu(request):
    if request.method == 'POST':
        try:
            s_cart = shoppingCart.objects.get(
                username_cart=request.user.username, kode_produk=Produk.objects.get(produk_kode=request.data['kode_produk']))
            myserial = serialCart(s_cart)
            context = {
                'status': True,
                'myshoppingcart': myserial.data
            }
            return Response(context)
        except:
            pass
    return Response({'status': False})


@api_view(['POST'])
def get_jumlah(request):
    if request.method == 'POST':
        jumlah = 1
        try:
            kode_barang = request.data['kode_barang']
            s_cart = shoppingCart.objects.get(
                username_cart=request.user.username, kode_produk=Produk.objects.get(produk_kode=kode_barang))
            jumlah = s_cart.jumlah
        except:
            pass

        context = {
            'jumlah': jumlah,
        }
        return Response(context)
    return Response({'jumlah': 1})


@api_view(['POST'])
def setWishlist(request):
    if request.method == 'POST':
        user_id = request.user.username
        produk_id = request.data['produk_id']
        try:
            jumlah = wishlistCart.objects.all().filter(username_wishlist=User.objects.get(
                username=user_id), kode_produk_wishlist=Produk.objects.get(produk_kode=produk_id)).count()
            # print(type(request.data['ubah']))
            # print(request.data['ubah'])
            if (jumlah == 0):
                if (request.data['ubah'] == "false"):
                    return Response({'result': False})
                mywish = wishlistCart()
                mywish.username_wishlist = User.objects.get(username=user_id)
                mywish.kode_produk_wishlist = Produk.objects.get(
                    produk_kode=produk_id)
                mywish.save()
                return Response({'result': True})
            else:
                if (request.data['ubah'] == "false"):
                    return Response({'result': True})
                wishlistCart.objects.all().filter(username_wishlist=User.objects.get(username=user_id),
                                                  kode_produk_wishlist=Produk.objects.get(produk_kode=produk_id)).delete()
                return Response({'result': False})
        except:
            pass
    return Response({'result': False})


@api_view(['POST'])
def jumlahWishlist(request):
    if (request.method == 'POST'):
        user_id = request.user.username
        try:
            jumlah = wishlistCart.objects.all().filter(
                username_wishlist=User.objects.get(username=user_id)).count()
        except:
            jumlah = 0
        return Response({'result': jumlah})
    return Response({'result': 0})


@api_view(['POST'])
def get_harga_barang(request):
    if request.method == 'POST':
        produknya = Produk.objects.get(produk_kode=request.data['kode_produk'])
        return Response({'harga': produknya.produk_harga})
    return Response({'harga': 0})


@api_view(['POST'])
def del_cart(request):
    if request.method == 'POST':
        produknya = Produk.objects.get(produk_kode=request.data['kode_produk'])
        usernya = User.objects.get(username=request.user.username)
        shoppingCart.objects.all().filter(username_cart=usernya,
                                          kode_produk=produknya).delete()
        scart = shoppingCart.objects.all().filter(username_cart=usernya)
        jumlah = scart.count()
        context = {
            'result': True,
            'jumlah': jumlah,
            'myshoppingcart': serialCart(scart, many=True).data
        }
        return Response(context)
    return Response({'result': False})
