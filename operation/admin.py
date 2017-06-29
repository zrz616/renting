from django.contrib import admin
from .models import Appointment, UserFavorite


class AppointmentAdmin(admin.ModelAdmin):
    """docstring for appointment"""
    pass


class FavoriteAdmin(admin.ModelAdmin):
    """docstring for FavoriteAdmin"""
    pass

admin.site.register(Appointment)
admin.site.register(UserFavorite)
