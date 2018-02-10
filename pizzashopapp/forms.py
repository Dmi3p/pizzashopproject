from django import forms
from django.contrib.auth.models import User
from pizzashopapp.models import PizzaShop


class UserForm(forms.ModelForm):    #используем модель форм так-как уже есть модель
    username = forms.CharField(max_length=100, required=True) #низкоуровневое определение функционала полей
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')


class PizzaShopForm(forms.ModelForm):
    class Meta:
        model = PizzaShop
        fields = ('name', 'phone', 'addres', 'logo')
