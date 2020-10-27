from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reptiles/', views.reptile_index, name='reptile_index'),
]
