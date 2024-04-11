from django.urls import path
from .views import index, addTournoiForm, saisirScores, tournoiDetails
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    path('', index, name='indexFoot'),
    path('addTournoiForm/', addTournoiForm, name='addTournoiForm'),
    path('saisir_scores/<int:tournoi_id>/', saisirScores, name='saisirScores'),
    path('tournoiDetails/', tournoiDetails, name='tournoiDetails'),
    path('admin/', admin.site.urls, name='adminFoot'),
]