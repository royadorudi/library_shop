from django import forms
from .models import ContactUs
from django.core import validators


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['title', 'full_name', 'email', 'phone_number', 'message']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message'
            }),
        }
        validators = [
            validators.MaxLengthValidator(100),
            validators.EmailValidator,
        ]
