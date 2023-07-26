from django.urls import path

from .import views

app_name = 'foncier'


urlpatterns = [
    path('DimFoncier/', views.DimFon, name='DimFoncier'),
    path('DimFoncierGouvernanc/', views.DFG, name='DimFoncierGouvernanc'),
   # path('DimGeographie/', views.DG, name='DimGeographie'),
   # path('FactFoncier/', views.FF, name='FactFoncier'),
  
    path('de_fon<int:id>/', views.delete_fon, name='de_fon'),
    path('up_fon<int:id>/', views.update_fon, name='up_fon'),
    path('de_Gouve<int:id>/', views.delete_up_Gouve, name='de_Gouve'),
    path('up_Gouve<int:id>/', views.update_up_Gouve, name='up_Gouve'),
   # path('up_geo<int:id>/', views.update_geo, name='up_geo'),
    #path('de_geo<int:id>/', views.delete_geo, name='de_geo'),


]
