from django.contrib import admin

from Occasion.main.models import Car, Truck, Motorbike


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # list_display = ('brand', 'user_id',)
    # sortable_by = ('brand',)
    pass

@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    pass

@admin.register(Motorbike)
class MotorAdmin(admin.ModelAdmin):
    pass