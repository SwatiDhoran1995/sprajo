from django.core import validators
from django import forms
from .models import Sprajo

class ProductInfo(forms.ModelForm):
    class Meta:
        model = Sprajo
        fields = ['Name','Image','description','capacity','unit','price']
    #    widgets={
    #        'Name':forms.CharField(attrs={'class':'form-control'}),
    #        'Image':forms.ImageField(attrs={'class':'form-control'}),
    #        'description': forms.CharField(attrs={'class': 'form-control'}),
    #        'capacity': forms.IntegerField(attrs={'class': 'form-control'}),
    #        'unit': forms.CharField(attrs={'class': 'form-control'}),
    #        'Price': forms.IntegerField(attrs={'class': 'form-control'})
    #  }
