from django.db import models
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User


from Occasion.accounts.managers import OccasionUserManager
from Occasion.accounts.validators import validate_only_letters
from django.core.validators import RegexValidator


class OccasionUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(unique=True, null=False, blank=False, )

    date_joined = models.DateTimeField(auto_now_add=True, )

    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField(
        default=False,)

    objects = OccasionUserManager()


class UserProfile(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^[+|0]\d{9,12}$")

    first_name = models.CharField(max_length=30, null=False, blank=False, validators=(validate_only_letters,))

    last_name = models.CharField(max_length=30, null=False, blank=False, validators=(validate_only_letters,))

    email = models.EmailField(unique=True, null=False, blank=False, )

    phone = models.CharField(validators=[phoneNumberRegex], max_length=10,  null=False, blank=False, )

    region = models.CharField(max_length=30, null=False, blank=False, )


    user = models.OneToOneField(
        OccasionUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class FirmProfile(models.Model):
    phoneNumberRegex = RegexValidator(regex=r"^[+|0]\d{9,12}$")

    firm_name = models.CharField(max_length=30, null=False, blank=False, validators=(validate_only_letters,))

    email = models.EmailField(unique=True, null=False, blank=False, )

    region = models.CharField(max_length=30, null=False, blank=False, )

    address = models.TextField(null=False, blank=False, )

    phone = models.CharField(validators=[phoneNumberRegex], max_length=10, null=False, blank=False, )

    user = models.OneToOneField(
        OccasionUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )
