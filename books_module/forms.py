from django import forms
from .models import BookComments
from django.core import validators


class CommentsModelForm(forms.ModelForm):
    class Meta:
        model = BookComments
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5
            })
        }
