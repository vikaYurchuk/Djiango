from django import forms
from main.models import Product


class CreateProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__" 
        widgets = {
            "brand": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Enter car brand"}
            ),
        }