from django.contrib import admin

from Occasion.accounts.models import UserProfile, FirmProfile

@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    # sortable_by = ('id',)
    pass

@admin.register(FirmProfile)
class FirmProfileAdmin(admin.ModelAdmin):
    # sortable_by = ('id',)
    pass
