from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from pizzashopapp.forms import UserForm, PizzaShopForm, UserFormForEdit, PizzaForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from pizzashopapp.models import Pizza
# Create your views here.

def home(request):
    return redirect(pizzashop_home)


@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_home(request):
    return render(request, 'pizzashopapp/pizza.html', {})


@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_account(request):
    user_form = UserFormForEdit(instance=request.user)
    pizzashop_form = PizzaShopForm(instance=request.user.pizzashop)

    if request.method == "POST":
        user_form = UserFormForEdit(request.POST, instance=request.user)
        pizzashop_form = PizzaShopForm(request.POST, request.FILES, instance=request.user.pizzashop)

        if user_form.is_valid() and pizzashop_form.is_valid():
            user_form.save
            pizzashop_form.save


    return render(request, 'pizzashopapp/account.html', {
        'user_form': user_form,
        'pizzashop_form': pizzashop_form
    })


@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_pizza(request):
    pizzas = Pizza.objects.filter(pizzashop=request.user.pizzashop).order_by("-id")
    return render(request, 'pizzashopapp/pizza.html', {
        'pizzas' : pizzas
    })

@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_add_pizza(request):
    form = PizzaForm()
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.pizzashop = request.user.pizzashop
            pizza.save()
            return redirect(pizzashop_pizza)
    return render(request, 'pizzashopapp/add_pizza.html', {
    'form' : form
    })

@login_required(login_url='/pizzashopapp/sign-in')
def pizzashop_edit_pizza(request, pizza_id):
    form = PizzaForm(instance=Pizza.objects.get(id = pizza_id))
    if request.method == 'POST':
        form = PizzaForm(request.POST, request.FILES, instance=Pizza.objects.get(id = pizza_id))
        if form.is_valid():
            pizza = form.save()

            return redirect(pizzashop_pizza)
    return render(request, 'pizzashopapp/edit_pizza.html', {
    'form' : form
    })


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
