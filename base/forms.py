from django.forms import ModelForm, TextInput, Select, Textarea
from django import forms
from .models import Note, NoteType

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ["name", "type", "description"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"}),
            "type": Select(attrs={"class":"form-select"}),
            "description": Textarea(attrs={"class":"form-control"})
        }

class NoteFormType(ModelForm):
    class Meta:
        model = NoteType
        fields = ["name"]
        widgets = {
            "name": TextInput(attrs={"class": "form-control"})
        }