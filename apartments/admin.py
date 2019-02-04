from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Apartment


@register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    pass
