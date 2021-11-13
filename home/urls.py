from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('create-menu/',views.create_new_menu,name='create-menu'),
    path('list-menus/<int:id>/',views.list_menus,name='list-menus')
]
