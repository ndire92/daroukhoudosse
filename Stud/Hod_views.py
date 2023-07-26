
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# from django.template import engine
# from django.template import Engine, EngineHandler, engines

from django.contrib import messages


from foncier.models import DimFoncier, DimFoncierGouvernanc, Visiteur

# @login_required(login_url='/')


def Home(request):

    dt = DimFoncier.objects.all().count()
    datg = DimFoncierGouvernanc.objects.all().count()

    nb_visite = Visiteur.objects.all().count()

    context = {
        'dt': dt,
        'datg': datg,
 
        'nb_visite': nb_visite,
    }
    return render(request, 'Hod/home.html', context)
