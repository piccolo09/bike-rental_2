from django.contrib import admin
from .models import BikeAd

# Register your models here.

class BikeAdsAdmin(admin.ModelAdmin):
    list_display = ["bike_name", "bike_type", "bike_rent_price","bike_engine_size"]

admin.site.register(BikeAd,BikeAdsAdmin)
