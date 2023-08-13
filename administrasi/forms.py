from django import forms
from django.contrib.auth.models import User

class formUsers(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name', 'email','username', 'password']
    
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder':'First Name','class':'my-2 w-100 form-control shadow','required':'required'}),
            'last_name': forms.TextInput(attrs={'placeholder':'Last Name','class':'my-2 w-100 form-control shadow','required':'required'}),
            'username': forms.TextInput(attrs={'placeholder':'Username ','class':'my-2 w-100 form-control shadow','required':'required'}),
            'password': forms.PasswordInput(attrs={'placeholder':'Password','class':'my-2 w-100 form-control shadow','required':'required'}),
            'email': forms.EmailInput(attrs={'placeholder':'First Name','class':'my-2 w-100 form-control shadow','required':'required'}),
        }