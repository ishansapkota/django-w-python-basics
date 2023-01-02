from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Vehicle,Parts
from django import forms
from vehicle.forms import PartsForm
from django.views import View
from django.views.generic import DeleteView,ListView
from django.urls import reverse_lazy



# Create your views here.

#GET METHOD bhaneko chahi URL baata request garera enter gareko chij ko method GET huncha 
#POST METHOD bhaneko chahi euta page ko textfield or dialog box ma enter gareko chij or for eg FORMS ma enter 
#gareko chij ko method chahi POST huncha

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
        return redirect('vehicles')
    
    if request.method == "GET":
        return render(request,'create_vehicle.html')

 

def list_vehicle(request):
    if request.method == "GET":
        context = {
            'all_vehicles': Vehicle.objects.all()
        }
        return render(request,'list_vehicle.html',context)


def vehicle_details(request,pk):
    vehicle = Vehicle.objects.get(id=pk)
    context = {
            'vehicle' : vehicle
        }

    return render(request,'vehicle_details.html',context)

def vehicle_delete(request,pk):
    vehicle = Vehicle.objects.get(id=pk)
    vehicle.delete()
    return redirect('vehicles')

def vehicle_update(request,pk):
    vehicle = Vehicle.objects.get(pk = id)
    form = Vehicle(request.POST ,isinstance=vehicle)
    vehicle.save()



class CreateParts(View):
    def get(self,request):
        form = PartsForm()
        context = {
            'form': form
        }
        return render(request,'create_parts.html',context)
        #return HttpResponse("this is where the parts html goes.")

    def post(self,request):
        form = PartsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('parts')
        context = {
            "form": form
        }
        return render(request,'create_parts.html',context)

#list display garna ko laagi django ma ListView bhanney class nai huney raicha django.generic bhanney module ma

class ListParts(ListView):
    parts = Parts
    template_name = 'parts_details.html'



#deletion ko laagi chahi django ko generic module ma DeleteView bhanney class nai raicha so tei use gareko 
class DeleteParts(DeleteView):
    parts = Parts
    template_name = 'base.html'