from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('',views.HomePage.as_view(),name='index'),
    path('create-menu/',views.create_new_menu,name='create-menu'),
    path('list-menus/<int:id>/',views.list_menus,name='list-menus'),
    path('add-cart/<int:id>/',views.add_cart,name='add-cart'),
    path('remove-cart/<int:id>/',views.remove_cart,name='remove-cart'),
    path('cart/<int:id>/',views.cart_view,name='cart-view'),
    path('checkout/<int:id>/',views.check_out,name='check-out'),
]
