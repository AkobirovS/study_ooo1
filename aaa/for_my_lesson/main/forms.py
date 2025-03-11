from django import forms
from django.core.exceptions import ValidationError
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ['title','image','content']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'class': 'form-control',
            'placeholders': 'title',
            'id': 'exampleInputTitle'

        })
        self.fields['image'].widget.attrs.update({
            'class': 'form-control'
        })
        self.fields['content'].widget.attrs.update({
            'class': 'form-control',
            'cols': 60,
            'rows': 5,
            'placeholders': 'title',
            'id': 'exampleInputContent'
        })