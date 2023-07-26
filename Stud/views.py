
from django.db.models import Q
from django.db import IntegrityError
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.http import Http404
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, logout, login
from app.models import Post, Ressource, UserProfile
from django.contrib.auth import login
from django.contrib import messages
from django.contrib import sessions
from app.forms import SignUpForm, ProfileForm
from app.ressource import Ressou
from app.forms import PostForm
from django.contrib.auth import get_user_model

from foncier.models import DimFoncier, DimFoncierGouvernanc, Visiteur

User = get_user_model()


def Base(request):
    return render(request, 'pages/base.html')


def Accueil(request):

    dt = DimFoncier.objects.all().count()
    datg = DimFoncierGouvernanc.objects.all().count()

    nb_visite = Visiteur.objects.all().count()
    
    if 'visits' not in request.session:
        # Si elle n'existe pas, initialise à 0
        request.session['visits'] = 0

    # Incrémente le nombre de visites
    request.session['visits'] += 1

    # Le reste de votre code pour la vue de la page d'accueil
    # ...
    context = {
        'dt': dt,
        'datg': datg,

        'nb_visite': nb_visite,
    }
    return render(request, 'pages/accueil.html', context)


def register(request):
    if request.method == 'POST':
        fs = SignUpForm(request.POST)
        if fs.is_valid():
            user = fs.save()
            user.refresh_from_db()
            user.email = fs.cleaned_data.get('email')
            user.save()
            raw_password = fs.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        fs = SignUpForm()
    return render(request, 'pages/register.html', {'fs': fs})


def user_login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_gestionnaire:
                return redirect('home')

            elif user.is_decideur:
                return redirect('decideur')

            else:
                return redirect('visiteur')
        else:
            error = ' passwoerd ou username'
    return render(request, 'pages/login.html')


def user_logout(request):
    logout(request)
    return redirect('/')


def coord(request):
    return render(request, 'pages/coordonateur.html')


def deci(request):
    return render(request, 'pages/decideur.html')


def visit(request):
    
    profiles = UserProfile.objects.all()
    return render(request, 'pages/visiteur.html', {'profiles': profiles})
# end login

def peche(request):

    return render(request, 'pa/peche.html')
# @login_required


@login_required(login_url='/login/')
def ho(request):
    posts = Post.objects.order_by('-id').all()
    paginator = Paginator(posts, 6)

    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    posts_number = posts.count()
    message = f'{posts_number} posts:'
    if posts_number == 1:
        message = f'{posts_number} post:'

    context = {
        'posts': page_object,
        # 'post_number':post_number,
        'message': message
    }

    return render(request, 'pa/index.html', context)


@login_required(login_url='/login/')
def detail(request, id):
    post = Post.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'pa/detail.html', context)

# @login_required


@login_required(login_url='/login/')
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/post/')
    else:
        form = PostForm()

    context = {
        'form': form,
    }

    return render(request, 'pa/new_post.html', context)


@login_required(login_url='/login/')
def update_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Vérifiez si l'utilisateur est l'auteur du post
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect('/post/')
        else:
            form = PostForm(instance=post)
    else:
        raise Http404

    context = {
        'form': form,
        'post': post
    }
    return render(request, 'pa/update_post.html', context)


@login_required(login_url='/login/')
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if post.user == request.user:
        post.delete()
        return redirect('/post/')
    else:
        raise Http404

    return render(request, 'pa/delete.html')


@login_required(login_url='/login/')
def search(request):
    search = request.GET.get('search')
    posts = Post.objects.filter(Q(title__icontains=search) |
                                Q(content__icontains=search) |
                                Q(image__icontains=search)
                                )

    posts_number = posts.count()
    message = f'{posts_number} results:'
    if posts_number == 1:
        message = f'{posts_number} results:'

    context = {
        'posts': posts,
        'message': message,
    }
    return render(request, 'pa/search.html', context)


def all(request):

    posts = Post.objects.order_by('-id').all()
    context = {
        'posts': posts,
        # 'post_number':post_number,
    }
    return render(request, 'pa/blog.html', context)


def ress(request):

    if request.method == 'POST':
        form = Ressou(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('/ressource/')
    else:
        form = Ressou()
    return render(request, 'pa/ressource.html', {'form': form, 'dataObject': Ressource.objects.all()})


@login_required(login_url='/login/')
def upda_ress(request, id):
    stud = Ressource.objects.get(id=id)

    if request.method == 'POST':
        form = Ressou(request.POST, request.FILES, instance=stud)
        if form.is_valid():
            form.save()
            return redirect('ressource')

    else:
        form = Ressou(instance=stud)

    context = {

        'form': form,

    }

    return render(request, 'pa/update_ress.html', context)


@login_required(login_url='/login/')
def del_ress(request, id):
    stud = Ressource.objects.get(id=id)
    stud.delete()
    return redirect('ressource')

    return render(request, 'pa/delete.html')

# start profile
@login_required(login_url='/login/')
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm()
    return render(request, 'pages/create_profile.html', {'form': form})


@login_required(login_url='/login/')
def update_profile(request):
    user_profile = request.user.userprofile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user_profile.user = request.user
            user_profile.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm(instance=user_profile)

    return render(request, 'pages/update_profile.html', {'form': form})


@login_required(login_url='/login/')
def delete_profile(request):
    user_profile = request.user.userprofile
    if request.method == 'POST':
        user_profile.delete()
        return redirect('/')  # Replace 'home' with the appropriate URL
    return render(request, 'pages/delete_profile.html', {'user_profile': user_profile})


@login_required(login_url='/login/')
def profile_detail(request):
    user_profile = request.user.userprofile
    return render(request, 'pages/profile_detail.html', {'user_profile': user_profile})


@login_required(login_url='/login/')
def profile_list(request):
    profiles = UserProfile.objects.all()
    return render(request, 'pages/profile_list.html', {'profiles': profiles})

# end profile

def commune(request):
    
    return render(request, 'pa/commune.html')


def co(request):
    
    return render(request, 'pa/commune_detail.html')

def fonce(request):

    return render(request, 'pa/foncier.html')
