from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pizzashopapp.forms import UserForm, PizzaShopForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
# Create your views here.

def home(request):
    return redirect(pizzashop_home)


@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_home(request):
    return render(request, 'pizzashopapp/home.html', {})


@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_account(request):
    return render(request, 'pizzashopapp/account.html', {})


@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_pizza(request):
    return render(request, 'pizzashopapp/pizza.html', {})

def pizzashop_sign_up(request):
    user_form = UserForm
    pizzashop_form = PizzaShopForm

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES)

        if user_form.is_valid() and pizzashop_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_pizzashop = pizzashop_form.save(commit=False)
            new_pizzashop.owner = new_user
            new_pizzashop.save()

            login(request, authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            ))

            return redirect(pizzashop_home)

    return render(request, 'pizzashopapp/sign_up.html',       #формы передаём 3тьим параметром
    {
        'user_form' : user_form,
        'pizzashop_form' : pizzashop_form
    })
