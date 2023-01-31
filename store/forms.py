from django import forms
from django.core.exceptions import ValidationError
from store.models import Product

class OrderItemForm(forms.Form):
    quantity = forms.IntegerField(required=True, label='Quantity')
        