from django.contrib import admin
from django.contrib.auth import get_user_model

from Occasion.accounts.models import UserProfile, FirmProfile

UserModel = get_user_model()


@admin.register(UserProfile)
class ProfileAdmin(admin.ModelAdmin):
    # sortable_by = ('id',)
    pass


@admin.register(FirmProfile)
class FirmProfileAdmin(admin.ModelAdmin):
    # sortable_by = ('id',)
    pass


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    pass
