from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotAllowed, JsonResponse
from django.core.exceptions import ValidationError,PermissionDenied
from django.contrib import messages

from .models import Restaurant
from .forms import RestaurantForm,FoodForm

User = get_user_model()

class HomePage(View):
    def get(self,request,format=None):
        if(request.user.is_authenticated and request.user.info.is_restaurant):
            res = Restaurant.objects.filter(owner=request.user)
            if(len(res)==0):
                form = RestaurantForm()
                return render(request,'home/res_create.html',{'form':form})
            res = res.first()
            menus = res.menu.all()
            return render(request,'home/index_res.html',{'res':res,'menus':menus})

        restaurants = Restaurant.objects.all()
        return render(request,'home/index.html',{'restaurants':restaurants})

    def post(self,request,formt=None):
        if not (request.user.is_authenticated and request.user.info.is_restaurant):
            raise PermissionDenied()
        
        form = RestaurantForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.owner = request.user
            instance.save()

        return redirect('home:index')


def create_new_menu(request):
    if not (request.user.is_authenticated and request.user.info.is_restaurant):
        raise PermissionDenied() # Only Owner can Add Menu
    form = FoodForm()   
    if(request.method == 'POST'):
        form = FoodForm(request.POST)
        if(form.is_valid()):
            instance = form.save(commit=False)
            instance.restaurant = request.user.res
            instance.save()

        return redirect('home:index')

    return render(request,'home/menu_create.html',{'form':form})


@login_required
def list_menus(request,id):
    res = get_object_or_404(Restaurant,pk=id)
    menus = res.menu.all()
    return render(request,'home/menu_list.html',{'menus':menus,'res':res})


