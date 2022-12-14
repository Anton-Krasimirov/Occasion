from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from django.forms import TextInput

from Occasion.accounts.helpers import BootstrapFormMixin
from Occasion.accounts.models import UserProfile, FirmProfile
from Occasion.accounts.validators import phone_number_validator, validate_only_letters


class UserCreateForm(auth_forms.UserCreationForm, BootstrapFormMixin):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    first_name = forms.CharField(max_length=30, widget=TextInput(attrs={'type': 'name'}),
                                 validators=[validate_only_letters])

    last_name = forms.CharField(max_length=30, widget=TextInput(attrs={'type': 'name'}),
                                validators=[validate_only_letters])

    email = forms.EmailField(max_length=254, )

    # phone = forms.CharField(max_length=10, required=False,)
    phone = forms.CharField(label='Phone Number', widget=TextInput(attrs={'type': 'number'}),
                            validators=[phone_number_validator])

    region = forms.CharField(max_length=30, required=False)

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = UserProfile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            email=self.cleaned_data['email'],
            phone=self.cleaned_data['phone'],
            region=self.cleaned_data['region'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'region')


class FirmProfileCreateForm(auth_forms.UserCreationForm, BootstrapFormMixin):
    firm_name = forms.CharField(max_length=30, )

    email = forms.EmailField(max_length=254, )

    region = forms.CharField(max_length=30, )

    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, }), )

    phone = forms.CharField(label='Phone Number', widget=TextInput(attrs={'type': 'number'}),
                            validators=[phone_number_validator])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = FirmProfile(

            firm_name=self.cleaned_data['firm_name'],
            email=self.cleaned_data['email'],
            region=self.cleaned_data['region'],
            address=self.cleaned_data['address'],
            phone=self.cleaned_data['phone'],
            user=user,
        )
        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('firm_name', 'password1', 'password2', 'email', 'phone', 'region', 'address')
        widgets = {'address': forms.Textarea(attrs={'rows': 2, }, )}


class EditUserProfileForm(auth_forms.UserCreationForm, BootstrapFormMixin):
    pass


class EditFirmProfileForm(auth_forms.UserCreationForm, BootstrapFormMixin):
    pass


class DeleteUserForm(forms.ModelForm):
    pass


class DeleteFirmForm(forms.ModelForm):
    pass
