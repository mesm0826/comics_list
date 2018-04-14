from django import forms
from .models import ComicsList

class ComicsListForm(forms.ModelForm):
    class Meta:
        model = ComicsList
        fields = ("title", "volume")
