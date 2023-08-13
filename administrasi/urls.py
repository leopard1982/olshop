from django.urls import path
from administrasi.views import dashboard, createUser, chatTelegram

urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('c/users/', createUser, name='createUser'),
    path('c/telegram/', chatTelegram, name='chatTelegram')
]
