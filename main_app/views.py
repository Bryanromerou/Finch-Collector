from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Reptile , Toy
from .forms import FeedingForm, HomeForm , ReptileForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

#-------------------------------------------------------------------STATIC PAGES
def home(request):
    return render(request,"home.html")


#--------------------------------------------------------------------Reptiles
@login_required
def reptile_index(request):
    reptiles = Reptile.objects.filter(user=request.user)
    return render(request,"reptiles/index.html", {"reptiles": reptiles})
    # return HttpResponse("<h1>Reptile Index</h1>")


@login_required
def reptile_detail(request, reptile_id):
    reptile = Reptile.objects.get(id = reptile_id)
    feeding_form = FeedingForm()
    toys_reptile_doesnt_have = Toy.objects.exclude(id__in = reptile.toys.all().values_list('id'))
    return render(request, "reptiles/detail.html",{
        'reptile': reptile,
        'feeding_form': feeding_form,
        'home_form': HomeForm(),
        'toys': toys_reptile_doesnt_have
    })

@login_required
def add_reptile(request):
    if request.method  == 'POST':
        reptile_form = ReptileForm(request.POST)
        if reptile_form.is_valid():
            new_reptile = reptile_form.save(commit = False)
            new_reptile.user = request.user
            new_reptile.save()

            return redirect('detail', new_reptile.id)
    else:
        form  = ReptileForm()
        context = {
            'form': form,
        }
        return render(request, 'reptiles/new.html', context)


def delete_reptile(request, reptile_id):#parameter matches urls path
    reptile = Reptile.objects.get(id = reptile_id).delete()
    return redirect('reptile_index')


@login_required
def edit_reptile(request, reptile_id):
    reptile = Reptile.objects.get(id = reptile_id)

    if request.method  == 'POST':
        reptile_form = ReptileForm(request.POST, instance=reptile)
        if reptile_form.is_valid():
            updated_reptile = reptile_form.save()
            return redirect('detail', updated_reptile.id)
    else:
        form  = ReptileForm(instance=reptile)
        context = {
            'form': form,
            'reptile': reptile
        }
        return render(request, 'reptiles/new.html', context)


#--------------------------------------------------------------------Reptiles Feeding
@login_required
def add_feeding(request, reptile_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        new_form = form.save(commit = False)
        new_form.reptile_id = reptile_id
        new_form.save()

    return redirect('detail', reptile_id = reptile_id)

@login_required
def assoc_toy(request, reptile_id, toy_id):
    Reptile.objects.get(id =reptile_id).toys.add(toy_id)
    return redirect('detail', reptile_id = reptile_id)


def add_home(request, reptile_id):
    form = HomeForm(request.POST)

    if form.is_valid():
        new_form = form.save(commit = False)
        new_form.reptile_id = reptile_id
        new_form.save()
    
    return redirect('detail', reptile_id = reptile_id)


@login_required
def remove_toy(request, reptile_id, toy_id):
    toy = Toy.objects.get(id =toy_id)
    reptile = Reptile.objects.get(id =reptile_id)
    reptile.toys.remove(toy)
    # reptile = Reptile.objects.get(id =reptile_id).toys.remove(Toy.objects.get(id =toy_id))
    print(toy_id)
    # reptile.save()
    return redirect('detail', reptile_id = reptile_id)


def signup(request):
    error_message = ''

    if request.method == 'POST':#checks for Post request 
        form = UserCreationForm(request.POST) # if Post then populate information in the form given by Django
        if form.is_valid():
            user = form.save()#The form will be saved as a user
            login(request, user)# We will use the user we just created to log them in
            return redirect('reptiles_index')
        else:
            error_message = 'Invalid sign up - try again'
            
    form = UserCreationForm()
    context = {
        'form': form,
        'error_message': error_message
    }
    return render(request,'registration/signup.html', context)
