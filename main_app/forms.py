from django import forms
from .models import Feeding,Reptile,Home

class FeedingForm(forms.ModelForm):
    
    class Meta:
        model = Feeding
        fields = ("date","meal")

# class ReptileForm(forms.ModelForm):
    
#     class Meta:
#         model = Reptile
#         fields = ("name","species","breed", "color", "age")

class HomeForm(forms.ModelForm):
    
    class Meta:
        model = Home
        fields = ("address","location","city", "state", "zipcode", "occupants")
