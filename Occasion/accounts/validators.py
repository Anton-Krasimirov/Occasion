import re

from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for ch in value:
        if not ch.isalpha():

            raise ValidationError('Value must contain only letters')


def phone_number_validator(value):
    if not re.compile(r'^[+|0|00]\d{7,13}$').match(value):
        raise ValidationError('Enter Phone Number Correctly')