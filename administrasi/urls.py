from django.urls import path
from administrasi.views import dashboard, createUser, loginUser, logoutUser
from administrasi.views import upload_propinsi, upload_kecamatan, upload_kota, save_user
from administrasi.views import get_kota,get_kecamatan, ganti_password

urlpatterns = [
    path('', dashboard,name='dashboard'),
    path('c/users/', createUser, name='createUser'),
    path('l/users/',loginUser, name='loginUser'),
    path('lo/users/',logoutUser, name='logoutUser'),
    path('master/upload/propinsi/',upload_propinsi,name="upload_propinsi"),
    path('master/upload/kota/',upload_kota,name="upload_kota"),
    path('master/upload/kecamatan/',upload_kecamatan,name="upload_kecamatan"),
    path('user/info/',save_user,name="save_user"),
    path('user/password/',ganti_password,name="ganti_password"),
    path('api/get/kota/',get_kota,name="get_kota"),
    path('api/get/kecamatan/',get_kecamatan,name="get_kecamatan"),
]
