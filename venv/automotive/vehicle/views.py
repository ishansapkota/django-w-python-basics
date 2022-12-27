from django.shortcuts import render
from django.http import HttpResponse
from .models import Vehicle


# Create your views here.

def base(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html') 
#yo html lai chahi euta template bhanney folder banaauneyanityo#template lai settings ko template bhanney ko DIR ma gayera specify gareko cha

def about(request):
    return render(request,'about.html')


def create_vehicle(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     return render(request,'about.html')
    # if request.method == "GET":
    #     return render(request,'create_vehicle.html')

    if request.method == "POST":
        print(request.POST)
        model = request.POST['model']
        brand = request.POST['brand']
        type = request.POST['type']
        manufactured_date = request.POST['manufactured_date']
        vehicle = Vehicle(
            model = model,
            brand = brand,
            type = type,
            manufactured_date = manufactured_date
        )
        vehicle.save()
        return HttpResponse("VEHICLE CREATED")
    
    if request.method == "GET":
        return render(request,'create_vehicle.html')


def list_vehicle(request):
    # if request.method == "POST":
    #     print(request.POST)
    #     return render(request,'about.html')
    # if request.method == "GET":
    #     return render(request,'create_vehicle.html')

    if request.method == "POST":
        print(request.POST)
        model = request.POST['model']
        brand = request.POST['brand']
        type = request.POST['type']
        manufactured_date = request.POST['manufactured_date']
        vehicle = Vehicle(
            model = model,
            brand = brand,
            type = type,
            manufactured_date = manufactured_date
        )
        vehicle.save()
        
    
    if request.method == "GET":
        return render(request,'create_vehicle.html')