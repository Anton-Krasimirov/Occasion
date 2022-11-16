
from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from Occasion.accounts.helpers import BootstrapFormMixin
from Occasion.accounts.models import UserProfile


class UserCreateForm(auth_forms.UserCreationForm, BootstrapFormMixin):

    first_name = forms.CharField(max_length=30,)

    last_name = forms.CharField(max_length=30,)

    email = forms.EmailField()

    phone = forms.CharField()

    region = forms.CharField(max_length=30, required=False)

    gender = forms.ChoiceField(choices=UserProfile.GENDERS,)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            region=self.cleaned_data['region'],
            gender=self.cleaned_data['gender'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'gender', 'region')
        widgets = {
            'phone': forms.NumberInput(attrs={'placeholder': 'Enter yor phone number',})
        }