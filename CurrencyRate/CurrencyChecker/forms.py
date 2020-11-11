from django import forms
from .models import CurrencyRate


# Creating form for our model
class CurrencyRateForm(forms.ModelForm):
    class Meta:
        model = CurrencyRate
        # Choosing fields to be in form
        fields = ['uah_rate', 'date']
        # Setting labels
        labels = {
            'uah_rate': 'UAH currency rate',
            'date': 'Date'
        }
