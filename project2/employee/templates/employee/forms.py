from django import forms
from .models import Club,Department

class SearchForm(forms.Form):
    club = forms.ModelChoiceField(
        queryset=Club.objects,label='circle',required=False
    )
    department = forms.ModelChoiceField(
        queryset=Department.objects,label='department',required=False
    )
