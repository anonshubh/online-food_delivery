from django import forms

from .models import Restaurant,Food

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'area', 'city','image','lat','lon']