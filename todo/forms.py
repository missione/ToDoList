from django import forms
from django.db.models import fields

from django.forms import ModelForm

from .models import *

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields= '__all__'