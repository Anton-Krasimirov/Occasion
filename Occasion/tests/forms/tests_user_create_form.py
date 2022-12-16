from django.core.exceptions import ValidationError
from django.test import TestCase

from Occasion.accounts.forms import UserCreateForm


class UserFormTests(TestCase):
    VALID_DATA = {
        'email': 'Ant@abv.bg',
        'password1': 123456,
        'password2': 123456,
        'first_name': 'Anton',
        'last_name': 'And',
        'phone': '0899656565',
        'region': 'Varna',

    }

    def test_user_profile_create__when_first_name_contains_only_letters__expect_success(self):
        form = UserCreateForm(self.VALID_DATA)
        self.assertTrue(form.is_valid())

    def test_user_profile_create__when_first_name_contains_number__expect_to_fail(self):
        form = UserCreateForm(
            data={'email': 'Ant@abv.bg', 'password1': 123456, 'password2': 123456, 'first_name': 'Anton1',
                  'last_name': 'And', 'phone': '0899656565', 'region': 'Varna', })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], ['Value must contain only letters', ])

    def test_user_profile_create__when_first_name_contains_other__expect_to_fail(self):
        form = UserCreateForm(
            data={'email': 'Ant@abv.bg', 'password1': 123456, 'password2': 123456, 'first_name': 'Anton@',
                  'last_name': 'And', 'phone': '0899656565', 'region': 'Varna', })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['first_name'], ['Value must contain only letters', ])

    def test_user_profile_create__when_last_name_contains_number__expect_to_fail(self):
        form = UserCreateForm(
            data={'email': 'Ant@abv.bg', 'password1': 123456, 'password2': 123456, 'first_name': 'Anton',
                  'last_name': 'And2', 'phone': '0899656565', 'region': 'Varna', })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['last_name'], ['Value must contain only letters', ])

    def test_user_profile_create__when_last_name_contains_other__expect_to_fail(self):
        form = UserCreateForm(
            data={'email': 'Ant@abv.bg', 'password1': 123456, 'password2': 123456, 'first_name': 'Anton',
                  'last_name': 'And$', 'phone': '0899656565', 'region': 'Varna', })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['last_name'], ['Value must contain only letters', ])

    def test_user_profile_create__when_phone_is_correct__expect_success(self):
        form = UserCreateForm(self.VALID_DATA)
        self.assertTrue(form.is_valid())

    def test_user_profile_create__when_phone_is_not_correct__expect_to_fail(self):
        form = UserCreateForm(
            data={'email': 'Ant@abv.bg', 'password1': 123456, 'password2': 123456, 'first_name': 'Anton',
                  'last_name': 'And2', 'phone': '99656565', 'region': 'Varna', })
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone'], ['Enter Phone Number Correctly', ])
