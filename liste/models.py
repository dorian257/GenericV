from django.db import models

# Create your models here.

class Personne (models.Model):

    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Profession = models.CharField(max_length=50)
    photo = models.ImageField()

def __str__(self):
        return self.Prenom
