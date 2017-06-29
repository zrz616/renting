from django.contrib import admin

from .models import House, City, School, Position, Device


# 后台管理器
class HouseAdmin(admin.ModelAdmin):
    """docstring for HouseAdmin"""
    pass


class CityAdmin(admin.ModelAdmin):
    """docstring for City"""
    pass


class SchoolAdmin(admin.ModelAdmin):
    """docstring for SchoolAdmin"""
    pass

# 在admin中注册
admin.site.register(House, HouseAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(School, SchoolAdmin)
admin.site.register(Position)
admin.site.register(Device)
