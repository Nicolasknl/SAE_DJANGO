from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cours/nouveau/', views.saisir_cours, name='saisir_cours'),
    path('absences/saisir/', views.saisir_absence, name='saisir_absence'),
    path('absences/statistiques/', views.statistiques, name='statistiques'),
]