import self
from django.contrib.auth import get_user_model
from django.db import models

from Occasion.accounts.models import OccasionUser

UserModel = get_user_model()


class Car(models.Model):
    DIESEL = "Diesel"
    GASOLINE = "Gasoline"
    HYBRID = "Hybrid"
    ELECTRIC = "Electric"

    MANUAL = "Manual"
    AUTOMATIC = "Automatic"

    CARGO_VAN = 'Cargo van'
    COUPE = 'Coupe'
    HATCHBACK = 'Hatchback'
    MINIVAN = 'Minivan'
    SUV = 'SUV'
    SEDAN = 'Sedan'
    WAGON = 'Wagon'
    COMBI = 'Combi'

    BODY_STYLES = [(x, x) for x in (CARGO_VAN, COMBI, COUPE, HATCHBACK, MINIVAN, SUV, SEDAN, WAGON)]

    TYPE_TRANSMISSION = [(x, x) for x in (MANUAL, AUTOMATIC,)]

    TYPES_FUEL = [(x, x) for x in (DIESEL, GASOLINE, HYBRID, ELECTRIC,)]

    brand = models.CharField(max_length=15, null=False, blank=False, )

    model = models.CharField(max_length=15, null=False, blank=False, )

    body_style = models.CharField(max_length=max(len(x) for (x, _) in BODY_STYLES), choices=BODY_STYLES, null=True,
                                  blank=True, )

    km = models.CharField(max_length=15, null=False, blank=False, )  # TODO fix the field

    first_reg_date = models.DateField(null=False, blank=False, )

    transmission = models.CharField(max_length=max(len(x) for (x, _) in TYPE_TRANSMISSION), choices=TYPE_TRANSMISSION, )

    fuel = models.CharField(max_length=max(len(x) for (x, _) in TYPES_FUEL), choices=TYPES_FUEL, )

    color = models.CharField(max_length=15, )

    price = models.CharField(max_length=15, null=False, blank=False, )

    photo = models.URLField(null=False, blank=False, )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.brand} {self.model}'


class CarPhoto(models.Model):
    photo = models.URLField(help_text='The photo must not be duplicated !')

    description = models.CharField(max_length=150, null=True, blank=True, )

    car = models.ForeignKey(Car, on_delete=models.CASCADE, )




