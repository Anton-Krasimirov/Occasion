from Occasion.accounts.helpers import BootstrapFormMixin
from django import forms

from Occasion.main.models import Car


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
        fields = ('brand', 'model', 'body_style', 'km', 'first_reg_date', 'transmission', 'fuel', 'color', 'price', 'photo',)
        widgets = {
            'first_reg_date': forms.TextInput(
                attrs={'placeholder': 'Fill in this format - 31/12/0000',}
            ),
            'km': forms.TextInput(attrs={'placeholder': 'Fill in format - 100 000',}),
            'price': forms.TextInput(attrs={'placeholder': 'fill in format - 10 000',}),
        }

