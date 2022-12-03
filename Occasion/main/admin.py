from django.contrib import admin

from Occasion.accounts.models import UserProfile
from Occasion.main.models import Car, CarPhoto


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'user_id',)
    sortable_by = ('brand',)


@admin.register(CarPhoto)
class CarPhotoAdmin(admin.ModelAdmin):
    pass