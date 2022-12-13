from django.contrib.auth import get_user_model
from django.db import models

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

    photo2 = models.URLField(null=False, blank=False, )

    photo3 = models.URLField(null=False, blank=False, )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.brand} {self.model}'


class Truck(models.Model):
    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'

    DIESEL = "Diesel"
    GASOLINE = "Gasoline"

    BOX = 'Box'
    CAR_CARRIER = 'Car carrier'
    DUMPER_TRUCK = 'Dumper truck'
    FOOD_CARRIER = 'Food Carrier'
    GRAIN_TRUCK = 'Grain Truck'
    MINING_TRUCK = 'Mining Truck'
    HYDRAULIC_PLATFORM = 'Hydraulic Platform'
    OVER_TRUCKS_OVER = 'Over truck over 7.5 t'

    TYPES_FUEL = [(x, x) for x in (DIESEL, GASOLINE,)]
    CATEGORY = [(x, x) for x in (BOX, CAR_CARRIER, DUMPER_TRUCK, FOOD_CARRIER, GRAIN_TRUCK, MINING_TRUCK,
                                 HYDRAULIC_PLATFORM, OVER_TRUCKS_OVER)]
    TYPE_TRANSMISSION = [(x, x) for x in (MANUAL, AUTOMATIC,)]

    brand = models.CharField(max_length=15, null=False, blank=False, )

    model = models.CharField(max_length=15, null=False, blank=False, )

    color = models.CharField(max_length=15, )

    fuel = models.CharField(max_length=max(len(x) for (x, _) in TYPES_FUEL), choices=TYPES_FUEL, )

    category = models.CharField(max_length=max(len(x) for (x, _) in CATEGORY), choices=CATEGORY, null=True,
                                blank=True, )

    first_reg_date = models.DateField(null=False, blank=False, )

    price = models.CharField(max_length=15, null=False, blank=False, )

    kilometers = models.CharField(max_length=15, null=False, blank=False, )

    transmission = models.CharField(max_length=max(len(x) for (x, _) in TYPE_TRANSMISSION), choices=TYPE_TRANSMISSION, )

    photo = models.URLField(null=False, blank=False, )

    photo2 = models.URLField(null=True, blank=True, )

    photo3 = models.URLField(null=True, blank=True, )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.brand} {self.model}'


class Motorbike(models.Model):
    DIESEL = "Diesel"
    PETROL = "Petrol"
    ELECTRIC = "Electric"
    OTHER = "Other"

    MANUAL = 'Manual'
    AUTOMATIC = 'Automatic'

    NAKED_BIKE = "Naked Bike"
    SCOOTER = "Scooter"
    CHOPPER = "Chopper"
    MOTORCYCLE = "Motorcycle"
    ENDURO = "Enduro"

    TYPE_TRANSMISSION = [(x, x) for x in (MANUAL, AUTOMATIC,)]
    CATEGORY = [(x, x) for x in (NAKED_BIKE, SCOOTER, CHOPPER, MOTORCYCLE, ENDURO,)]
    TYPES_FUEL = [(x, x) for x in (DIESEL, PETROL, ELECTRIC, OTHER)]

    brand = models.CharField(max_length=15, null=False, blank=False, )

    model = models.CharField(max_length=15, null=False, blank=False, )

    type = models.CharField(max_length=max(len(x) for (x, _) in CATEGORY), choices=CATEGORY, null=True,
                            blank=True, )
    fuel = models.CharField(max_length=max(len(x) for (x, _) in TYPES_FUEL), choices=TYPES_FUEL, )

    price = models.CharField(max_length=15, null=False, blank=False, )

    first_reg_date = models.DateField(null=False, blank=False, )

    kilometers = models.CharField(max_length=15, null=False, blank=False, )

    photo = models.URLField(null=False, blank=False, )

    photo2 = models.URLField(null=True, blank=True, )

    photo3 = models.URLField(null=True, blank=True, )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, )

    def __str__(self):
        return f'{self.brand} {self.model}'