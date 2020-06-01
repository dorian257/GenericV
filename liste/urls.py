from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [

    path('formulaire',views.formulaire , name='formulaire1'),
    path('faq',views.FAQView.as_view()),
    path('list', views.ListPersonne.as_view() ,name= 'liste'),
    path ('detail/<pk>' ,views.Pers.as_view(), name= 'detail'),
    path ('nouveau' ,views.New.as_view(),name='formulaire'),
    path ('update/<pk>' ,views.Update1.as_view(),name='update'),
    path ('delete/<pk>' , views.Sup.as_view()),
    path ('voir1',views.AffichageC.as_view(),name='vueClasse'),
    path('formulaire1',views.FormulaireC.as_view(),name='classe'),




]