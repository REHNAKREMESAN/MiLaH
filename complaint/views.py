from django.shortcuts import render, redirect
from . import forms
from .models import Complaint


def complaint(request):
    login_id = request.session['logid']
    model_object = Complaint.objects.filter(contractor_id=login_id)
    if request.method == 'POST':
        form = forms.ComplaintForms(request.POST, request.FILES)
        if form.is_valid():
            ComObj = form.cleaned_data
            employee_name = ComObj['employee_name']
            description = ComObj['description']
            complaint_date = ComObj['complaint_date']
            a = Complaint(contractor_id=request.session['logid'], employee_name=employee_name, description=description,
                          complaint_date=complaint_date)
            a.save()
        return redirect('complaint:ComplaintForms')
    else:
        form = forms.ComplaintForms
    return render(request, "complaint/complaint.html", {'form': form, 'data': model_object})



