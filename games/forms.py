from django import forms
from . import models

class UploadGame(forms.ModelForm):
    class Meta:
        model = models.Game
        fields = ['title', 'url', 'price', 'high_scores', 'description', 'slug', 'thumb']