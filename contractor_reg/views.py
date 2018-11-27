from django.shortcuts import render, redirect
from . import forms
from django.core.mail import EmailMessage


def contractor_reg(request):

    if request.method == 'POST':
        form = forms.ContractorForms(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            obj = form.cleaned_data
            mail = obj['email']
            username = obj['username']
            password = obj['password']
            instance.save()
            email = EmailMessage('Contractor Registration', 'Congratulations successfully registered      username:   '+username+'    password:    '+password, to=[mail])
            email.send()
            return redirect('mainhome:mainhome')
    else:
        form = forms.ContractorForms

    return render(request, "ContractorReg/registration.html", {'form': form})
