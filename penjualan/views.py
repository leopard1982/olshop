from django.shortcuts import render
from administrasi.forms import formUsers

# Create your views here.
def dashboard(request):
    form = formUsers()
    context = {
        'form':form
    }
    return render(request,'penjualan/dashboard.html',context)