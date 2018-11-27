from django import forms
from .import models


class ChitForms(forms.ModelForm):

    chit_amount = forms.CharField(
        required=True,
        label='chit_amount',
        max_length=6,
        widget=forms.TextInput(attrs={'pattern': '[0-9]+', 'title': 'enter numeric character only'})
    )


    class Meta:
        model = models.Chit
        fields = ['chit_name', 'chit_amount', 'chit_start_date']
