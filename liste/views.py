from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

from .models import Personne
from .forms import PersonneForm,StafForm
from django.views import View
from django.utils.decorators import method_decorator


# Create your views here.

#vue permettant d'afficher la page d'accueil
class AccueilView (View):
    def get (self,request):
        var1 = Personne.objects.all()
        return render(request,'liste/accueil.html',{'post':var1})



#une fonction qui affiche tout le personnel et leur profession
class AffichageView (View):

    def get (self,request):
        var1 = Personne.objects.all()
        return render(request,'liste/affichage.html',{'post':var1})


#La liste des noms des employes
class ListePersonnelView (ListView):

    model = Personne
    context_object_name = 'Personne'
    template_name = 'liste/list.html'


"""Les trois classes suivant permet de creer une vue qui ajouter un employe.
   On peut utiliser une de ces classes
   """

#vue generique CreateView
class NewView (LoginRequiredMixin,CreateView):
    model = Personne
    template_name = 'liste/formulaire.html'
    form_class = PersonneForm
    success_url = reverse_lazy('liste')

#une classe avec un methode get et un methode post
class FormulaireView (LoginRequiredMixin,View):

    form_class = StafForm
    initial = {'key':'value'}
    template_name = 'liste/formulaire.html'

    def get(self,request,*args,**kwargs):
        form = self.form_class(initial={'key':'value'})
        return render(request,'liste/formulaire.html',locals())


    def post (self,request,*args,**kwargs):
        form =self.form_class(request.POST or None,request.FILES)

        if form.is_valid():
            Nom = form.cleaned_data['Nom']
            Prenom = form.cleaned_data['Prenom']
            Profession = form.cleaned_data['Profession']
            Photo = form.cleaned_data['Photo']

            envoi = True

            return HttpResponseRedirect(reverse_lazy('liste'))

        return render (request,'liste/formulaire.html',locals())


#vue du formulaire a partir de notre model qui exige l'aunthification
@login_required()
def formulaire (request) :
    form = PersonneForm(request.POST or None)
    return render(request , 'liste/formulaire.html',locals())



#vue permettant l'affichage des details d'un employe
class EmployeView (DetailView):
    model = Personne
    context_object_name = 'Personne'
    template_name = 'liste/employe.html'



"""Les Deux classes suivant permet de creer une vue qui modifier un employe.
   """

#vue generique UpdateView
class UpdateView (UpdateView):
    model = Personne
    template_name = 'liste/update.html'
    form_class = PersonneForm
    success_url = reverse_lazy('liste')
    context_object_name = 'Personne'

#vue affichant tout les employe afin de choisir celui qu'on veut modifier
class ModifyView (LoginRequiredMixin,ListView):
    model = Personne
    context_object_name = 'Personne'
    template_name = 'liste/modify.html'



"""Les Deux classes suivant permet de creer une vue qui supprime un employe.
   """

#vue generique DeleteView
class SupprimerView (DeleteView):
    model = Personne
    template_name = 'liste/supprimer.html'
    context_object_name = 'Personne'
    success_url = reverse_lazy('liste')

#vue affichant tout les employe afin de choisir celui qu'on veut supprimer
class DeleteView (LoginRequiredMixin,ListView):
    model = Personne
    context_object_name = 'Personne'
    template_name = 'liste/delete.html'




