from django.contrib import admin

from .models import Restaurant,Food,Cart

admin.site.register(Restaurant)
admin.site.register(Cart)
admin.site.register(Food)