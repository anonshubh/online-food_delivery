from django import forms
from django.db.models import fields

from .models import Restaurant,Food

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'description', 'area', 'city','image','limit','lat','lon']

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = ['food_name','price','ratings','image',]