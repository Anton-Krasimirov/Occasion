from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from Occasion.accounts.managers import OccasionUserManager
from Occasion.accounts.validators import validate_only_letters


class OccasionUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):

    email = models.EmailField(unique=True, null=False, blank=False)

    # is_staff = models.BooleanField(default=False, )

    date_joined = models.DateTimeField(auto_now_add=True,)

    USERNAME_FIELD = 'email'

    objects = OccasionUserManager()


class UserProfile(models.Model):

    MALE = 'Male'
    FEMALE = 'Female'
    DO_NOT_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, DO_NOT_SHOW)]

    first_name = models.CharField(max_length=30, validators=(validate_only_letters,))

    last_name = models.CharField(max_length=30, validators=(validate_only_letters,))

    email = models.EmailField(unique=True, null=False, blank=False)

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DO_NOT_SHOW,
    )
    user = models.OneToOneField(
        OccasionUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'