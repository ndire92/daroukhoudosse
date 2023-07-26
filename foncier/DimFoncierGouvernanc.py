from django.forms import ModelForm
from foncier.models import DimFoncierGouvernanc
from django import forms


class Dimfong(ModelForm):
    codeCommune = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    nomCommune = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    LoiReglement = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    OutilSecuriseFoncie = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    ActFoncier = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    DegreConnaissanc = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    NivComprehension = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    Resume = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    AtelierBonInformat = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SecuritAjout = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    NreConflitAnnComm = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    NbreIndustri_FoncComm = forms.IntegerField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SuperfiAlloueIndustri = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    NbreIndustri_FoncCommMoy = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SupTypeFoncier = forms.DecimalField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    ActImplique = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    CauseAvance = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': ' CauseAvance ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SolutionPropose = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    SolutionRetenu = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    VerificatProcedur = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    ControlPermanant = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    ConfliFoncieEnregMois = forms.CharField(widget=forms.NumberInput(
        attrs={'placeholder': '  ', 'style': 'width: 800px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    date_ent = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))
    date_modification = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date', 'style': 'width: 300px;border: 4px solid #557029;border-radius: 10px;', 'class': 'form-control'}))

    class Meta:
        model = DimFoncierGouvernanc
        fields = ['codeCommune',
                  'nomCommune',
                  'LoiReglement',
                  'OutilSecuriseFoncie',
                  'ActFoncier',
                  'DegreConnaissanc',
                  'NivComprehension',
                  'Resume',
                  'AtelierBonInformat',
                  'SecuritAjout',
                  'NreConflitAnnComm',
                  'NbreIndustri_FoncComm',
                  'SuperfiAlloueIndustri',
                  'NbreIndustri_FoncCommMoy',
                  'SupTypeFoncier',
                  'ActImplique',
                  'CauseAvance',
                  'SolutionPropose',
                  'SolutionRetenu',
                  'VerificatProcedur',
                  'ControlPermanant',
                  'ConfliFoncieEnregMois',
                  'date_ent',
                  'date_modification']
