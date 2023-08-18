from django.shortcuts import render
from administrasi.forms import formUsers
from administrasi.forms import formUserInformations
from administrasi.models import UserInformations

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