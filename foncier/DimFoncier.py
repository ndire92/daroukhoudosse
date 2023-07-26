from django.forms import ModelForm
from foncier.models import DimFoncier
from django import forms


class Dimfonfon(ModelForm):
    codeCommune = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    StatuFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    TerrDeclas5D_Ans = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    ActFonciePresen = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    TxtFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    OutilGesFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    TypeConflit = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    TypeUsage = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    ExistCadrConcert = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    EchelCadrConcert = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    Entrepris_Indust_IncidFonc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    TypeExploit_Foncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SuperficConced = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SuperficExploite = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    Superfic_Deja_Exploite = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))

    date_en = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))

    class Meta:
        model = DimFoncier
        fields = ['codeCommune', 'nomCommune', 'StatuFoncier', 'TerrDeclas5D_Ans', 'ActFonciePresen', 'TxtFoncier', 'OutilGesFoncier', 'TypeConflit', 'TypeUsage', 'ExistCadrConcert',
                  'EchelCadrConcert', 'Entrepris_Indust_IncidFonc', 'TypeExploit_Foncier', 'SuperficConced', 'SuperficExploite', 'Superfic_Deja_Exploite', 'date_en', 'date_modification']
