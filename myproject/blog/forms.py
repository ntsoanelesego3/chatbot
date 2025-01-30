from django import forms
from .models import user_login
from .models import user_register

class user_registerForm(forms.ModelForm):
    class Meta:
        model = user_register
        fields = ['fname', 'lname', 'email', 'passwd']

class user_loginForm(forms.ModelForm):
    class Meta:
        model = user_login
        fields= ['fname', 'passwd2']