from django.forms import ModelForm
from foncier.models import DimGeographie
from django import forms


class Dimfgeo(ModelForm):

    codeCommune = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 900px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    CodeIndicateur = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    Indicateur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    CodeDomaine = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    NomDomaine = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 900px;', 'class': 'form-control'}))
    date = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 800px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = DimGeographie
        fields = ['codeCommune', 'nomCommune', 'CodeIndicateur',
                  'Indicateur', 'CodeDomaine', 'NomDomaine', 'date', 'date_modification']
