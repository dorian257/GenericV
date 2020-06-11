from django.contrib.admin.templatetags.admin_list import result_list
from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser



# Create your models here.

"""Les deux classes suivant permettent de creer un custom manager qui filtre un prenom"""

class PersonneQuery(models.QuerySet):
    def prenom(self):
        return self.filter(Prenom='Dorian')


class PersonneManager(models.Manager):
    def get_queryset(self):
        return PersonneQuery(self.model,using=self._db)


    def prenom(self):
        return self.get_queryset().prenom()

class Personne (models.Model):

    Nom = models.CharField(max_length=20)
    Prenom = models.CharField(max_length=20)
    Profession = models.CharField(max_length=50)
    photo = models.ImageField()

    objects = PersonneManager()

def __str__(self):
        return self.Prenom








