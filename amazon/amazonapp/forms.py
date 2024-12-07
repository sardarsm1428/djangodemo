from django.forms import ModelForm,Form
from django import forms
from .models import login

class auto_form(ModelForm):
    class Meta:
        model=login
        fields='__all__'
class LoginForm(Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)