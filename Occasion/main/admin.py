from django.contrib import admin

from Occasion.main.models import Car, CarPhoto


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # list_display = ('brand', 'user_id',)
    # sortable_by = ('brand',)
    pass


@admin.register(CarPhoto)
class CarPhotoAdmin(admin.ModelAdmin):
    pass