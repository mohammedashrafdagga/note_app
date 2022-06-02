from django import forms
from .models import Note, Category


class NoteForm(forms.ModelForm):

    class Meta:
        model = Note
        fields = ['title', 'desc', 'category']


class CreteCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']
