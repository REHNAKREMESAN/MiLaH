from django import forms
from .import models


class ChitRequestForms(forms.ModelForm):

    class Meta:
        model = models.ChitRequest
        fields = ['chit_name']
