'''
Created on 2018. 5. 26.

@author: 1104-2
'''
from django import forms
from django.contrib.auth.models import User
from django.forms.models import ModelForm
from django.forms.widgets import EmailInput

class SignForm(ModelForm):
    class Meta:
        model = User
        widgets={
            'password':forms.PasswordInput(),
            'email':forms.EmailInput()
            }
        fields=['username','email','password']
class CustomUserRegisterForm(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    passwordCheck = forms.CharField(widget=forms.PasswordInput())
    
class CustomUserLoginForm(forms.Form):
    id = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    
    