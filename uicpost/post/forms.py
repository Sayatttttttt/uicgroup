from django import forms
from .models import Order, Filial, Role
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class OrderForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=30, required=True)
    second_name = forms.CharField(label='Last name', max_length=150, required=True)
    father = forms.CharField(label='Middle name', max_length=200, required=True)
    phone = forms.CharField(label='Number', max_length=200, required=True)
    email = forms.EmailField(label='EMAIL', required=True)
    filial_send = forms.ModelChoiceField(label='From', queryset=Filial.objects.all(), required=True, widget=forms.Select(attrs={'id': 'pick_up_address'}))
    filial_receive = forms.ModelChoiceField(label='To', queryset=Filial.objects.all(), required=True, widget=forms.Select(attrs={'id': 'drop_off_address'}))
    # price = forms.IntegerField(label='Price', required=True, disabled=True,  widget=forms.NumberInput(attrs={'id': 'price_field'}))

    class Meta:
        model = Order
        fields = ['first_name', 'second_name', 'father', 'phone', 'email', 'filial_send', 'filial_receive', 'price']