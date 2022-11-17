from django.contrib import admin

from Occasion.accounts.models import UserProfile, FirmProfile


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('first_name', 'last_name')


@admin.register(FirmProfile)
class FirmProfileAdmin(admin.ModelAdmin):
    pass