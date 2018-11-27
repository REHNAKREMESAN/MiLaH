from django.shortcuts import render, redirect, get_object_or_404
from .import forms
from .models import ChitRequest


def chitrequest(request):
    login_id = request.session['logid']
    model_object = ChitRequest.objects.filter(members_name=login_id)

    if request.method == 'POST':
        form = forms.ChitRequestForms(request.POST, request.FILES)
        if form.is_valid():
            chitobj=form.cleaned_data
            chit_name = chitobj['chit_name']
            c = ChitRequest(chit_name=chit_name, members_name=login_id)
            c.save()
            return redirect('chit_request:chit_request')
    else:
        form = forms.ChitRequestForms

    return render(request, "chit_request/chit_request.html", {'form': form, 'data': model_object})


