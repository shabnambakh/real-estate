from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import *


@register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass


@register(MailTemplate)
class MailTemplateAdmin(admin.ModelAdmin):
    pass
