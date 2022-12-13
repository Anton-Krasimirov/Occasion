from Occasion.accounts.helpers import BootstrapFormMixin
from django import forms

from Occasion.main.models import Car, Truck


class CreatCarProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        car = super().save(commit=False)

        car.user = self.user
        if commit:
            car.save()
        return car

    class Meta:
        model = Car
        fields = (
            'brand', 'model', 'body_style', 'km', 'first_reg_date', 'transmission', 'fuel', 'color', 'price', 'photo',
            'photo2', 'photo3')
        widgets = {
            'first_reg_date': forms.TextInput(
                attrs={'placeholder': 'Fill in this format - mm/dd/year', }
            ),
            'km': forms.TextInput(attrs={'placeholder': 'Fill in format - 100 000', }),
            'price': forms.TextInput(attrs={'placeholder': 'fill in format - 10 000', }),
        }


class EditCarForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Car
        fields = ('km', 'price', 'photo', 'photo2', 'photo3')


class DeleteCarForm(forms.ModelForm):
    pass


class CreatTruckProfileForm(forms.ModelForm, BootstrapFormMixin):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        truck = super().save(commit=False)

        truck.user = self.user
        if commit:
            truck.save()
        return truck

    class Meta:
        model = Truck
        fields = (
            'brand', 'model', 'color', 'fuel', 'category', 'first_reg_date', 'transmission',
            'price', 'kilometers', 'photo', 'photo2', 'photo3')
        widgets = {
            'first_reg_date': forms.TextInput(
                attrs={'placeholder': 'Fill in this format - mm/dd/year', }
            ),
            'kilometers': forms.TextInput(attrs={'placeholder': 'Fill in format - 100 000', }),
            'price': forms.TextInput(attrs={'placeholder': 'fill in format - 10 000', }),
        }


class EditTruckForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    class Meta:
        model = Truck
        fields = ('kilometers', 'price', 'photo', 'photo2', 'photo3')


class DeleteTruckForm(forms.ModelForm):
    pass

