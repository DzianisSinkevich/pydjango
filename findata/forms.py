from .models import FinData
from django.forms import ModelForm, TextInput, DateTimeInput


class FinDataForm(ModelForm):
    class Meta:
        model = FinData
        fields = ['date', 'value', 'operation', 'category']

        widgets = {
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата операции'
            }),
            "value": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Сумма'
            }),
            "operation": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Операция'
            }),
            "category": TextInput(attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'Категория'
            })
        }