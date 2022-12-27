"""automotive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from vehicle.views import home,about,create_vehicle,base #url wala ma first tyo views ma dekhaako function lai call #garnu parcha

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base,name = 'base'),
    path('home/',home,name = 'home'),
    path('about/',about,name = 'about'),
    path('vehicles/',create_vehicle,name = 'vehicles')
]
