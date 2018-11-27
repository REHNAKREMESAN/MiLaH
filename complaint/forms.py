from django import forms
from . import models


class ComplaintForms(forms.ModelForm):
    description = forms.CharField(
        required=True,
        label='description',
        max_length=30,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter numeric character only'})
    )

    class Meta:
        model = models.Complaint
        fields = ['employee_name', 'description', 'complaint_date']
