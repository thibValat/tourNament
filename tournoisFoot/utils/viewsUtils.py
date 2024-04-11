from django.shortcuts import redirect
from ..models import Match, Equipe


def processAddTournoiForm(form):
    tournoi = form.save() 
    equipes = form.cleaned_data['equipes']
    if len(equipes) < 2:
        return redirect('addTournoiForm')
    for i in range(len(equipes)):
        for j in range(i + 1, len(equipes)):
            match = Match.objects.create(
                tournoi=tournoi,
                equipe1=equipes[i],
                equipe2=equipes[j]
            )
    return tournoi



def processSaisirScores(matchs, request, tournoi):
    for match in matchs:
        score_equipe1 = request.POST.get(f'score_equipe1_{match.id}')
        score_equipe2 = request.POST.get(f'score_equipe2_{match.id}')
        if(score_equipe1 == '' or score_equipe2 == ''):
            return redirect('saisirScores', tournoi_id=tournoi.id)
        if score_equipe1 is not None and score_equipe2 is not None:
            match.score_equipe1 = score_equipe1
            match.score_equipe2 = score_equipe2
            match.save()
    return redirect('indexFoot')   



def processTournoiDetails(tournoi):
    equipes = Equipe.objects.filter(tournoi=tournoi)
    for equipe in equipes:
        matches = Match.objects.filter(tournoi=tournoi, equipe1=equipe) | Match.objects.filter(tournoi=tournoi, equipe2=equipe)
        nb_matchs_joues = 0
        points = 0
        buts_pour = 0
        buts_contre = 0
        for match in matches:
            if match.score_equipe1 is not None and match.score_equipe2 is not None:
                nb_matchs_joues += 1
                if match.equipe1 == equipe:
                    buts_pour += match.score_equipe1
                    buts_contre += match.score_equipe2
                    if match.score_equipe1 > match.score_equipe2:
                        points += 3
                    elif match.score_equipe1 == match.score_equipe2:
                        points += 1
                elif match.equipe2 == equipe:
                    buts_pour += match.score_equipe2
                    buts_contre += match.score_equipe1
                    if match.score_equipe2 > match.score_equipe1:
                        points += 3
                    elif match.score_equipe2 == match.score_equipe1:
                        points += 1
        equipe.nb_matchs_joues = nb_matchs_joues
        equipe.points = points
        equipe.buts_pour = buts_pour
        equipe.buts_contre = buts_contre

    equipes = sorted(equipes, key=lambda x: (-x.points, -x.buts_pour))
    return equipes