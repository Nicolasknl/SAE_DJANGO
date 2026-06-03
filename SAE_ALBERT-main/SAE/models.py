from django.db import models


class Groupe(models.Model):
    nom = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'groupe'

    def __str__(self):
        return self.nom


class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enseignant'

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=150, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)

    # Si le groupe (ex: RT12) est supprimé, l'étudiant reste en base mais n'a plus de groupe attitré
    groupe = models.ForeignKey('Groupe', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'etudiant'

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Cours(models.Model):
    titre = models.CharField(max_length=150)
    date_cours = models.DateField(blank=True, null=True)
    duree = models.IntegerField(blank=True, null=True)

    # Si le prof est supprimé, le cours reste au planning (champs mis à NULL)
    enseignant = models.ForeignKey('Enseignant', on_delete=models.SET_NULL, blank=True, null=True)

    # Si le groupe est supprimé, le cours reste au planning (champs mis à NULL)
    groupe = models.ForeignKey('Groupe', on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cours'

    def __str__(self):
        return f"{self.titre} ({self.date_cours})"


class Absence(models.Model):
    # Si l'étudiant est supprimé, toutes ses fiches d'absences sautent en CASCADE
    etudiant = models.ForeignKey('Etudiant', on_delete=models.CASCADE, blank=True, null=True)

    # Si le cours est supprimé, l'absence associée est supprimée en CASCADE
    cours = models.ForeignKey('Cours', on_delete=models.CASCADE, blank=True, null=True)

    justifie = models.IntegerField(blank=True, null=True, default=0)
    justification = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'absence'