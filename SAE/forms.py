from django import forms
from .models import Cours, Absence


class CoursForm(forms.ModelForm):

    class Meta:
        model = Cours
        fields = ['titre', 'date', 'duree', 'enseignant', 'groupe']

        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: R109 - Technologies Web',
                'style': 'max-width: 400px;'
            }),
            'date': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'style': 'max-width: 400px;'
            }),
            'duree': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ex: 90',
                'style': 'max-width: 400px;'
            }),
            'enseignant': forms.Select(attrs={
                'class': 'form-select',
                'style': 'max-width: 400px;'
            }),
            'groupe': forms.Select(attrs={
                'class': 'form-select',
                'style': 'max-width: 400px;'
            }),
        }


class AbsenceCSVForm(forms.Form):
    cours = forms.ModelChoiceField(
        queryset=Cours.objects.all(),
        empty_label="Choisir un cours...",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'style': 'max-width: 500px;'
        })
    )
    fichier_csv = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'form-control',
            'style': 'max-width: 500px;',
            'accept': '.csv'
        })
    )