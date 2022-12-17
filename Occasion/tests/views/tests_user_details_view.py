from datetime import date

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from Occasion.accounts.models import UserProfile
from Occasion.main.models import Car

UserModel = get_user_model()

class UserTest(TestCase):

    VALID_USER_DATA = {
        # 'username': 'Ant@abv.bg',
        'email': 'Ant@abv.bg',
        # 'password1': 123456,
        # 'password2': 123456,
        # 'first_name': 'Anton',
        # 'last_name': 'And',
        # 'phone': '0899656565',
        # 'region': 'Varna',

    }

    VALID_PROFILE_DATA = {

        'email': 'Ant@abv.bg',
        # 'password1': 123456,
        # 'password2': 123456,
        'first_name': 'Anton',
        'last_name': 'And',
        'phone': '0899656565',
        'region': 'Varna',
    }

    VALID_CAR_DATA = {
        'brand': 'Audi',
        'model': 'A6',
        'body_style': 'combi',
        'km': '50 000',
        'first_reg_date': date(1990, 4, 13),
        'transmission': 'automatic',
        'fuel': 'diesel',
        'color': 'Red',
        'price': '50 000',
        'photo': 'https://images.unsplash.com/photo-1605559424843',
    }

    def __create_user(self, **credentials):
        return UserModel.objects.create(**credentials)


    def __get_response_for_profile(self, profile):
        return self.client.get(reverse('profile details', kwargs={'pk': profile.pk}))

    def __create_valid_user_and_profile(self):
        user = self.__create_user(**self.VALID_USER_DATA)
        profile = UserProfile.objects.create(**self.VALID_PROFILE_DATA, user=user, )
        return user, profile


    def test_when_user_has_two_cars__expect_return_two_cars_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        car1 = Car.objects.create(**self.VALID_CAR_DATA, user=user, )
        car2 = Car.objects.create(**self.VALID_CAR_DATA, user=user, )
        cars = list(Car.objects.filter(user_id=profile.pk))

        self.assertEqual(len(cars), 2)

    def test_when_user_has_no_cars__expect_retusn_empty_list_be_true(self):
        user, profile = self.__create_valid_user_and_profile()
        cars = list(Car.objects.filter(user_id=profile.pk))
        self.assertEqual(len(cars), 0)

    def test_expect_correct_template(self):
        user, profile = self.__create_valid_user_and_profile()
        response = self.__get_response_for_profile(profile)
        self.assertTemplateUsed('accounts/profile_details.html')