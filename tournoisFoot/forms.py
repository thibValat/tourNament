from django import forms
from .models import Tournoi, Equipe, Match

class TournoiForm(forms.ModelForm):
    equipes = forms.ModelMultipleChoiceField(queryset=Equipe.objects.all(), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Tournoi
        fields = ['nom', 'equipes']



class ScoreForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['score_equipe1', 'score_equipe2']



