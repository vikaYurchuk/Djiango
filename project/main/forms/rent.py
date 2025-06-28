# forms.py
from django import forms
from main.models import Rental


class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['car', 'start_date', 'end_date', 'name', 'email', 'phone']
