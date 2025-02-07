from django import forms
from .models import Country

class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name', 'population', 'area', 'gdp']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'population': forms.NumberInput(attrs={'class': 'form-control'}),
            'area': forms.NumberInput(attrs={'class': 'form-control'}),
            'gdp': forms.NumberInput(attrs={'class': 'form-control'}),
        }