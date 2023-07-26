from django.shortcuts import render, redirect
from foncier.DimFoncier import Dimfonfon

from django.contrib import messages
from foncier.DimFoncierGouvernanc import Dimfong



from foncier.models import DimFoncier, DimFoncierGouvernanc

# Create your views here.


def DimFon(request):

    if request.method == 'POST':

        form = Dimfonfon(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncier/')
    else:
        form = Dimfonfon()

    return render(request, 'pag/Dimfon.html', {'form': form, 'dataObject': DimFoncier.objects.all()})


# update Gouver
def update_fon(request, id):
    dataObject = DimFoncier.objects.get(id=id)
    form = Dimfonfon(instance=dataObject)
    if request.method == 'POST':
        form = Dimfonfon(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncier/')

    context = {

        'form': form

    }
    return render(request, 'pag/Dimfon.html', context)


def delete_fon(request, id):
    dataObject = DimFoncier.objects.get(id=id)
    if request.method == 'POST':

        dataObject.delete()
        return redirect('/foncier/DimFoncier/')
    context = {

        'item': dataObject, }
    return render(request, 'pag/delete_fon.html', context)


def DFG(request):
    if request.method == 'POST':
        form = Dimfong(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncierGouvernanc/')
    else:
        form = Dimfong()

    return render(request, 'pag/DimFoncierGouvernanc.html', {'form': form, 'dataObject': DimFoncierGouvernanc.objects.all()})


# update Gouver
def update_up_Gouve(request, id):
    dataObject = DimFoncierGouvernanc.objects.get(id=id)
    form = Dimfong(instance=dataObject)
    if request.method == 'POST':
        form = Dimfong(request.POST, instance=dataObject)
        if form.is_valid():
            form.save()
            messages.success(request, " Are Successfully Added !")
            return redirect('/foncier/DimFoncierGouvernanc/')

    context = {

        'form': form

    }
    return render(request, 'pag/DimFoncierGouvernanc.html', context)


def delete_up_Gouve(request, id):
    dataObject = DimFoncierGouvernanc.objects.get(id=id)
    if request.method == 'POST':

        dataObject.delete()
        return redirect('/foncier/DimFoncierGouvernanc/')
    context = {

        'item': dataObject, }
    return render(request, 'pag/delete_fon.html', context)
