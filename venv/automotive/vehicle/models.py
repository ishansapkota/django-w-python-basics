from django.db import models

# Create your models here.

class Vehicle(models.Model):
    model = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    manufactured_date = models.DateField()
    

class Parts(models.Model):
    parts_name = models.CharField(max_length = 255)
    parts_brand = models.CharField(max_length=255)
    parts_manufactured_date = models.DateField()