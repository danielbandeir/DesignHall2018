from django import forms
from django.forms import ModelForm
from .models import *

class pessoaForm(ModelForm):
    class Meta:
        model = pessoa
        fields = ['email_pessoa']
