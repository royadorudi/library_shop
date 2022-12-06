from django import forms
from location_field.forms.plain import PlainLocationField


class SiteLocationMapForm(forms.Form):
    city = forms.CharField(label='شهر')
    location = PlainLocationField(based_fields=['city'],
                                  initial='35.49682292143212,51.22928559780121')
