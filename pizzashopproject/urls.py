"""pizzashopproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pizzashopapp import views

from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings  # нужны для работы с файлами

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('pizzashopapp/sign-in', auth_views.login,  #подключаем модуль для аутентификации
    {'template_name': 'pizzashopapp/sign_in.html'},
    name='pizzashopapp-sign-in'),

    path('pizzashopapp/sign-out', auth_views.logout,  #подключаем модуль для выхода из учетки
    {'next_page': '/'},
    name='pizzashopapp-sign-out'),

    path('pizzashopapp/', views.pizzashop_home, name='pizzashop-home'),

    path('pizzashopapp/sign-up', views.pizzashop_sign_up, name='pizzashop-sign-up'),

    path('pizzashopapp/account', views.pizzashop_account, name='pizzashop-account'),
    path('pizzashopapp/pizza', views.pizzashop_pizza, name='pizzashop-pizza'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #тоже нужно для работы с файлами
