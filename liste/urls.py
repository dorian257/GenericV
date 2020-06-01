from django.urls import path
from django.conf.urls import url
from .import views

urlpatterns = [
    path ('voir', views.affichage),
    path('formulaire',views.formulaire , name='formulaire1'),
    path('faq',views.FAQView.as_view()),
    #path('list',views.ListPersonne.as_view(), name= 'liste'),
    url(r'^list$', views.ListPersonne.as_view() ,name= 'liste'),
    url (r'^detail/(?P<pk>\d+)$' ,views.Pers.as_view(), name= 'detail'),
    url (r'^nouveau$' ,views.New.as_view(),name='formulaire'),
    url (r'^update/(?P<pk>\d+)$' ,views.Update1.as_view(),name='update'),
    url (r'^delete/(?P<pk>\d+)$' , views.Sup.as_view()),
    url (r'^dorian$' ,views.via , name='dorian'),
    url (r'^modifier$' ,views.mod ,name='modifier'),


]