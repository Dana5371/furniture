from typing import OrderedDict
from django import forms
from order.models import Order

class CreateOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'