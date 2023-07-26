from django.utils import timezone
from django.db import models

# foncier


class DimFoncier(models.Model):

    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    StatuFoncier = models.CharField(max_length=300)
    TerrDeclas5D_Ans = models.CharField(max_length=300)
    ActFonciePresen = models.CharField(max_length=300)
    TxtFoncier = models.CharField(max_length=300)
    OutilGesFoncier = models.CharField(max_length=300)
    TypeConflit = models.CharField(max_length=300)
    TypeUsage = models.CharField(max_length=300)
    ExistCadrConcert = models.CharField(max_length=300)
    EchelCadrConcert = models.CharField(max_length=300)
    Entrepris_Indust_IncidFonc = models.CharField(max_length=300)
    TypeExploit_Foncier = models.CharField(max_length=300)
    SuperficConced = models.DecimalField(max_digits=10, decimal_places=5)
    SuperficExploite = models.DecimalField(max_digits=10, decimal_places=5)
    Superfic_Deja_Exploite = models.DecimalField(
        max_digits=10, decimal_places=5)
    date_en = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.nomCommune)


class DimFoncierGouvernanc(models.Model):
    codeCommune = models.IntegerField()
    nomCommune = models.CharField(max_length=300)
    LoiReglement = models.CharField(max_length=300)
    OutilSecuriseFoncie = models.CharField(max_length=300)
    ActFoncier = models.CharField(max_length=300)
    DegreConnaissanc = models.CharField(max_length=300)
    NivComprehension = models.CharField(max_length=300)
    Resume = models.CharField(max_length=300)
    AtelierBonInformat = models.CharField(max_length=300)
    SecuritAjout = models.CharField(max_length=300)
    NreConflitAnnComm = models.IntegerField()
    NbreIndustri_FoncComm = models.IntegerField()
    SuperfiAlloueIndustri = models.DecimalField(
        max_digits=10, decimal_places=2)
    NbreIndustri_FoncCommMoy = models.IntegerField()
    SupTypeFoncier = models.DecimalField(max_digits=10, decimal_places=5)
    ActImplique = models.CharField(max_length=300)
    CauseAvance = models.CharField(max_length=300)
    SolutionPropose = models.CharField(max_length=300)
    SolutionRetenu = models.CharField(max_length=300)
    VerificatProcedur = models.CharField(max_length=300)
    ControlPermanant = models.CharField(max_length=300)
    ConfliFoncieEnregMois = models.IntegerField()
    date_ent = models.DateTimeField()
    date_modification = models.DateTimeField()

    def __str__(self):
        return str(self.nomCommune)


class Visiteur (models.Model):
    nom = models.CharField(max_length=25)
    date_visiteur = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom
