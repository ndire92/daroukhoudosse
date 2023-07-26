"""Stud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include


from .import views
from django.contrib import admin
from django.urls import path
from .import Hod_views, views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('admin', admin.site.urls),
    path('base', views.Base, name='base'),
    path('home', Hod_views.Home, name='home'),
    path('', views.Accueil, name='acceueil'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('gestionnaire', views.coord, name='gestionnaire'),
    path('decideur', views.deci, name='decideur'),
    path('visiteur', views.visit, name='visiteur'),
    path('peche/', views.peche, name="peche"),
    path('post/<int:id>/', views.detail, name="detail"),
    path('post/', views.all, name="post"),
    path('new_post', views.new_post, name="new_post"),
    path('update_post/<int:pk>/', views.update_post, name="update_post"),
    path('delete_post/<int:id>/', views.delete_post, name="delete_post"),

    path('ressource/', views.ress, name="ressource"),
    path('upda_res/<int:id>/', views.upda_ress, name="upda_res"),
    path('delete_ress/<int:id>/', views.del_ress, name="delete_ress"),
    path('foncier', views.fonce, name='foncier'),
    path('commune', views.commune, name='commune'),
    path('commune_detail', views.co, name='commune_detail'),
    path('foncier/', include('foncier.urls')),

    # profile

    path('profile_list/', views.profile_list, name='profile_list'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('profile_detail/', views.profile_detail, name='profile_detail'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
