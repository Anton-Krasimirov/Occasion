from django.db import models
from django.contrib.auth import models

from Occasion.accounts.managers import OccasionUserManager


class OccasionUser(models.AbstractBaseUser, models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False)

    is_staff = models.BooleanField(default=False, )

    # is_firm = models.BooleanField(default=False, )

    date_joined = models.DateTimeField(auto_now_add=True,)

    USERNAME_FIELD = 'email'

    objects = OccasionUserManager()
