from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Restaurant(models.Model):
    owner = models.OneToOneField(User,on_delete=models.CASCADE,related_name='res')
    name = models.CharField(max_length=128,unique=True)
    description = models.TextField()
    area = models.CharField(max_length=128)
    city = models.CharField(max_length=128)
    image = models.URLField(max_length=500)
    ratings = models.PositiveSmallIntegerField(default=0)
    lat = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    lon = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name[:20]

class Food(models.Model):
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE,related_name='menu',null=True)
    food_name = models.CharField(max_length=56)
    price = models.PositiveIntegerField()
    ratings = models.PositiveSmallIntegerField(default=0)
    image = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.food_name[:20]
