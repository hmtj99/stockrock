from django import forms
from .models import Stock

class StockSearchForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['name']
        labels = {
            'name':'',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'id':'tags'}
            )
        }