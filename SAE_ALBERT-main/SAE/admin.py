from django.contrib import admin
from .models import Groupe, Enseignant, Etudiant, Cours, Absence

@admin.register(Groupe)
class GroupeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')
    search_fields = ('nom',)

@admin.register(Enseignant)
class EnseignantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')
    search_fields = ('nom', 'email')

@admin.register(Etudiant)
class EtudiantAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'groupe')
    list_filter = ('groupe',)
    search_fields = ('nom', 'prenom')

@admin.register(Cours)
class CoursAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_cours', 'duree', 'enseignant', 'groupe')
    list_filter = ('date_cours', 'groupe', 'enseignant')
    search_fields = ('titre',)

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('etudiant', 'cours', 'justifie', 'justification')
    list_filter = ('justifie', 'cours')