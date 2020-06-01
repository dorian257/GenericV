from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .models import Personne
from .forms import PersonneForm,Personal
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView


# Create your views here.

#une fonction qui affiche tout les personnes
def affichage (request) :

    var1 = Personne.objects.all()
    return render(request,'liste/affichage.html',{'post':var1})

#un formulaire de notre model

def formulaire (request) :
    form = PersonneForm(request.POST or None)
    return render(request , 'liste/formulaire.html',locals())

#classe FAQView qui affiche simplement un template a l'utilasateur
class FAQView (TemplateView):
    template_name = 'liste/faq.html'


#classe ListView qui affiche une liste d'object en quelques lignes
class ListPersonne (ListView):

    model = Personne
    context_object_name = 'Personne'
    template_name = 'liste/list.html'

#classe DetailView qui affiche un object
class Pers (DetailView):
    model = Personne
    context_object_name = 'Personne'
    template_name = 'liste/obj.html'

#classe CreateView
class New (CreateView):
    model = Personne
    template_name = 'liste/formulaire.html'
    form_class = PersonneForm
    success_url = reverse_lazy()

#classe UpdateView
class Update1 (UpdateView):
    model = Personne
    template_name = 'liste/formulaire.html'
    form_class = PersonneForm
    success_url = reverse_lazy()

class Sup (DeleteView):
    model = Personne
    template_name = 'liste/delete.html'
    context_object_name = 'Personne'
    success_url = reverse_lazy()

def via (request):
    form = Personal(request.POST  or None)

    if form.is_valid():
        Nom = form.cleaned_data['Nom']
        Prenom = form.cleaned_data['Prenom']
        Profession = form.cleaned_data['Profession']
        Photo = form.cleaned_data['Photo']

        envoi = True

    return render(request,'liste/via.html',locals())



def mod (request):

    indent = Personne.objects.Nom()
    form = Personal(instance=indent)

    return (request,'list/via.html',locals())