from django import forms
from . import models


class ContractorForms(forms.ModelForm):
    contractor_name = forms.CharField(
        required=True,
        label='contractor_name',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})
    )
    house_name = forms.CharField(
        required=True,
        label='house_name',
        max_length=32,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})
    )
    street = forms.CharField(
        required=True,
        label='street',
        max_length=25,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )
    city = forms.CharField(
        required=True,
        label='city',
        max_length=25,
        widget=forms.TextInput(attrs={'pattern': '[A-Za-z ]+', 'title': 'enter character only'})

    )

    username = forms.CharField(
        required=True,
        label='Username',
        max_length=20
    )
    password = forms.CharField(
        required=True,
        label='Password',
        max_length=15,
        widget=forms.PasswordInput()
    )

    class Meta:
        model = models.ContractorReg
        fields = ['contractor_name', 'house_name', 'street', 'city', 'contact', 'email', 'state', 'district', 'gender',
                  'licence', 'username', 'password', 'security_question', 'security_answer']



