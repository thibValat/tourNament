from django.shortcuts import render

def index(request):
    tournois = [
        {"name": "Football", "url": "indexFoot"},
        {"name": "Tennis", "url": "indexTennis"},
        {"name": "Basket", "url": "indexBasket"},
        {"name": "Formule 1", "url": "indexFormule"},
    ]

    return render(request, 'index.html', {'tournois': tournois})
