from django.db import models

class Equipe(models.Model):
    nom = models.CharField(max_length=100)
    logo = models.URLField()
    
    def __str__(self):
        return self.nom

class Tournoi(models.Model):
    nom = models.CharField(max_length=100)
    equipes = models.ManyToManyField(Equipe)

    def __str__(self):
        return self.nom


class Match(models.Model):
    tournoi = models.ForeignKey(Tournoi, on_delete=models.CASCADE)
    equipe1 = models.ForeignKey(Equipe, related_name='equipe1', on_delete=models.CASCADE)
    equipe2 = models.ForeignKey(Equipe, related_name='equipe2', on_delete=models.CASCADE)
    score_equipe1 = models.IntegerField(null=True, blank=True)
    score_equipe2 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.equipe1} vs {self.equipe2}"
