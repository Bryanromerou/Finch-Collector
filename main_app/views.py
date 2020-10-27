from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reptile
from .forms import FeedingForm, HomeForm

# from .models import reptiles

def home(request):
    return render(request,"home.html")

def reptile_index(request):
    reptiles = Reptile.objects.all()
    return render(request,"reptiles/index.html", {"reptiles": reptiles})
    # return HttpResponse("<h1>Reptile Index</h1>")


def reptile_detail(request, reptile_id):
    reptile = Reptile.objects.get(id = reptile_id)
    feeding_form = FeedingForm()
    return render(request, "reptiles/detail.html",{
        'reptile': reptile,
        'feeding_form': feeding_form,
        'home_form': HomeForm()
    })


def add_feeding(request, reptile_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_form = form.save(commit = False)
        new_form.reptile_id = reptile_id
        new_form.save()

    return redirect('detail', reptile_id = reptile_id)

def add_home(request, reptile_id):
    form = HomeForm(request.POST)

    if form.is_valid():
        new_form = form.save(commit = False)
        new_form.reptile_id = reptile_id
        new_form.save()
    
    return redirect('detail', reptile_id = reptile_id)