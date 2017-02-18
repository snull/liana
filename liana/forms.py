from django import forms
from . import models

class PostForm(forms.ModelForm):
    content = forms.CharField(),

    class Meta:
        model = models.Post
        fields = ('user', 'text')
