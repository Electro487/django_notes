from django.forms import ModelForm, TextInput, Select, Textarea, PasswordInput
from django import forms
from .models import Note, NoteType, User

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

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": TextInput(attrs={"class": "form-control"}),
            "password": PasswordInput(attrs={"class": "form-control"})
        }

        help_texts = {
            "username": ()
        }