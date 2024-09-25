from django import forms 
from .models import clientes


class clientesForm(forms.ModelForm):
    class Meta:
        model = clientes
        fields = '__all__'

