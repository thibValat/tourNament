from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Tournoi, Equipe, Match
from .forms import TournoiForm, ScoreForm
from .utils.viewsUtils import processAddTournoiForm, processSaisirScores, processTournoiDetails


def index(request):
    tournois = Tournoi.objects.all()
    return render(request, 'tournoisFoot/index.html', {'tournois': tournois})



def addTournoiForm(request):
    if request.method == 'POST':
        form = TournoiForm(request.POST)
        if form.is_valid():
            tournoi = processAddTournoiForm(form)
            return redirect('saisirScores', tournoi_id=tournoi.id)
    else:
        form = TournoiForm()  
        form.fields['equipes'].queryset = Equipe.objects.all()
        
    return render(request, 'tournoisFoot/addTournoiForm.html', {'form': form, 'equipes': Equipe.objects.all()})




def saisirScores(request, tournoi_id):
    tournoi = Tournoi.objects.get(pk=tournoi_id)
    matchs = Match.objects.filter(tournoi=tournoi)
    if request.method == 'POST':
        return processSaisirScores(matchs, request, tournoi)
    else:
        forms = {match.id: ScoreForm() for match in matchs} 
    
    return render(request, 'tournoisFoot/saisirScores.html', {'tournoi': tournoi, 'matchs': matchs, 'forms': forms})



def tournoiDetails(request):
    if 'HTTP_X_REQUESTED_WITH' in request.META and request.META['HTTP_X_REQUESTED_WITH'] == 'XMLHttpRequest' and request.method == 'GET':
        tournoi_id = request.GET.get('tournoi_id')
        tournoi = get_object_or_404(Tournoi, pk=tournoi_id)
        equipes = processTournoiDetails(tournoi)

        html_response = render(request, 'tournoisFoot/tournoiDetails.html', {'tournoi': tournoi, 'equipes': equipes})
        return JsonResponse({'html': html_response.content.decode('utf-8')})
    else:
        return JsonResponse({'error': 'Invalid request'})





