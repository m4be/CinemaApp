from .models import Persons
from django.forms import ModelForm, TextInput

class PersonForm(ModelForm):
    class Meta:
        model = Persons
        fields = ['name', 'card_number', 'expiry_m', 'expiry_y', 'cvc']

        widgets = {
            'name': TextInput(attrs={
                'class':'form-control',
                'placeholder' : 'Имя на карте'
            }),
            'card_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер карты'
            }),
            'expiry_m': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ММ'
            }),
            'expiry_y': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ГГ'
            }),
            'cvc': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'CVC'
            })
        }