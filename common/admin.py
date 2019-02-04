from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import City


@register(City)
class CityAdmin(admin.ModelAdmin):
    pass
