from django import forms
from .models import Personne

class PersonneForm (forms.ModelForm):

    class Meta :
        model = Personne
        fields = '__all__'

class StafForm (forms.Form):
    Nom = forms.CharField(max_length=20)
    Prenom = forms.CharField()
    Profession = forms.CharField(widget=forms.Textarea)
    Photo = forms.ImageField()

