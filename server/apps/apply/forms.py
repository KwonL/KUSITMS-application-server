from django import forms
from .models import ApplyForm


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplyForm
        exclude = ['user']
