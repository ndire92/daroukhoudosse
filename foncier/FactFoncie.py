from django.forms import ModelForm
from foncier.models import FactFoncier
from django import forms


class Dimff(ModelForm):

    IdFoncier_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    IdGouvFoncier_FK = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NreConflitAnnComm = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreIndustri_FoncComm = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    SuperfiAlloueIndustri = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    NbreIndustri_FoncCommMoy = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    SupTypeFoncier = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))

    ConfliFoncieEnregMois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    SuperficConced = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': ' ', 'style': 'width: 800px;', 'class': 'form-control'}))
    SuperficExploite = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    Superfic_Deja_Exploite = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '', 'style': 'width: 800px;', 'class': 'form-control'}))
    datef = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 800px;', 'class': 'form-control'}))
    date_modification = forms.CharField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 800px;', 'class': 'form-control'}))

    class Meta:
        model = FactFoncier
        fields = ['IdFoncier_FK', 'IdGouvFoncier_FK', 'NreConflitAnnComm', 'NbreIndustri_FoncComm', 'SuperfiAlloueIndustri',
                  'NbreIndustri_FoncCommMoy', 'SupTypeFoncier', 'ConfliFoncieEnregMois', 'SuperficConced', 'SuperficExploite', 'Superfic_Deja_Exploite', 'datef', 'date_modification']
