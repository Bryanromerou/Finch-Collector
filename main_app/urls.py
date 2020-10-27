from django.contrib import admin
from django.urls import path, include
from . import views
# from .models import Reptile

urlpatterns = [
    path('', views.home, name='home'),
    path('reptiles/', views.reptile_index, name='reptile_index'),
    path('reptiles/<int:reptile_id>/', views.reptile_detail, name='detail'),
    path('reptiles/<int:reptile_id>/add_feeding', views.add_feeding, name='add_feeding'),
    path('reptiles/<int:reptile_id>/add_home', views.add_home, name='add_home'),
]
