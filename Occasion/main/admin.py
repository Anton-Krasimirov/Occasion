from django.contrib import admin

from Occasion.main.models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # list_display = ('brand', 'user_id',)
    # sortable_by = ('brand',)
    pass


