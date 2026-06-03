import csv
import datetime
from django.shortcuts import render, redirect
from .models import Enseignant, Groupe, Etudiant, Cours, Absence


def index(request):
    context = {
        'total_etudiants': Etudiant.objects.count(),
        'total_absences': Absence.objects.count(),

        'total_profs': Enseignant.objects.count(),
        'absences_non_justifiees': Absence.objects.filter(justifie__in=[0, None]).count(),

        'prochains_cours': Cours.objects.filter(date_cours__gte=datetime.date.today()).order_by('date_cours')[:5],
    }
    return render(request, 'SAE/index.html', context)


def saisir_cours(request):
    if request.method == 'POST':
        titre = request.POST.get('titre')
        date_c = request.POST.get('date_cours')
        duree = request.POST.get('duree')
        enseignant_id = request.POST.get('enseignant_id')
        groupe_id = request.POST.get('groupe_id')

        Cours.objects.create(
            titre=titre,
            date_cours=date_c,
            duree=duree,
            enseignant_id=enseignant_id,
            groupe_id=groupe_id
        )
        return redirect('index')

    context = {
        'enseignants': Enseignant.objects.all(),
        'groupes': Groupe.objects.all(),
    }
    return render(request, 'SAE/saisir_cours.html', context)


def saisir_absence(request):
    if request.method == 'POST':
        cours_id = request.POST.get('cours_id')
        fichier_csv = request.FILES.get('fichier_csv')

        fichier_decode = fichier_csv.read().decode('utf-8').splitlines()
        lecteur_csv = csv.reader(fichier_decode)

        for ligne in lecteur_csv:
            if not ligne:
                continue
            nom_etudiant = ligne[0].strip()
            prenom_etudiant = ligne[1].strip()
            doc_justificatif = ligne[4].strip() if len(ligne) > 4 else ""

            try:
                etudiant = Etudiant.objects.get(nom__iexact=nom_etudiant, prenom__iexact=prenom_etudiant)

                Absence.objects.get_or_create(
                    etudiant=etudiant,
                    cours_id=cours_id,
                    defaults={
                        'justifie': bool(doc_justificatif),
                        'justification': doc_justificatif
                    }
                )
            except Etudiant.DoesNotExist:
                continue

        return redirect('statistiques')

    context = {
        'liste_cours': Cours.objects.all()
    }
    return render(request, 'SAE/saisir_absence.html', context)


def statistiques(request):
    nom_recherche = request.GET.get('nom_recherche', '').strip()
    prenom_recherche = request.GET.get('prenom_recherche', '').strip()

    absences = []
    total_absences = 0
    etudiant_trouve = None
    recherche_effectuee = False

    if nom_recherche and prenom_recherche:
        recherche_effectuee = True
        try:
            etudiant_trouve = Etudiant.objects.get(nom__iexact=nom_recherche, prenom__iexact=prenom_recherche)
            absences = Absence.objects.filter(etudiant=etudiant_trouve)
            total_absences = absences.count()
        except Etudiant.DoesNotExist:
            etudiant_trouve = None

    context = {
        'absences': absences,
        'total_absences': total_absences,
        'etudiant': etudiant_trouve,
        'recherche_effectuee': recherche_effectuee,
        'nom_recherche': nom_recherche,
        'prenom_recherche': prenom_recherche,
    }
    return render(request, 'SAE/statistiques.html', context)