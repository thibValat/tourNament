from django.contrib import admin
from .models import Equipe, Match, Tournoi

# Register your models here.
admin.site.register(Equipe)
admin.site.register(Match)
admin.site.register(Tournoi)