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
from vehicle.views import home,about,create_vehicle,base,list_vehicle,vehicle_details,vehicle_delete,vehicle_update, CreateParts,DeleteParts,ListParts,DetailsParts #url wala ma first tyo views ma dekhaako function lai call #garnu parcha
from users.views import Login,RegistrationView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base,name = 'base'),
    path('home/',home,name = 'home'),
    path('about/',about,name = 'about'),
    path('vehicles/',list_vehicle,name = 'vehicles'),
    path('vehicles/create_vehicle',create_vehicle,name = 'create_vehicle'),
    path('vehicles/<int:pk>',vehicle_details,name = 'vehicle_details'),
    path('vehicle_delete/<int:pk>',vehicle_delete,name = 'vehicle_delete'),
    path('vehicles/vehicle_update/<int:pk>',vehicle_update, name = 'vehicle_update'),


    path('create_parts/',CreateParts.as_view(),name = 'create_parts'),
    path('parts_details/',DetailsParts.as_view(),name = 'parts_details'),
    path('parts_list/<int:pk>',ListParts.as_view(),name = 'parts_list'),
    path('parts_delete/<int:pk>',DeleteParts.as_view(),name = 'parts_delete'),

    path('login/',Login.as_view(),name = 'user_login'),
    path('user_register',RegistrationView.as_view(),name = 'user_register')

]
