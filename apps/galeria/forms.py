# Licença: CC BY-NC 4.0
# Este código pode ser usado, modificado e redistribuído **apenas para fins não comerciais**.
# Mais detalhes: https://creativecommons.org/licenses/by-nc/4.0/

from django import forms
from datetime import datetime
from apps.galeria.models import photographs

class PhotographyForms(forms.ModelForm):
    class Meta:
        model = photographs
        exclude = [
            'publication', 'user', 'date_publication',
        ]
        labels={
            'name':'Nome',
            'credit':'Créditos',
            'category':'Categoria',
            'title':'Titulo',
            'text':'Descrição',
            'photo':'Foto',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'credit': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
        }