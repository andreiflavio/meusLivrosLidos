from django import forms
from .models import Livro


class LivroForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(LivroForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
   
    class Meta:
        model = Livro
        fields = [
            'nome',
            'autor',
            'serie',
            'num_paginas',
            'inicio',
            'fim',
            'nota',
            'ebook']
        widgets = {
            'inicio': forms.DateInput(),
            'fim': forms.DateInput(),
            'user':  forms.HiddenInput(),
        }

