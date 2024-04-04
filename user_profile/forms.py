from django import forms
from django.contrib.auth.models import User
from django.forms import models


class UserForm(models.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-primary-light'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control bg-primary-light'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-primary-light'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control  bg-primary-light'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control bg-primary-light'}))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'password',
                  'confirm_password']
