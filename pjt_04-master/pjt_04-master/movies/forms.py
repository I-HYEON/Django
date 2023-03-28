from .models import Movie
from django import forms

class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields ='__all__'
        widgets = {
            'genre': forms.Select(choices=[('comedy','코미디'),('horror','공포'),('romance','로맨스')]),
            'score': forms.NumberInput(attrs={'type':'number','step':0.5,'min':0,'max':5}),
            'release_date':forms.DateInput(attrs={'type':'date'}),
        }