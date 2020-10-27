from django.shortcuts import render
from django.http import HttpResponse
from main_app.models import Reptile
# from .models import reptiles

def home(request):
    return render(request,"home.html")

def reptile_index(request):
    reptiles = Reptile.objects.all()
    return render(request,"reptiles/index.html", {"reptiles": reptiles})
    # return HttpResponse("<h1>Reptile Index</h1>")

