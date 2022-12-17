
from django.test import TestCase


from Occasion.accounts.forms import FirmProfileCreateForm


class UserFormTests(TestCase):
    VALID_DATA = {
        'firm_name': 'Anton77',
        'password1': 123456,
        'password2': 123456,
        'email': 'Ant@abv.bg',
        'phone': '0899656565',
        'region': 'Sofia',
        'address': 'Sofia 1000',
    }

    def test_firm_profile_create__when_phone_is_correct__expect_success(self):
        form = FirmProfileCreateForm(self.VALID_DATA)
        self.assertTrue(form.is_valid())

    def test_user_profile_create__when_phone_is_not_correct__expect_to_fail(self):
        form = FirmProfileCreateForm(
            data={'email': 'Ant@abv.bg', 'password1': 123456, 'password2': 123456, 'firm_name': 'Anton77',
                  'phone': '99656565', 'region': 'Sofia', 'address': 'Sofia 1000',})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['phone'], ['Enter Phone Number Correctly', ])

