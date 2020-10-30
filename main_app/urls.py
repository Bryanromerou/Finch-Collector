from django.contrib import admin
from django.urls import path, include
from . import views
# from .models import Reptile

urlpatterns = [
    path('', views.home, name='home'),

    path('reptiles/', views.reptile_index, name='reptile_index'),
    # Reptile CRUD
    path('reptiles/new/', views.add_reptile, name='add_reptile'),
    path('reptiles/<int:reptile_id>/delete/', views.delete_reptile, name='delete_reptile'),
    path('reptiles/<int:reptile_id>/edit/', views.edit_reptile, name='edit_reptile'),
    path('reptiles/<int:reptile_id>/', views.reptile_detail, name='detail'),

    path('reptiles/<int:reptile_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('reptiles/<int:reptile_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('reptiles/<int:reptile_id>/remove_toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),

    path('accounts/signup', views.signup, name='signup'),
]
