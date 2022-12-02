from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model


from Occasion.accounts.helpers import BootstrapFormMixin
from Occasion.accounts.models import UserProfile, FirmProfile


class UserCreateForm(auth_forms.UserCreationForm, BootstrapFormMixin):
    first_name = forms.CharField(max_length=30, )

    last_name = forms.CharField(max_length=30, )

    email = forms.EmailField(max_length=254, )

    phone = forms.CharField(max_length=10, required=False,)

    region = forms.CharField(max_length=30, required=False)

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
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:  # TODO fix the widget fields , Enter your phone nomber
        model = get_user_model()
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'region')
        widgets = {
            'phone': forms.NumberInput(attrs={'placeholder': 'Enter your phone number', })
        }


class FirmProfileCreateForm(auth_forms.UserCreationForm, BootstrapFormMixin):

    firm_name = forms.CharField(max_length=30, )

    email = forms.EmailField(max_length=254, )

    region = forms.CharField(max_length=30, )

    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,}), )

    phone = forms.CharField(max_length=10, required=False,)

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

