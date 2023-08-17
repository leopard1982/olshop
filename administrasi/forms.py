from django import forms
from django.contrib.auth.models import User
from administrasi.models import UserInformations, Kecamatan, Kota,Propinsi,uploadCSV

class formUsers(forms.ModelForm):
    password2 = forms.CharField(max_length=128,widget=forms.PasswordInput(attrs={'placeholder':'Password Confirmation','class':'my-2 w-100 form-control shadow','required':'required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password','class':'my-2 w-100 form-control shadow','required':'required'}))
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','username', 'password']
    
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First Name','class':'my-2 w-100 form-control shadow','required':'required'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name','class':'my-2 w-100 form-control shadow','required':'required'}),
            'username': forms.TextInput(attrs={'placeholder':'Username ','class':'my-2 w-100 form-control shadow','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder':'First Name','class':'my-2 w-100 form-control shadow','required':'required'}),
        }

class formUserInformations(forms.ModelForm):
    class Meta:
        model = UserInformations
        fields = "__all__"
        exclude = ['point']

        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}),
            'nomor_hp': forms.TextInput(attrs={'class': 'form-control'}),
            'alamat':forms.TextInput(attrs={'class': 'form-control'}),
            'propinsi':forms.Select(attrs={'class': 'form-select'}),
            'kota':forms.Select(attrs={'class': 'form-select'}),
            'kecamatan':forms.Select(attrs={'class': 'form-select'}),
        }

class formUpload(forms.ModelForm):
    class Meta:
        model = uploadCSV
        fields = "__all__"

        widgets = {
            'filenya': forms.FileInput(attrs={'class': 'form-control'}),
        }