from django import forms
from account_module.models import User
from django.core import validators
from django.core.exceptions import ValidationError


class EditProfileModelForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'avatar', 'address', 'about_user']
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }),
            'avatar': forms.FileInput(attrs={
                'class': 'form-control'
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 3,
                'id': 'message'
            }),
            'about_user': forms.Textarea(attrs={
                'class': 'form-control',
                'row': 6,
                'id': 'message'
            }),
        }


class ChangePasswordForm(forms.Form):
    current_pass = forms.CharField(
        label='کلمه عبور فعلی',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    new_pass = forms.CharField(
        label='کلمه عبور جدید',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
    confirm_new_pass = forms.CharField(
        label='تکرار کلمه عبور جدید',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control'
            }
        ),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    def clean_confirm_password(self):
        new_pass = self.cleaned_data.get('new_pass')
        confirm_new_pass = self.cleaned_data.get('confirm_new_pass')

        if new_pass == confirm_new_pass:
            return confirm_new_pass

        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')
