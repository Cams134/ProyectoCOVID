from django import forms
from .models import registros

class registrosForm(forms.ModelForm):
    class Meta:
        model= registros
        fields= ["dia", "covid", "sintomas"]
