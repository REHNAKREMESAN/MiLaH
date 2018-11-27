from django.shortcuts import render, redirect
from .import forms
from django.contrib.auth import authenticate


def adminhome(request):
    return render(request, 'HomepageAdmin/homepageadmin.html', {'logid': request.session['logid']})


def login(request):
    if request.method == 'POST':
        form = forms.AdminLoginForms(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            password = userObj['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                request.session['logid'] = user.id
                request.session['logname'] = user.username
                return redirect('admin_login:adminhome')
            else:
                return render(request, 'admin_login/admin_login.html', {'form': form})
    else:
        form = forms.AdminLoginForms()
    return render(request, 'admin_login/admin_login.html', {'form': form})




# Create your views here.
