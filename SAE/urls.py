from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cours/nouveau/', views.saisir_cours, name='saisir_cours'),
    path('absences/saisir/', views.saisir_absence, name='saisir_absence'),
    path('absences/statistiques/', views.statistiques, name='statistiques'),
    path('enseignant/<int:enseignant_id>/planning/', views.planning_enseignant, name='planning_enseignant'),
    path('absence/<int:absence_id>/modifier/', views.modifier_absence, name='modifier_absence'),
    path('absence/<int:absence_id>/supprimer/', views.supprimer_absence, name='supprimer_absence'),
    path('etudiant/<int:etudiant_id>/supprimer/', views.supprimer_etudiant, name='supprimer_etudiant'),
    path('enseignant/<int:enseignant_id>/supprimer/', views.supprimer_enseignant, name='supprimer_enseignant'),
]