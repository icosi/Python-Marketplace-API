from django import forms

from .models import *


class ProductsForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    category = forms.CharField(max_length=100)
    description = forms.CharField(max_length=100)
    price = forms.CharField(max_length=100)

    class Meta:
        model = Products
        fields = ["name", "category", "description", "price"]
