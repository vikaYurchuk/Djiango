from django import forms  

from main.models import Product


class EditProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__" 