from django.contrib import admin
from .models import Vehicle

# Register your models here.
# @admin.register(vehicle)
# class vehicleadmin(admin.ModelAdmin):
#     list_display=('model','brand','type','manufactured_date')

admin.site.register(Vehicle)