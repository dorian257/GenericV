from django.urls import path
from .import views

urlpatterns = [

    path('accueil' ,views.AccueilView.as_view(),name='accueil'),

    path ('affichage',views.AffichageView.as_view(),name='affichage'),
    path('list', views.ListePersonnelView.as_view() ,name= 'liste'),

    path ('nouveau' ,views.NewView.as_view(),name='nouveau'),
    path('formulaire',views.FormulaireView.as_view(),name='formulaire'),
    path('formulairemodel',views.formulaire, name='formulaire1'),

    path ('detail/<int:pk>' ,views.EmployeView.as_view(), name= 'detail'),

    path ('update/<int:pk>' ,views.UpdateView.as_view(),name='update'),

    path ('delete/<int:pk>' , views.SupprimerView.as_view(),name='delete'),



]