from django import forms
from apps.galeria.models import photographs

class PhotographyForms(forms.ModelForm):
    class Meta:
        model = photographs
        exclude = [
            'publication',
        ]
        labels={
            'name':'Nome',
            'credit':'Créditos',
            'category':'Categoria',
            'title':'Titulo',
            'text':'Descrição',
            'photo':'Foto',
            'date_publication':'Data de publicação',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'credit': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'class':'form-control'}),
            'photo': forms.FileInput(attrs={'class':'form-control'}),
            'date_publication': forms.DateInput(
                format='%d%m%Y',
                attrs={
                    'type':'date',
                    'class':'form-control'
                }
            ),
            'user': forms.Select(attrs={'class':'form-control'}),
        }