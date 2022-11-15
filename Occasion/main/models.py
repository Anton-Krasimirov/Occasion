from django.db import models

from Occasion.accounts.models import OccasionUser
from Occasion.accounts.validators import MaxFileSizeInValidator


class Car(models.Model):

    DIESEL = "Diesel"
    GASOLINE = "Gasoline"
    HYBRID = "Hybrid"
    ELECTRIC = "Electric"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"

    TYPE_TRANSMISSION = [(x, x) for x in (MANUAL, AUTOMATIC,)]

    TYPES_FUEL = [(x, x) for x in (DIESEL, GASOLINE, HYBRID, ELECTRIC,)]

    brand = models.CharField(max_length=15, null=False, blank=False,)

    model = models.CharField(max_length=15, null=False, blank=False,)

    description = models.CharField(max_length=255, null=True, blank=True,)

    km = models.PositiveIntegerField()

    first_reg_date = models.DateField()# TODO провери дата format?

    transmission = models.CharField(max_length=max(len(x) for (x, _) in TYPE_TRANSMISSION), choices=TYPE_TRANSMISSION,)

    fuel = models.CharField(max_length=max(len(x) for (x, _) in TYPES_FUEL), choices=TYPES_FUEL,)

    color = models.CharField(max_length=15,)

    price = models.FloatField()

    user = models.ForeignKey(OccasionUser, on_delete=models.CASCADE,)

    def __str__(self):
        return f'{self.brand} {self.model}'


class CarPhoto(models.Model):

    photo = models.ImageField(validators=(
        MaxFileSizeInValidator,
    ),)

    publication_date = models.DateTimeField(auto_now_add=True,)

    user = models.ForeignKey(OccasionUser, on_delete=models.CASCADE,)