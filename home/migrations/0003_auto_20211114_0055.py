# Generated by Django 3.2.9 on 2021-11-13 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_food_limit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='limit',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='limit',
            field=models.IntegerField(default=0),
        ),
    ]