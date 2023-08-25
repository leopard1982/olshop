from django.shortcuts import render, HttpResponseRedirect
from administrasi.forms import formUsers, formUpload, formUserInformations
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from administrasi.models import uploadCSV, Kota,Kecamatan,Propinsi, UserInformations
from django.conf import settings
import os
import pandas
from administrasi.serializersnya import  serialKota, serialKecamatan


# Create your views here.
def dashboard(request):
    return render(request, 'administrasi/dashboard.html')

@api_view(['POST','GET'])
def createUser(request):
    if request.method == 'POST':
        # try:
            forms = User()
            forms.username = request.POST['username'].lower()
            forms.password = request.POST['password']
            forms.email = request.POST['email']
            forms.first_name = request.POST['first_name']
            forms.last_name = request.POST['last_name']
            forms.save()
            forms=User.objects.get(username=request.POST['username'].lower())
            forms.set_password(request.POST['password'])
            forms.save()
            user = authenticate(username=request.POST['username'].lower(),password=request.POST['password'])
            if user is not None:
                login(request,user)
                return Response({'success':True})
            else:
                return Response({'success':False})
        # except:
            # return Response({'success':False})

    return Response({'success':False})


@api_view(['POST','GET'])
def loginUser(request):
    if request.method == 'POST':
        try:
            username=request.POST['user_login'].lower()
            password=request.POST['password_login']
            user = authenticate(username=username, password=password)
            print(user)
            if(user is not None):
                login(request,user)
                return Response({'success': True})
        except:
            return Response({'success': False})
    return Response({'success': False})

def logoutUser(request):
    logout(request)
    return HttpResponseRedirect("/")

def upload_propinsi(request):
    if request.method == 'POST':
        print(request.FILES)
        print(request.POST)
        form = formUpload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            filenya = uploadCSV.objects.all().order_by("-id")[0]
            pathnya = os.path.join(settings.BASE_DIR,"media/" + str(filenya.filenya))

            x=pandas.read_csv(pathnya)
            for xx in x.iterrows():
                #data yang diambil adalah data indeks ke 1
                data = xx[1]
                #save ke table
                try:
                    prov_table = Propinsi()
                    prov_table.kode_propinsi=data['kode_provinsi']
                    prov_table.nama_propinsi=data['nama_provinsi']
                    prov_table.save()
                except:
                    print("error")
                    #ada data double

    form = formUpload()
    propinsinya = Propinsi.objects.all()
    context = {
        'form_propinsi' : form,
        'propinsinya' : propinsinya 
    }
    return render(request,'administrasi/uploadPropinsi.html',context)

def upload_kota(request):
    if request.method == 'POST':
        form = formUpload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            filenya = uploadCSV.objects.all().order_by("-id")[0]
            pathnya = os.path.join(settings.BASE_DIR,"media/" + str(filenya.filenya))

            x=pandas.read_csv(pathnya)
            for xx in x.iterrows():
                #data yang diambil adalah data indeks ke 1
                data = xx[1]
                #save ke table
                try:
                    kota_table = Kota()
                    kota_table.kode_propinsi=Propinsi.objects.get(kode_propinsi=data['kode_provinsi'])
                    kota_table.nama_kota=data['nama_kota']
                    kota_table.kode_kota=data['kode_kota']
                    kota_table.save()
                except:
                    print("error")
                    #ada data double

    form = formUpload()
    kotanya = Kota.objects.all()
    context = {
        'form_kota' : form,
        'kotanya' : kotanya 
    }
    return render(request,'administrasi/uploadKota.html',context)

def upload_kecamatan(request):
    if request.method == 'POST':
        form = formUpload(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            filenya = uploadCSV.objects.all().order_by("-id")[0]
            pathnya = os.path.join(settings.BASE_DIR,"media/" + str(filenya.filenya))

            x=pandas.read_csv(pathnya)
            for xx in x.iterrows():
                #data yang diambil adalah data indeks ke 1
                data = xx[1]
                #save ke table
                try:
                    kecamatan_table = Kecamatan()
                    kecamatan_table.kode_kota=Kota.objects.get(kode_kota=data['kode_kota'])
                    kecamatan_table.nama_kecamatan=data['nama_desa']
                    kecamatan_table.kode_kecamatan=data['kode_desa']
                    kecamatan_table.save()
                except:
                    print("error")
                    #ada data double

    form = formUpload()
    kecamatannya = Kecamatan.objects.all()
    context = {
        'form_kecamatan' : form,
        'kecamatannya' : kecamatannya 
    }
    return render(request,'administrasi/uploadKecamatan.html',context)

def save_user(request):
    if request.method == 'POST':
        form = formUserInformations(request.POST)
        if form.is_valid():
            print("ok")
            form.save()
        else:
            #berarti update saja
            data = UserInformations.objects.get(user_id=request.POST['user_id'])
            form = formUserInformations(request.POST,instance=data)
            if form.is_valid():
                form.save()            
    return HttpResponseRedirect("/")

@api_view(['POST'])
def get_kota(request):
    if request.method == 'POST':
        kode=request.data['propinsi']
        try:
            data = Kota.objects.all().filter(kode_propinsi=Propinsi.objects.get(kode_propinsi=kode))
            serialinya = serialKota(data,many=True)
            return Response(serialinya.data)
        except:
            return Response({})
            
    return Response({})

@api_view(['POST'])
def get_kecamatan(request):
    if request.method == 'POST':
        kode=request.data['kota']
        data = Kecamatan.objects.all().filter(kode_kota=Kota.objects.get(kode_kota=kode))
        serialinya = serialKecamatan(data,many=True)
        return Response(serialinya.data)
        
    return Response({})

@api_view(['POST'])
def ganti_password(request):
    if request.method == "POST":
        print(request.data)
        password_lama = request.data['password_lama']
        password_baru1 = request.data['password_baru1']
        password_baru2 = request.data['password_baru2']

        user = authenticate(username=request.user.username,password=password_lama)
        if(user is not None):
            if(password_baru1==password_baru2):
                usernya = User.objects.get(username=request.user.username)
                usernya.set_password(password_baru1)
                usernya.save()
                return Response({'result':True})
            
    return Response({'result':False})