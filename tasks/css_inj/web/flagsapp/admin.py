from django.contrib import admin

from .models import *


@admin.register(Flag, Favourite)
class AdminModel(admin.ModelAdmin):
    pass