from django import forms
from .models import Movie

class moviform(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'des', 'year', 'img']
