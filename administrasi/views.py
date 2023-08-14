from django.shortcuts import render, HttpResponseRedirect
from administrasi.forms import formUsers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def dashboard(request):
    return render(request, 'administrasi/dashboard.html')

def createUser(request):
    if request.method == 'POST':
        forms = formUsers(request.POST)
        if forms.is_valid():
            usernya= forms.save()
            usernya.set_password(request.POST['password'])
            usernya.save()
            print("ok")
            user = authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                messages.success(request,"Create New User Successfully")
            else:
                messages.success(request,"Create New User Failed! Username '%s' is already taken! Please Try again!" %request.POST['username'])
        else:
                messages.success(request,"Create New User Failed! Username '%s' is already taken! Please Try again!" %request.POST['username'])
    forms = formUsers()
    context= {
        'forms':forms
    }
    return render(request, 'administrasi/createUser.html',context)

def chatTelegram(request):
    if request.method == 'POST':
         nomor_HP = request.POST['nomor_HP']
         print(nomor_HP)
         #send message to telegram
         api_id = 22531450
         api_hash = "acdcf81fa80cfbfafce2a2d5b1268f05"
         client = TelegramClient('onlineshop',api_id,api_hash)
         client.start()
         client.send_message(nomor_HP,"hallo")
    return HttpResponseRedirect('/')