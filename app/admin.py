from django.contrib import admin
from .models import BikeAd,MyUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class BikeAdsAdmin(admin.ModelAdmin):
    list_display = ["bike_name", "bike_type", "bike_rent_price","bike_engine_size","is_active"]

admin.site.register(BikeAd,BikeAdsAdmin)


class MyUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email','mobile','address')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
    )
    list_display = ["username","first_name", "last_name", "email","mobile","is_active"]

admin.site.register(MyUser,MyUserAdmin)
