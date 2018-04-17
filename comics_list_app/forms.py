from django import forms
from .models import ComicsList


class ComicsListForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    volume = forms.IntegerField()
    username = forms.CharField(max_length=30)

    class Meta:
        model = ComicsList
        fields = ('title', 'volume', 'username')
